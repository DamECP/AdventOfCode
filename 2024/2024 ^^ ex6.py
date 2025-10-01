with open("ex6.txt") as exercise:
    data = exercise.readlines()
    data = [i.strip() for i in data]

full_map = {}

for y, line in enumerate(data):
    for x, char in enumerate(line):
        full_map[(x, y)] = char


class Cursor:
    def __init__(self, x, y, full_map):
        self.x = x
        self.y = y
        self.full_map = full_map
        self.max_x = max(x for (x, y) in self.full_map.keys())
        self.max_y = max(y for (x, y) in self.full_map.keys())
        self.path = []
        self.position = 1
        self.finished = False
        self.count = 1

    def up(self):

        if (self.x, self.y - 1) not in self.full_map.keys():
            self.finished = True
        elif self.full_map[(self.x, self.y - 1)] != "#":
            self.y -= 1
            return True

    def down(self):
        if (self.x, self.y + 1) not in self.full_map.keys():
            self.finished = True

        elif self.full_map[(self.x, self.y + 1)] != "#":
            self.y += 1
            return True

    def right(self):
        if (self.x + 1, self.y) not in self.full_map.keys():
            self.finished = True

        elif self.full_map[(self.x + 1, self.y)] != "#":
            self.x += 1
            return True

    def left(self):

        if (self.x - 1, self.y) not in self.full_map.keys():
            self.finished = True

        elif self.full_map[(self.x - 1, self.y)] != "#":
            self.x -= 1
            return True

    def walk(self):
        self.path.append((self.x, self.y))

        while not self.finished:
            self.count += 1
            # print(self.x, self.y)
            if full_map[(self.x, self.y)] != "#":
                moved = False
                if self.position % 4 == 1:
                    if self.up():
                        moved = True
                    else:
                        self.position += 1

                elif self.position % 4 == 2:
                    if self.right():
                        moved = True
                    else:
                        self.position += 1

                elif self.position % 4 == 3:
                    if self.down():
                        moved = True
                    else:
                        self.position += 1

                elif self.position % 4 == 0:
                    if self.left():
                        moved = True

                    else:
                        self.position += 1

                if moved:
                    self.path.append((self.x, self.y))

                if (
                    self.x < 0
                    or self.x > self.max_x
                    or self.y < 0
                    or self.y > self.max_y
                ):
                    # print("sortie")
                    self.finished = True

                if self.count == self.max_x * self.max_y:
                    # print("boucle max", self.count)
                    self.finished = True

            else:
                self.position += 1

        # print(len(set(self.path)))


for key, value in full_map.items():
    if value == "^":
        cursor = Cursor(key[0], key[1], full_map)
        break

x, y = cursor.x, cursor.y

countdown = cursor.max_x * cursor.max_y
counter = 0

for key, value in full_map.items():
    countdown -= 1
    print("countdown", countdown)
    if value == ".":
        full_map[key] = "#"
        cursor = Cursor(x, y, full_map)
        cursor.walk()
        if cursor.count == cursor.max_x * cursor.max_y:
            counter += 1
        full_map[key] = "."

print()
print(counter)
