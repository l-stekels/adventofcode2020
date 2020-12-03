with open('input.txt') as input_file:
    input_array = input_file.readlines()

input_array = [int(item.strip()) for item in input_array]

def answer(array):
    for number in array:
        for check in array:
            if check + number == 2020:
                print(check * number)
                return


# answer(input_array)
