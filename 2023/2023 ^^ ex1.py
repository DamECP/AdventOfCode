numbers = [
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    "0",
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
    "zero",
]

int_dict = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
    "zero": "0",
}


def result(numbers: tuple) -> int:
    new_number = []
    for elt in numbers:
        if elt.isdigit():
            new_number.append(elt)
        else:
            elt = int_dict[elt]
            new_number.append(elt)
    print(new_number)

    return int("".join(new_number))


total = 0
with open("ex1.txt") as exercise:
    data_list = []
    for line in exercise:
        print(line)
        line = line.replace("\n", "")
        extreme_numbers = []
        for number in numbers:
            index = line.find(number)
            while index != -1:
                extreme_numbers.append((index, number))
                index = line.find(number, index + 1)
        print(extreme_numbers)
        print(min(extreme_numbers), max(extreme_numbers))
        min_value = min(extreme_numbers, key=lambda x: x[0])[1]
        max_value = max(extreme_numbers, key=lambda x: x[0])[1]
        data_list.append((min_value, max_value))
        print(min_value, max_value)
        print(result((min_value, max_value)))
        print()
        total += result((min_value, max_value))

print(total)
"""total = 0
for i in data_list:
    total += result(i)

print(total)"""
