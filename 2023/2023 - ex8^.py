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

print(moves)
print(dataset)

start = "AAA"
end = "ZZZ"

counter = 0
repeat = True

while repeat:
    for move in moves:
        print(move)
        if move == "L":
            next_step = dataset.get(start)[0]
        elif move == "R":
            next_step = dataset.get(start)[1]

        print(next_step)
        counter += 1
        if next_step == end:
            repeat = False
            break

        start = next_step


print(counter)
