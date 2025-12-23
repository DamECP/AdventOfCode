from itertools import combinations
import numpy as np
from math import prod

with open("ex8.txt") as exercise:
    data = [
        tuple(int(n) for n in line.strip().split(",")) for line in exercise.readlines()
    ]


class Box:
    def __init__(self, x, y, z):
        self.array = np.array([x, y, z])
        self.closest = None
        self.distance = None


boxes = [Box(x, y, z) for x, y, z in data]

# gathers closest pairs and their distance as tuples
pairs = [
    (n1, n2, np.linalg.norm(n1.array - n2.array)) for n1, n2 in combinations(boxes, 2)
]

# sort them by distance
pairs.sort(key=lambda b: b[2])


def answer_1():
    shortest_pairs = pairs[:1000]

    circuits = []

    for b1, b2, dist in shortest_pairs:
        # checks if one of the values is in a circuit already
        overlap = [c for c in circuits if b1 in c or b2 in c]

        # if not, build its own one
        if not overlap:
            circuits.append(set([b1, b2]))

        # or merge b1, b2 and the current circuit
        else:
            merged = set([b1, b2])
            for c in overlap:
                merged |= c
                circuits.remove(c)
            circuits.append(merged)

    # get the 3 largest circuits
    sizes = sorted([len(c) for c in circuits], reverse=True)[:3]

    return prod(sizes)


print(answer_1())


def answer_2():
    circuits = []

    for b1, b2, dist in pairs:
        overlap = [c for c in circuits if b1 in c or b2 in c]

        if not overlap:
            circuits.append(set([b1, b2]))

        else:
            merged = set([b1, b2])
            for c in overlap:
                merged |= c
                circuits.remove(c)
            circuits.append(merged)

        # stops when there is only one huge circuit
        if len(circuits) == 1 and len(circuits[0]) == len(boxes):
            return b1.array[0] * b2.array[0]


print(answer_2())
