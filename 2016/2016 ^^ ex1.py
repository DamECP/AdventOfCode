with open("ex1.txt") as exercise:
    for line in exercise:
        line = line.replace("\n", "")
        moveset = line.split(", ")


class Santa:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.direction = "N"

    def north(self, n):
        self.direction = "N"
        self.y += n
        return self.y

    def south(self, n):
        self.direction = "S"
        self.y -= n
        return self.y

    def east(self, n):
        self.direction = "E"
        self.x += n
        return self.x

    def west(self, n):
        self.direction = "W"
        self.x -= n
        return self.x

    def position(self):
        return self.x, self.y


test = ["R8", "R4", "R4", "R8"]

santa = Santa()
visited_places = set()

for i in moveset:
    path = int(i[1:])
    turn = i[0]
    previous_position = santa.position()
    if santa.direction == "N":
        if turn == "L":
            santa.west(path)
        elif turn == "R":
            santa.east(path)
    elif santa.direction == "E":
        if turn == "L":
            santa.north(path)
        elif turn == "R":
            santa.south(path)
    elif santa.direction == "S":
        if turn == "L":
            santa.east(path)
        elif turn == "R":
            santa.west(path)
    elif santa.direction == "W":
        if turn == "L":
            santa.south(path)
        elif turn == "R":
            santa.north(path)

    prev_x = previous_position[0]
    prev_y = previous_position[1]
    santa_x = santa.position()[0]
    santa_y = santa.position()[1]

    if prev_x > santa_x:
        for i in range(prev_x - 1, santa_x - 1, -1):
            intermediate_position = (i, prev_y)
            # print(intermediate_position)
            if intermediate_position in visited_places:
                print(intermediate_position)
                break
            else:
                visited_places.add(intermediate_position)

    if prev_x < santa_x:
        for i in range(prev_x + 1, santa_x + 1):
            intermediate_position = (i, prev_y)
            # print(intermediate_position)
            if intermediate_position in visited_places:
                print(intermediate_position)
                break
            else:
                visited_places.add(intermediate_position)

    if prev_y > santa_y:
        print("changement en Y")
        for i in range(prev_y - 1, santa_y - 1, -1):
            intermediate_position = (prev_x, i)
            # print(intermediate_position)
            if intermediate_position in visited_places:
                print(intermediate_position)
                break
            else:
                visited_places.add(intermediate_position)

    if prev_y < santa_y:
        print("changement en y")
        for i in range(prev_y + 1, santa_y + 1):
            intermediate_position = (prev_x, i)
            # print(intermediate_position)
            if intermediate_position in visited_places:
                print(intermediate_position)
                break
            else:
                visited_places.add(intermediate_position)
