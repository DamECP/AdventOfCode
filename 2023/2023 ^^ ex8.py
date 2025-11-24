import numpy

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

test_moves = "LR"
test_dataset = {
    "11A": ["11B", "XXX"],
    "11B": ["XXX", "11Z"],
    "11Z": ["11B", "XXX"],
    "22A": ["22B", "XXX"],
    "22B": ["22C", "22C"],
    "22C": ["22Z", "22Z"],
    "22Z": ["22B", "22B"],
    "XXX": ["XXX", "XXX"],
}


def part_2():
    part_2 = [k for k in dataset.keys() if k.endswith("A")]

    multipliers = []
    for i in part_2:
        counter = 0

        not_found = True

        while not_found:
            for char in moves:
                counter += 1
                if char == "L":
                    i = dataset[i][0]
                else:
                    i = dataset[i][1]

                if i.endswith("Z"):
                    multipliers.append(counter)
                    not_found = False

    return multipliers


arr = numpy.array(part_2())
answer_2 = numpy.lcm.reduce(arr)

print(answer_2)


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
