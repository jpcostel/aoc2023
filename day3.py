from common import *

def calculate_part_sum(input_file, gear_ratios = False):
    input_lines = open(input_file, 'r')
    input_matrix = []
    for line in input_lines:
        input_matrix.append(line.strip())
    numbers = set()
    if gear_ratios:
        symbols = '*'
        neighbor_count = 2
        result = 0
        for i in range(len(input_matrix)):
            for j in range(len(input_matrix[0])):
                if input_matrix[i][j] in symbols:
                    temp_result = check_neighbors((i,j), input_matrix, neighbor_count)
                    gr = 1
                    if temp_result:
                        for item in temp_result:
                            row = item[0][0]
                            start = item[0][1]
                            end = item[1][1] + 1
                            line = input_matrix[row]
                            gr = gr * int(line[start:end])
                        result = result + gr
        return result

    else:
        symbols = '!@#$%^&*()-_=+[{]}\|;:/?><,'
        neighbor_count = 0
        for i in range(len(input_matrix)):
            for j in range(len(input_matrix[0])):
                if input_matrix[i][j] in symbols:
                    temp_result = check_neighbors((i,j), input_matrix, neighbor_count)
                    if temp_result:
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

def check_neighbors(coords, matrix, neighbor_count):
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
    if neighbor_count:
        if len(result) == neighbor_count:
            return result
    else:
        return result