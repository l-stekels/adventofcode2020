from day1_part1 import input_array
from itertools import product

values = product(input_array, input_array, input_array)

for value in values:
    if sum(value) == 2020:
        print(value[0] * value[1] * value[2])
        break

