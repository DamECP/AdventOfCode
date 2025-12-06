from functools import reduce
from operator import mul

with open("ex6.txt") as exercise:
    data = [i.replace("\n", "") for i in exercise.readlines()]


def part_1(data=data):
    data = [line.split() for line in data]
    for _ in range(len(data[0])):
        current = [line[_] for line in data]
        numbers = [int(i) for i in current if i.isdigit()]
        operator = current[-1]
        yield (numbers, operator)


def part_2(data=data):
    data = [list(line.rstrip("\n")) for line in data]
    data = [line[::-1] for line in data]

    numbers = []
    for _ in range(len(data[0])):
        current = [elt[_] for elt in data if elt[_] != " "]
        if current:
            if "*" in current or "+" in current:
                number = int("".join([i for i in current[:-1] if i.isdigit()]))
                numbers.append(number)
                operator = current[-1]
                yield (numbers, operator)
                numbers = []
            else:
                number = int("".join([i for i in current if i.isdigit()]))
                numbers.append(number)


def get_result(current: tuple) -> int:
    if current[1] == "*":
        return reduce(mul, current[0])
    return sum(current[0])


answer_1 = 0
for current in part_1():
    answer_1 += get_result(current)

answer_2 = 0
for current in part_2():
    answer_2 += get_result(current)

print(answer_1)
print(answer_2)
