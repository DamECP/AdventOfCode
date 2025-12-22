with open("ex2.txt") as exercise:
    data = exercise.read()
    data = [int(i.strip()) for i in data.split(",")]

positions = {i: data[i] for i in range(len(data))}


def op_1(n1, n2, n3):
    positions[n3] = positions[n1] + positions[n2]


def op_2(n1, n2, n3):
    positions[n3] = positions[n1] * positions[n2]


i = 0

while i < len(data):

    ref = positions[i]

    if ref == 99:
        break

    a, b, c = positions[i + 1], positions[i + 2], positions[i + 3]

    if ref == 1:
        op_1(a, b, c)
    elif ref == 2:
        op_2(a, b, c)

    i += 4
