from __future__ import annotations
from collections import defaultdict
from itertools import combinations

with open("ex8.txt") as test:
    data = [i.strip() for i in test.readlines()]

width = len(data[0])
height = len(data)


class Antenna:
    def __init__(self, frequency, x, y):
        self.frequency = frequency
        self.x = x
        self.y = y
        self.antinodes = None

    def position(self):
        return (self.x, self.y)

    def antinode(self, opposite: Antenna):

        x1, y1 = self.position()
        x2, y2 = opposite.position()

        dx = x2 - x1
        dy = y2 - y1

        before_A = (x1 - dx, y1 - dy)
        after_B = (x2 + dx, y2 + dy)

        return [before_A, after_B]

    def resonnance(self, opposite: Antenna, width, height):

        all_resonnances = []
        x1, y1 = self.position()
        x2, y2 = opposite.position()

        print(self.position(), opposite.position())

        stepx = x2 - x1
        stepy = y2 - y1

        x, y = x1 - stepx, y1 - stepy
        while 0 <= x < width and 0 <= y < height:
            print(x, y)
            all_resonnances.append((x, y))
            x -= stepx
            y -= stepy

        x, y = x2 + stepx, y2 + stepy
        while 0 <= x < width and 0 <= y < height:
            all_resonnances.append((x, y))
            print(x, y)
            x += stepx
            y += stepy

        return all_resonnances


antennas = defaultdict(list)
for y, line in enumerate(data):
    for x, char in enumerate(line):
        if char != ".":
            ant = Antenna(char, x, y)
            antennas[char].append(ant)

antinodes = []
resonnances = []
added_ant = []
for key, value in antennas.items():
    list_ant = [i.position() for i in value]
    added_ant.extend(list_ant)
    for ant_1, ant_2 in combinations(value, 2):
        antinodes.extend(ant_1.antinode(ant_2))
        resonnances.extend(ant_1.resonnance(ant_2, width, height))


answer_1 = len(set([i for i in antinodes if 0 <= i[0] < width and 0 <= i[1] < height]))
answer_2 = len(set([r for r in resonnances] + [i for i in added_ant]))
print(added_ant)
print(answer_2)
