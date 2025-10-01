with open("ex5.txt") as exercise:
    data = exercise.readlines()

stack_1 = ["W", "P", "G", "Z", "V", "S", "B"]
stack_2 = ["F", "Z", "C", "B", "V", "J"]
stack_3 = ["C", "D", "Z", "N", "H", "M", "L", "V"]
stack_4 = ["B", "J", "F", "P", "Z", "M", "D", "L"]
stack_5 = ["H", "Q", "B", "J", "G", "C", "F", "V"]
stack_6 = ["B", "L", "S", "T", "Q", "F", "G"]
stack_7 = ["V", "Z", "C", "G", "L"]
stack_8 = ["G", "L", "N"]
stack_9 = ["C", "H", "F", "J"]

stacks = [
    stack_1,
    stack_2,
    stack_3,
    stack_4,
    stack_5,
    stack_6,
    stack_7,
    stack_8,
    stack_9,
]

instructions = [i.strip() for i in data[10:]]


def move(stacks, moved, origin, destination):
    moved_boxes = stacks[origin - 1][:moved]
    # print(moved_boxes)
    for elt in moved_boxes[::-1]:
        stacks[destination - 1].insert(0, elt)
    stacks[origin - 1] = stacks[origin - 1][moved:]
    return stacks


for line in instructions:
    line = line.split(" ")
    moved, origin, destination = int(line[1]), int(line[3]), int(line[5])
    stacks = move(stacks, moved, origin, destination)

for i in stacks:
    print(i[0], end="")

test_1 = ["N", "Z"]
test_2 = ["D", "C", "M"]
test_3 = ["P"]

tests = [test_1, test_2, test_3]

test_instructions = [[1, 2, 1], [3, 1, 3], [2, 2, 1], [1, 1, 2]]

for i in test_instructions:
    moved, origin, destination = i[0], i[1], i[2]
    tests = move(tests, moved, origin, destination)
