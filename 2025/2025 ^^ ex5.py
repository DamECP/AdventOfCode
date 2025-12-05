with open("ex5.txt") as exercise:
    data = [i.strip() for i in exercise.readlines()]

ranges = [
    range(int(a), int(b)) for line in data if "-" in line for a, b in [line.split("-")]
]
ids = [int(i) for i in data if i.isdigit()]


def answer_1():
    answer_1 = len([i for i in ids if any(i in r for r in ranges)])
    return answer_1


starts = sorted([r.start for r in ranges])
stops = sorted([r.stop for r in ranges])


def answer_2():
    new_ranges = []
    starter = starts[0]

    for i, j in zip(stops, starts[1:]):
        if i < j:
            new_ranges.append(range(starter, i))
            starter = j
    new_ranges.append(range(starter, stops[-1]))

    total = sum(len(r) + 1 for r in new_ranges)
    return total


print(answer_1())
print(answer_2())
