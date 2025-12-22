with open("ex11.txt") as exercise:
    data = [i.strip() for i in exercise.readlines()]


class Octopus:
    def __init__(self, value, x, y):
        self.x = x
        self.y = y
        self.coords = (x, y)
        self.value = int(value)
        self.neighbors = []
        self.has_flashed = False

    def flashing(self):
        if self.value > 9 and self.has_flashed == False:
            self.has_flashed = True
            self.bounce()
            return True
        return False

    def bounce(self):
        for neighbor in self.neighbors:
            neighbor.value += 1


def build_collection():
    # build the collection
    octopuses = {
        (x, y): Octopus(char, x, y)
        for y, line in enumerate(data)
        for x, char in enumerate(line)
    }

    # update the collection with neighbors
    for (x, y), o in octopuses.items():
        o.neighbors = [
            octopuses[(nx, ny)]
            for nx in (x - 1, x, x + 1)
            for ny in (y - 1, y, y + 1)
            if (nx, ny) in octopuses and (nx, ny) != (x, y)
        ]
    return octopuses


def answer_1():
    octopuses = build_collection()

    counter = 0

    # increase by 1 each element
    for i in range(100):
        for o in octopuses.values():
            o.value += 1

        # spreading light
        progress = True
        while progress:
            progress = False
            for o in octopuses.values():
                if o.flashing():
                    progress = True

        # count the total of flashes and reset
        for o in octopuses.values():
            if o.has_flashed:
                counter += 1
                o.value = 0
                o.has_flashed = False

    return counter


# print(answer_1())


def answer_2():
    octopuses = build_collection()
    step = 0

    # increase by 1 each element
    while True:
        step += 1
        for o in octopuses.values():
            o.value += 1

        # spreading light
        progress = True
        while progress:
            progress = False
            for o in octopuses.values():
                if o.flashing():
                    progress = True

        if all(o.has_flashed for o in octopuses.values()):
            return step

        # count the total of flashes and reset
        for o in octopuses.values():
            if o.has_flashed:
                o.value = 0
                o.has_flashed = False


print(answer_2())
