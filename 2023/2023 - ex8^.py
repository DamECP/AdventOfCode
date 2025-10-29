dataset = {}
with open("ex8.txt") as exercise:
    lines = exercise.readlines()
    moves = lines[0].strip()
    for line in lines[2:]:
        line = line.replace("\n", "")
        node, references = line.split(" = ")
        references = references.split(",")
        references[0] = references[0][1:].strip()
        references[1] = references[1][:-1].strip()
        dataset[node] = references


def part_2():
    part_2 = [i for i in dataset.keys() if i.endswith("A")]
    counter = 0
    repeat = True


part_2()


def part_1():
    start = "AAA"
    end = "ZZZ"
    counter = 0
    repeat = True
    while repeat:
        for move in moves:

            if move == "L":
                next_step = dataset.get(start)[0]
            elif move == "R":
                next_step = dataset.get(start)[1]

            counter += 1
            if next_step == end:
                repeat = False
                break

            start = next_step
    print(counter)
