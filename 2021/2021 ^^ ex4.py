data = []

with open("ex4.txt") as exercise:
    numbers = []
    for line in exercise:
        line = line.replace("\n", "")
        numbers.append(line)
        if line == "":
            data.append(numbers)
            numbers = []

numbers_called = [int(i) for i in data[0][0].split(",")]


class Grid:
    def __init__(self, grid_list: list):
        self.lines = grid_list
        self.columns = [list(column) for column in zip(*grid_list)]
        self.win = False

    def __repr__(self):
        grid_repr = "Grid(\n"
        grid_repr += "  Lignes:\n"
        for line in self.lines:
            grid_repr += f"  {line}\n"

        grid_repr += "  Colonnes:\n"
        for column in self.columns:
            grid_repr += f"  {column}\n"

        grid_repr += ")"
        return grid_repr

    def number_picked(self, number):
        for line in self.lines:
            for i in range(len(line)):
                if line[i] == number:
                    line[i] = 0
        for column in self.columns:
            for i in range(len(column)):
                if column[i] == number:
                    column[i] = 0

    def bingo(self):
        for line in self.lines:
            if sum(line) == 0:
                print("bingo")
                return True

        for column in self.columns:
            if sum(column) == 0:
                print("bingo")
                return True

        return False


grids = []

for content in data[1:-1]:
    content = content[:-1]
    for i, line in enumerate(content):
        content[i] = [int(j) for j in line.split(" ") if j != ""]
    grid = Grid(content)
    grids.append(grid)

bingo_found = False

for i in numbers_called:
    for j in grids:
        if j.win == False:
            j.number_picked(i)
            if j.bingo():
                print(i)
                print(j)
                print(sum(sum(line) for line in j.lines) * i)
                j.win = True
