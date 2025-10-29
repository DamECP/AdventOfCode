import math


class Tree:
    def __init__(self, height, x, y):
        self.height = height
        self.x = x
        self.y = y
        self.row = None
        self.col = None
        self.viewing_distance = 0
        self.left = None
        self.right = None
        self.up = None
        self.down = None

    def isvisible(self, rows, cols):
        visible = False

        self.row = rows[self.y]
        self.col = cols[self.x]

        up = [i.height for i in self.col if i.y < self.y]
        self.up = up[::-1]
        if not up or self.height > max(up):
            visible = True

        left = [i.height for i in self.row if i.x < self.x]
        self.left = left[::-1]
        if not left or self.height > max(left):
            visible = True

        right = [i.height for i in self.row if i.x > self.x]
        self.right = right
        if not right or self.height > max(right):
            visible = True

        down = [i.height for i in self.col if i.y > self.y]
        self.down = down
        if not down or self.height > max(down):
            visible = True

        return visible

    def next_trees(self, direction):

        total = 0
        ref = self.height
        for height in direction:
            if height < ref:
                total += 1
            elif height >= ref:
                total += 1
                break

        return total

    def around(self, rows, cols):

        total = []

        directions = [self.up, self.left, self.down, self.right]

        if self.isvisible(rows, cols):
            for direction in directions:
                visible_trees = self.next_trees(direction)
                total.append(visible_trees)

        return total


with open("ex8.txt") as exercise:
    data = [i.strip() for i in exercise]


rows = {}
cols = {}
forest = []

for y, line in enumerate(data):
    for x, height in enumerate(line):
        h = int(height)
        t = Tree(h, x, y)
        rows.setdefault(y, []).append(t)
        cols.setdefault(x, []).append(t)
        forest.append(t)

for y in rows:
    rows[y].sort(key=lambda t: t.x)
for x in cols:
    cols[x].sort(key=lambda t: t.y)


visible_trees = [i for i in forest if i.isvisible(rows, cols)]
answer_1 = len(visible_trees)

highest = 0
for tree in visible_trees:
    numbers = tree.around(rows, cols)
    total = math.prod(numbers)
    if total > highest:
        highest = total

print(highest)
