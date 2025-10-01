reports = []
valid_levels = []
invalid_levels = []
definitely_invalid = []


def increase_or_decrease(level: list):

    if level == sorted(level) or level == sorted(level, reverse=True):
        return True


def adjacent_levels(level: list):
    level = sorted(level)
    for i in range(len(level) - 1):
        if level[i + 1] - level[i] not in range(1, 4):
            return False
    return True


test_data = [
    [7, 6, 4, 2, 1],
    [1, 2, 7, 8, 9],
    [9, 7, 6, 2, 1],
    [1, 3, 2, 4, 5],
    [8, 6, 4, 4, 1],
    [1, 3, 6, 7, 9],
]

counter = 0
with open("ex2.txt") as exo:
    total = 0
    for line in exo:
        line = line.replace("\n", "")
        data = line.split()
        data = [int(nb) for nb in data]
        if increase_or_decrease(data) and adjacent_levels(data):
            counter += 1
        else:
            for i in range(len(data)):
                new_list = data[:i] + data[i + 1 :]
                if increase_or_decrease(new_list) and adjacent_levels(new_list):
                    counter += 1
                    break


"""
for data in test_data:
    if increase_or_decrease(data) and adjacent_levels(data):
        counter += 1
        print(data)
    else:
        for elt in data:
            new_list = data[:]
            slicing = new_list.index(elt)
            new_list = new_list[:slicing] + new_list[slicing + 1 :]
            if increase_or_decrease(new_list) and adjacent_levels(new_list):
                counter += 1
                print(data, new_list)
                break
"""


print(counter)
