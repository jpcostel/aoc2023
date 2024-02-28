def get_mins(game):
    result = {}
    result['total'] = 0
    result['blue'] = 0
    result['green'] = 0
    result['red'] = 0
    [game_number, reveals] = game.split(":")
    result['game'] = int(game_number.replace("Game ", ''))
    for reveal in reveals.split(";"):
        total = 0
        color_counts = reveal.strip().split(",")
        for color_count in color_counts:
            color_count_split = color_count.strip().split(" ")
            count = color_count_split[0]
            color = color_count_split[1]
            count = int(count)
            total += count
            if count > result[color]:
                result[color] = count
        if total > result['total']:
            result['total'] = total
    return result

def process_mins(filename):
    lines = open(filename, 'r')
    answer = 0
    for game in lines:
        min = get_mins(game)
        power = min['red'] * min['green'] * min['blue']
        answer += power
        # print("Game {}: Red: {}, Green: {}, Blue: {}".format(min['game'], min['red'], min['green'], min['blue']))
        # if min['red'] <= 12 and min['green'] <= 13 and min['blue'] <= 14:
        #     answer += min['game']
    print(answer)