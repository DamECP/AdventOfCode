with open("ex5.txt") as exercise:
    data = [i.strip() for i in exercise]


def difference(start: int, finish):
    difference = finish - start
    value = difference // 2
    return value


def row(instructions):
    start = 0
    finish = 127
    for i in instructions[:-1]:
        value = difference(start, finish)
        if i == "F":
            finish -= value + 1
        elif i == "B":
            start += value + 1
    if instructions[-1] == "F":
        return start
    return finish


def column(instructions):
    start = 0
    finish = 7
    for i in instructions[:-1]:
        value = difference(start, finish)
        if i == "L":
            finish -= value + 1
        elif i == "R":
            start += value + 1
    if instructions[-1] == "L":
        return start
    return finish


all_seats = []
for d in data:
    d_row = row(d[:7])
    d_col = column(d[-3:])
    seat_id = d_row * 8 + d_col
    all_seats.append(seat_id)

# answer1
print(max(all_seats))


# answer2
myseat = set(range(min(all_seats), max(all_seats))) - set(all_seats)
print(myseat)
