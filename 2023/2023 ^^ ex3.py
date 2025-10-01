import re
import string
from math import prod

with open("ex3.txt") as exercise:
    data = exercise.read().split("\n")


class Symbol:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def around(self):
        return [
            (self.x - 1, self.y - 1),
            (self.x, self.y - 1),
            (self.x + 1, self.y - 1),
            (self.x - 1, self.y),
            (self.x, self.y),
            (
                self.x + 1,
                self.y,
            ),
            (self.x - 1, self.y + 1),
            (self.x, self.y + 1),
            (self.x + 1, self.y + 1),
        ]

    def __repr__(self):
        return f"* : x = {self.x} ; y = {self.y}"


class Number:
    def __init__(self, value, x, y):
        self.x = x
        self.y = y
        self.value = value
        self.len = len(str(value))

    def coordinates(self):
        coordinates = []
        for i in range(self.len):
            coordinates.append((self.x + i, self.y))
        return coordinates


regex = r"\d+"
all_numbers = []


# Part 1

valid_punctuation = list(string.punctuation)
valid_punctuation.remove(".")

symbols = []
gears = []

for y, line in enumerate(data):
    # identifies each number in the line
    numbers_found = re.finditer(regex, line)
    for elt in numbers_found:
        elt = Number(elt.group(), elt.span()[0], y)
        all_numbers.append(elt)

    for x, char in enumerate(line):
        # if char != "." and not char.isdigit():
        # char = Symbol(x, y)
        # symbols.append(char)
        if char == "*":
            char = Symbol(x, y)
            gears.append(char)


all_symbols_coordinates = [coord for i in symbols for coord in i.around()]
all_numbers_coordinates = [coord for i in all_numbers for coord in i.coordinates()]

all_gears_coordinates = [coord for i in gears for coord in i.around()]

"""
total = 0
for number in all_numbers:
    for coord in number.coordinates():
        if coord in all_symbols_coordinates:
            total += int(number.value)
            print(number.value)
            print(number.x, number.y)
            break
print(total)

"""

total = 0
for gear in gears:
    adjacent = []
    for number in all_numbers:
        for coord in number.coordinates():
            if coord in gear.around():
                adjacent.append(int(number.value))
                break
    if len(adjacent) == 2:
        total += prod(adjacent)

print(total)
