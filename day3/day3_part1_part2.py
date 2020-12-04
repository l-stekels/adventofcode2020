from itertools import cycle
from math import ceil

with open('input.txt') as input_file:
    input_array = [item.strip() for item in input_file.readlines()]


# Weird solution, why I didn't use multi dimensional array??
def ans(array, left, down):
    finish = len(array)
    line_end = len(array[0])
    current_line = 0
    curr_location = left
    result = 0
    for line in cycle(array):
        if current_line >= finish:
            break
        multi = int(ceil(curr_location / line_end)) + 1
        if current_line != 0 and current_line % down == 0:
            line_to_check = multi * line
            result += 1 if line_to_check[curr_location] == '#' else 0
            curr_location += left
        current_line += 1
    return result


print(ans(input_array, 1, 1) * ans(input_array, 3, 1) * ans(input_array, 5, 1) * ans(input_array, 7, 1) * ans(input_array, 1, 2))
