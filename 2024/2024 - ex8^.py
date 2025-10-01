from itertools import combinations

with open("ex8test.txt") as test:
    data = test.readlines()
    data = [i.strip() for i in data]
    max_x = len(data[0])
    max_y = len(data)

print(max_x)
print(max_y)


dico = {}
antennas_list = set()


def part2(char1, char2):  # part 2
    x1, y1 = char1[0], char1[1]
    x2, y2 = char2[0], char2[1]

    delta_y = abs(y1 - y2)
    delta_x = abs(x1 - x2)

    start_y = max(y1, y2) % delta_y
    ys = [
        i for i in range(start_y, max_y) if i % delta_y == start_y
    ]  # tous les y valables

    start_x = max(x1, x2) % delta_x
    xs = [
        i for i in range(start_x, max_x) if i % delta_x == start_x
    ]  # tous les x valables

    print(char1, char2)
    print(xs, ys)

    # Il s'agit de trouver tous les points qui sont alignés et plus uniqument
    # ceux qui sont des symétriques avec un écart de delta
    # ex : A = (2, 5) et A' = (4, 9)
    # part 1 = up (0, 1) et down = (6, 14) car deltas de 2 et 4
    # part 2 = ups = [(0, 1)] car limité par 0 et downs = [(6, 14), (8, 18), (11, 22)...]

    # reste à associer les x et y dans les listes qui correspodent aux alignements


def antenna(char1, char2):  # part 1
    x1, y1 = char1[0], char1[1]
    x2, y2 = char2[0], char2[1]

    delta_y = abs(y1 - y2)
    up_y = y1 - delta_y
    down_y = y2 + delta_y

    delta_x = abs(x1 - x2)
    if x1 < x2:
        up_x = x1 - delta_x
        down_x = x2 + delta_x
    elif x1 > x2:
        up_x = x1 + delta_x
        down_x = x2 - delta_x
    else:
        up_x = down_x = x1
    # print("up : ", (up_x, up_y), "down : ", (down_x, down_y))
    return (up_x, up_y), (down_x, down_y)


for y, line in enumerate(data):
    for x, char in enumerate(line):
        if char == "." or char == "#":
            continue
        elif char not in dico:
            dico[char] = [(x, y)]
        else:
            dico[char].append((x, y))

for key, values in dico.items():
    # print(key, values)
    for a, b in combinations(values, 2):
        anta, antb = antenna(a, b)
        # print(anta, antb)
        antennas_list.add(anta)
        antennas_list.add(antb)
        part2(a, b)
part1_list = [i for i in antennas_list if 0 <= i[0] <= max_x and 0 <= i[1] <= max_y]

# print(len(part1_list))
