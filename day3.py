from common import *

def calculate_part_sum(input_file):
    symbols = '!@#$%^&*()-_=+[{]}\|;:/?><,'
    input_lines = open(input_file, 'r')
    input_matrix = []
    for line in input_lines:
        input_matrix.append(line.strip())
    numbers = set()
    for i in range(len(input_matrix)):
        for j in range(len(input_matrix[0])):
            if input_matrix[i][j] in symbols:
                temp_result = check_neighbors((i,j),input_matrix)
                for item in temp_result:
                    numbers.add(item)
    result = 0
    for number in numbers:
        left = number[0]
        right = number[1]
        part_text = input_matrix[left[0]][left[1]:right[1]+1]
        part_number = int(part_text)
        result += part_number
    return result

def print_indexed(in_line, line_number):
    count = 0
    header = str(line_number)
    out_line = str(line_number)
    for item in in_line:
        header = header + '\t' + str(count)
        out_line = out_line + '\t' + item
        count = count + 1
    print(header)
    print(out_line)

def get_number_bounds(coords, matrix):
    i = coords[0]  # Row
    j = coords[1]  # Column
    numbers = '0123456789'
    # find the left boundary
    found = False
    while not found:
        if (j-1) >= 0:
            if matrix[i][j-1] in numbers:
                j = j - 1
            else:
                found = True
        else:
            found = True
    left = (i, j)
    j = coords[1]
    # find the right boundary
    found = False
    while not found:
        if (j + 1) < len(matrix[0]):
            if matrix[i][j + 1] in numbers:
                j = j + 1
            else:
                found = True
        else:
            found = True
    right = (i, j)
    return (left, right)

def check_neighbors(coords, matrix):
    i = coords[0]   # Row
    j = coords[1]   # Column
    result = set()
    numbers = '0123456789'
    upper = (i-1) >= 0
    left = (j-1) >= 0
    right = (j+1) < len(matrix[0])
    lower = (i+1) < len(matrix)
    if upper:
        if left:
            if matrix[i-1][j-1] in numbers:
                result.add(get_number_bounds((i-1, j-1), matrix))
        if matrix[i-1][j] in numbers:
            result.add(get_number_bounds((i-1, j), matrix))
        if right:
            if matrix[i-1][j+1] in numbers:
                result.add(get_number_bounds((i-1, j+1), matrix))
    if left:
        if matrix[i][j-1] in numbers:
            result.add(get_number_bounds((i, j-1), matrix))
    if right:
        if matrix[i][j+1] in numbers:
            result.add(get_number_bounds((i, j+1), matrix))
    if lower:
        if left:
            if matrix[i+1][j-1] in numbers:
                result.add(get_number_bounds((i+1, j-1), matrix))
        if matrix[i+1][j] in numbers:
            result.add(get_number_bounds((i+1, j), matrix))
        if right:
            if matrix[i+1][j+1] in numbers:
                result.add(get_number_bounds((i+1, j+1), matrix))
    return result