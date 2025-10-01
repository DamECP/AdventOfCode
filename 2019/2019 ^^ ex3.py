with open("ex3.txt") as exercise:
    data = exercise.readlines()
    data_1, data_2 = (line.strip().split(",") for line in data[:2])


def move(array: list):
    coordinates = {}
    x, y = 0, 0
    z = 0
    for i in array:

        direction = i[0]
        steps = int(i[1:])

        if direction == "R":
            for _ in range(steps):
                x += 1
                z += 1
                coordinates[z] = (x, y)
        elif direction == "D":
            for _ in range(steps):
                y -= 1
                z += 1
                coordinates[z] = (x, y)
        elif direction == "L":
            for _ in range(steps):
                x -= 1
                z += 1
                coordinates[z] = (x, y)
        elif direction == "U":
            for _ in range(steps):
                y += 1
                z += 1
                coordinates[z] = (x, y)

    return coordinates


path_1 = list(move(data_1).values())
path_2 = list(move(data_2).values())

commons = set(path_1) & set(path_2)

result = float("inf")

fewest_combinations = float("inf")


for elt in commons:

    path_1_steps = next(k for k, v in move(data_1).items() if v == elt)
    # print(path_1_steps)
    path_2_steps = next(k for k, v in move(data_2).items() if v == elt)
    # print(path_2_steps)

    # print(elt)
    combination = path_1_steps + path_2_steps
    if combination < fewest_combinations:
        fewest_combinations = combination

    elt = abs(sum(elt))
    if elt < result:
        result = elt

print(fewest_combinations)
