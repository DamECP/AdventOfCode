from collections import defaultdict, Counter

# Part1
"""
class Space:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.used_spaces = set()
        self.double = set()
        self.data = defaultdict(int)
        self.counter = 0

    def use(self, x_diff, y_diff, width, height):

        self.counter += 1

        for x in range(x_diff, x_diff + width):
            for y in range(y_diff, y_diff + height):
                self.data[(x, y)] += 1
                if (x, y) not in self.used_spaces:
                    self.used_spaces.add((x, y))
                else:
                    self.double.add((x, y))


fabric = Space(1000, 1000)

with open("ex3.txt") as exercise:
    for line in exercise:
        line = line.replace("\n", "")
        line = line.split(" ")
        coordinates = line[2].split(",")
        size = line[3].split("x")
        x_diff = int(coordinates[0])
        y_diff = int(coordinates[1].removesuffix(":"))
        width = int(size[0])
        height = int(size[1])
        fabric.use(x_diff, y_diff, width, height)

"""


class Rectangle:
    def __init__(self, number, startx, starty, width, height):
        self.number = number
        self.startx = startx
        self.starty = starty
        self.width = width
        self.height = height
        self.coords = []

    def coordinates(self):
        for x in range(self.startx, self.width + self.startx):
            for y in range(self.starty, self.height + self.starty):
                self.coords.append((x, y))
        return self.coords


rectangles = []
all_coords = []

with open("ex3.txt") as exercise:
    for line in exercise:
        line = line.strip().replace("\n", "").split(" ")
        number, startingpoints, dimensions = (
            line[0],
            line[2].split(","),
            line[3].split("x"),
        )
        startx, starty = int(startingpoints[0]), int(startingpoints[1][:-1])
        width, height = int(dimensions[0]), int(dimensions[1])

        r = Rectangle(number, startx, starty, width, height)
        rectangles.append(r)
        all_coords.extend(r.coordinates())


counts = Counter(all_coords)

unique_values = [key for key, value in counts.items() if value == 1]

x = 0
for rect in rectangles:
    if all(item in set(unique_values) for item in set(rect.coordinates())):
        print(rect.number)
        break
    print(x)
    x += 1
