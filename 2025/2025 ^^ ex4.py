with open("ex4.txt") as exercise:
    data = [i.strip() for i in exercise.readlines()]


positions = {(x, y): char for y, line in enumerate(data) for x, char in enumerate(line)}
max_x = len(data[0])
max_y = len(data)


def four_around(pos: tuple) -> list:
    x, y = pos
    around = []
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0:
                continue
            new_x, new_y = x + i, y + j
            if 0 <= new_x < max_x and 0 <= new_y < max_y:
                around.append(positions[(new_x, new_y)])
    return len([i for i in around if i == "@"]) < 4


def answer_1():
    answer = 0
    for key, value in positions.items():
        if value == "@" and four_around(key):
            answer += 1
    return answer


def answer_2():
    answer = 0
    progress = True

    while progress:
        progress = False
        for key, value in positions.items():
            if value == "@" and four_around(key):
                answer += 1
                positions[key] = "."
                progress = True
    return answer


print(answer_1())
print(answer_2())
