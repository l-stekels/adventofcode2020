with open('input.txt') as input_file:
    input_array = [item.strip() for item in input_file.readlines()]


class Password:
    def __init__(self, min_len, max_len, symbol, pwd):
        self.min = min_len
        self.max = max_len
        self.letter = symbol
        self.password = pwd

    def symbol_in_pwd(self):
        return self.password.count(self.letter)

    def password_valid(self):
        if len(self.password) >= self.max:
            first = self.password[self.min - 1]
            second = self.password[self.max - 1]
            return first == self.letter != second or first != self.letter == second
        return False


password_list = []
for item in input_array:
    split = item.split()
    lengths = split[0].split('-')
    letter = split[1][0]
    password_list.append(Password(int(lengths[0]), int(lengths[1]), letter, split[2]))

valid_passwords = 0
for password in password_list:
    if password.password_valid():
        valid_passwords += 1

print(valid_passwords)