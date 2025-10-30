from __future__ import annotations


class Rope:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.positions = []

    def up(self):
        self.y += 1
        self.add_position()

    def down(self):
        self.y -= 1
        self.add_position()

    def right(self):
        self.x += 1
        self.add_position()

    def left(self):
        self.x -= 1
        self.add_position()

    @property
    def current(self):
        return (self.x, self.y)

    def follow(self, leader: Rope):

        diagonal = leader.x != self.x and leader.y != self.y

        delta = abs(leader.x - self.x) > 1 or abs(leader.y - self.y) > 1

        if not delta or self.current == leader.current:
            return

        elif delta and not diagonal:
            if leader.x > self.x:
                self.x += 1
            if leader.x < self.x:
                self.x -= 1
            if leader.y > self.y:
                self.y += 1
            if leader.y < self.y:
                self.y -= 1

        else:
            if leader.x > self.x:
                self.x += 1
            elif leader.x < self.x:
                self.x -= 1
            if leader.y > self.y:
                self.y += 1
            elif leader.y < self.y:
                self.y -= 1

        self.add_position()

    def add_position(self):
        self.positions.append(self.current)


with open("ex9.txt") as exercise:
    data = [line.strip() for line in exercise]

# initial position
x, y = 0, 0
h = Rope(x, y)
h.add_position()
t = Rope(x, y)
t.add_position()


rope = [Rope(0, 0) for _ in range(10)]

moves = {
    "U": lambda r: r.up(),
    "D": lambda r: r.down(),
    "L": lambda r: r.left(),
    "R": lambda r: r.right(),
}


for instruction in data:
    direction, steps = instruction.split(" ")

    for _ in range(int(steps)):

        # head moves
        moves[direction](rope[0])

        for i in range(1, 10):
            rope[i].follow(rope[i - 1])


answer_1 = len(set(rope[1].positions)) + 1  # start position
answer_2 = len(set(rope[9].positions)) + 1
