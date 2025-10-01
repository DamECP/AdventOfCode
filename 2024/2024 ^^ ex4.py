import os

os.chdir(r"C:\Users\damie\Documents\Code\Adventcode\2024")

test = []  # crée la matrice
with open("ex4.txt") as a:
    for line in a:
        line = line.replace("\n", "")
        test.append(line)


def counting(lines: list):
    xmas = 0
    samx = 0
    total = []
    for line in lines:
        # print(line)
        # print(f"XMAs : {line.count('XMAS')}")
        xmas += line.count("MAS")
        # print(f"SAMX : {line.count('SAMX')}")
        samx += line.count("SAM")
        # print()
    return samx + xmas


def vertical(test):
    vertical_test = []
    n = 0
    while n < len(test[0]):
        newline = ""
        for line in test:
            newline += line[n]
        vertical_test.append(newline)

        n += 1
    return vertical_test


def diagonal(test: list):
    new_matrixGD = []
    new_matrixDG = []
    max_len = (len(test[0]) * 2) - 1
    for i, line in enumerate(test):
        line = i * "-" + line + "-" * (max_len - i - len(line))
        new_matrixGD.append(line)
    for i, line in enumerate(test):
        line = "-" * (max_len - i - len(line)) + line + i * "-"
        new_matrixDG.append(line)

    diag1 = vertical(new_matrixGD)
    diag2 = vertical(new_matrixDG)

    diagonals = diag1 + diag2
    return diagonals


# print(counting(diagonal(test)))

grid = {}
for y, line in enumerate(test):
    for x, char in enumerate(line):
        grid[(x, y)] = char


def cross_finder(x, y):

    tl, bl, tr, br = (x - 1, y - 1), (x - 1, y + 1), (x + 1, y - 1), (x + 1, y + 1)

    if all(position in grid for position in [tl, tr, bl, br]):

        if (grid[tl] == "M" and grid[br] == "S") or (
            grid[tl] == "S" and grid[br] == "M"
        ):
            if (grid[tr] == "M" and grid[bl] == "S") or (
                (grid[tr] == "S" and grid[bl] == "M")
            ):
                return True

    return False


counter = 0
for key, value in grid.items():
    if value == "A":
        if 0 < key[1] < len(test) and 0 < key[0] < len(test[0]):
            if cross_finder(key[0], key[1]):
                counter += 1

print(counter)
