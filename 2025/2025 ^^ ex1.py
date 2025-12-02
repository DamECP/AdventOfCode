from collections import deque

with open("ex1.txt") as exercise:
    data = [i.strip() for i in exercise.readlines()]


def answer_1():
    numbers = deque((range(100)))
    numbers.rotate(50)
    password = 0

    for i in data:

        direction = i[0]
        rotation = int(i[1:])

        if direction == "R":
            rotation = -rotation

        numbers.rotate(rotation)

        if numbers[0] == 0:
            password += 1

    return password


def answer_2():
    numbers = deque((range(100)))
    numbers.rotate(50)
    password = 0

    for i in data:

        direction = i[0]
        rotation = int(i[1:])

        for n in range(rotation):
            if direction == "R":
                numbers.rotate(-1)
            else:
                numbers.rotate(1)

            if numbers[0] == 0:
                password += 1

    return password


if __name__ == "__main__":
    print(answer_1())
    print(answer_2())
