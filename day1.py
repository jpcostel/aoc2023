import re

debug = False

def dprint(text):
    if debug:
        print(text)

def get_cal_sum(in_file):
    lines = open(in_file, 'r')
    cal_sum = 0
    for counter, line in enumerate(lines):
        line_cal = get_cal(line)
        cal_sum += line_cal
        dprint("{} {}".format(counter, line_cal))
    return cal_sum

def get_cal(line):
    # line_digits = re.sub('\D', '', line)
    line_digits = get_digits(line)
    line_cal = int(line_digits[0]+line_digits[-1])
    return line_cal

def get_digits(line):
    alpha_digits = {'one':'1',
                    'two':'2',
                    'three':'3',
                    'four':'4',
                    'five':'5',
                    'six':'6',
                    'seven':'7',
                    'eight':'8',
                    'nine':'9'}
    number_digits = '123456789'
    digits = ""
    for i in range(len(line)):
        if line[i] in number_digits:
            digits = digits + line[i]
        elif line[i:i+3] in alpha_digits:
            digits = digits + alpha_digits[line[i:i+3]]
        elif line[i:i+4] in alpha_digits:
            digits = digits + alpha_digits[line[i:i+4]]
        elif line[i:i+5] in alpha_digits:
            digits = digits + alpha_digits[line[i:i+5]]
    return digits
