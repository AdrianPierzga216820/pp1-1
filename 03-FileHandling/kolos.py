import re


def suma_cyfr():
    with open('dane.txt', 'r') as file:
        return sum([int(n) for line in file for number in re.findall(r'\d+', line) if 10 <= int(number) < 500 for n in number])
