from collections import deque


class Grid:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.grid = [["." for _ in range(self.width)] for _ in range(self.height)]

    def __repr__(self):
        return "\n".join("".join(row) for row in self.grid)

    def select(self, x, y):
        for i in range(y):
            for j in range(x):
                self.grid[i][j] = "#"
        return self.grid

    def rotate_row(self, y, by):
        row = deque(self.grid[y])
        row.rotate(by)
        self.grid[y] = list(row)
        return self.grid

    def rotate_column(self, x, by):
        column = deque([line[x] for line in self.grid])
        column.rotate(by)
        for i in range(len(self.grid)):
            self.grid[i][x] = column[i]
        return self.grid

    def count(self):
        counter = 0
        for line in self.grid:
            counter += line.count("#")
        return counter


with open("ex8.txt") as exercise:
    g = Grid(50, 6)

    for line in exercise:
        line = line.replace("\n", "")
        instr = line.split(" ")

        if instr[0] == "rect":
            dimensions = instr[1].split("x")
            x, y = int(dimensions[0]), int(dimensions[-1])
            g.select(x, y)

        elif instr[1] == "row":
            y = int((instr[2].split("="))[-1])
            by = int(instr[-1])
            g.rotate_row(y, by)

        elif instr[1] == "column":
            x = int((instr[2].split("="))[-1])
            by = int(instr[-1])
            g.rotate_column(x, by)


print(g.count())

print(g)
