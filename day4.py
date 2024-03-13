def calculate_points(infile):
    result = 0
    # open and read input file
    lines = open(infile, 'r')
    # parse each line, calculate the line's points
    for line in lines:
        card_number, match_count, line_score = get_line_score(line)
        result = result + line_score
    return result


class Scratcher():
    def __init__(self, text):
        import re
        winning_numbers, test_numbers = text.split('|')
        card_number, winning_numbers = winning_numbers.split(':')
        self.number = card_number.replace("Card", "").strip()
        self.winning_numbers = re.split(" +", winning_numbers.strip())
        self.test_numbers = re.split(" +", test_numbers.strip())
        self.match_count = 0
        self.card_count = 1

    def get_match_count(self):
        for number in self.test_numbers:
            if number in self.winning_numbers:
                self.match_count += 1


def calculate_card_count(infile):
    result = 0
    cards = []
    lines = open(infile, 'r')
    for line in lines:
        card = Scratcher(line.strip())
        card.get_match_count()
        cards.append(card)
    for i in range(len(cards)):
        for j in range(1,cards[i].match_count+1):
            if i+j < len(cards):
                cards[i+j].card_count += cards[i].card_count
    for card in cards:
        result = result + card.card_count
    return result


def get_line_score(line):
    import re
    winning_numbers, test_numbers = line.split('|')
    card_number, winning_numbers = winning_numbers.split(':')
    card_number = card_number.replace("Card", "").strip()
    winning_numbers = re.split(" +", winning_numbers.strip())
    test_numbers = re.split(" +", test_numbers.strip())
    match_count = 0
    for number in test_numbers:
        if number in winning_numbers:
            match_count += 1
    if match_count:
        line_score = 2 ** (match_count - 1)
    else:
        line_score = 0
    return card_number, match_count, line_score
