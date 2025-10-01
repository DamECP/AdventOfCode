class Cell:
    def __init__(self, value: int, y: int, x: int):
        self.value = value
        self.x = x
        self.y = y
        self.coords = (x, y)
        self.neighbors = []

    def find_neighbors(self, all_cells: list):
        neighbors = []
        up = self.y - 1
        down = self.y + 1
        left = self.x - 1
        right = self.x + 1
        for cell in all_cells:
            if cell.coords in [
                (self.x, up),
                (self.x, down),
                (left, self.y),
                (right, self.y),
            ]:
                self.neighbors.append(cell)

    def __hash__(self):
        return hash(self.coords)

    def __eq__(self, other):
        return isinstance(other, Cell) and self.coords == other.coords


with open("ex9.txt") as exercise:
    grid: list[Cell] = []
    for y, line in enumerate(exercise):
        line = line.replace("\n", "")

        for x, value in enumerate(line):
            c = Cell(int(value), x, y)
            grid.append(c)


lowest_points = []
for c in grid:

    c.find_neighbors(grid)
    values_around = [cell.value for cell in c.neighbors]
    if all(v > c.value for v in values_around):
        lowest_points.append(c)

# part1 = sum(lowest_points) + len(lowest_points)
# print(part1)

all_basins_sizes = []


def build_basin(c: Cell, visited: set[Cell] | None = None):
    if visited is None:
        visited = set()
    visited.add(c)

    for neigh in c.neighbors:
        if neigh.value == 9:
            continue
        if neigh.value > c.value and neigh not in visited:
            build_basin(neigh, visited)

    return visited


basin_lengths = []
for cell in lowest_points:
    basin = build_basin(cell)
    basin_lengths.append(len([i.value for i in basin]))


last_three = sorted(basin_lengths, reverse=True)[0:3]

print(last_three)

result = 1
for i in last_three:
    result *= i

print(result)
