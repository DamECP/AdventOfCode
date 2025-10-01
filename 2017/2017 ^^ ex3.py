from math import sqrt
from collections import defaultdict

ref = 277678

# part1
"""
class Ring:
    def __init__(self, width):
        self.width = width
        self.lowest = self.get_lowest()
        self.highest = self.get_highest()
        self.digits = self.get_digits()

        self.tr_corner, self.tl_corner, self.bl_corner, self.br_corner = (
            self.get_corners()
        )

        self.right, self.up, self.left, self.down = self.get_middles()

        self.distances = self.get_distances()

    def get_highest(self):
        return self.width**2

    def get_lowest(self):
        if self.width >= 3:
            return (self.width - 2) ** 2 + 1
        return 1

    def get_digits(self):
        if self.width >= 3:
            return self.width**2 - (self.width - 2) ** 2
        return 1

    def get_corners(self):
        br_corner = self.highest
        tl_corner = (self.highest + self.lowest) // 2
        bl_corner = (self.highest + tl_corner) // 2
        tr_corner = (self.lowest + tl_corner) // 2

        return tr_corner, tl_corner, bl_corner, br_corner

    def get_middles(self):

        up = (self.tl_corner + self.tr_corner) // 2
        left = (self.bl_corner + self.tl_corner) // 2
        down = (self.bl_corner + self.br_corner) // 2
        right = (self.lowest + self.tr_corner) // 2

        return right, up, left, down

    def get_distances(self):
        distances = {}
        if self.width == 1:
            return f"Carré central"

        longest_path = self.width - 1
        shortest_path = self.width // 2

        distances[shortest_path] = []
        distances[longest_path] = []

        for middle in self.get_middles():
            distances[shortest_path].append(middle)

        for corner in self.get_corners():
            distances[longest_path].append(corner)

        return distances

    def data(self):
        return f"base : {self.width} | min : {self.lowest} | max : {self.highest} | chiffres : {self.digits} | coins : {self.get_corners()}"


i = 3
while True:
    r = Ring(i + 2)
    if r.highest >= ref:
        print(r.highest)
        print(r.get_distances())
        break
    i += 2

print(ref - 277466)
print(263 + 212)
"""

ref = 277678

# Part1
grid = defaultdict(int)
grid[(0, 0)] = 1


def get_spiral():

    def populate_grid(x, y):
        total = 0
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if not (dx, dy) == (0, 0):
                    total += grid[(x + dx, y + dy)]
        grid[(x, y)] = total

    x, y = 1, 0
    grid[(x, y)] = 1
    yield grid[(x, y)]

    while True:
        # go up
        while grid[(x - 1, y)]:
            y += 1
            populate_grid(x, y)
            yield grid[(x, y)]

        # go left
        while grid[(x, y - 1)]:
            x -= 1
            populate_grid(x, y)
            yield grid[(x, y)]

        # go down
        while grid[(x + 1, y)]:
            y -= 1
            populate_grid(x, y)
            yield grid[(x, y)]

        # go right
        while grid[(x, y + 1)]:
            x += 1
            populate_grid(x, y)
            yield grid[(x, y)]


for z in get_spiral():
    if z > ref:
        print(z)
        break
