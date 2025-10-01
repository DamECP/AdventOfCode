# part 1
"""
with open("ex1.txt") as exercise:
    start = 134
    counter = 0
    for line in exercise:
        line = line.replace("\n", "")
        line = int(line)
        if line > start:
            counter += 1
            print("alerte")
        print(line)
        start = line

print(counter)
"""

with open("ex1.txt") as exercise:
    data = exercise.read()
    data = data.split("\n")
    data = [i for i in data if i != ""]

list_n = [data[i : i + 3] for i, elt in enumerate(data)]


start = 0
total = 0
for i in list_n:
    if len(i) == 3:
        print(i)
        depth = sum([int(n) for n in i])
        print(depth)
        if depth > start:
            total += 1
            print(+1)
        start = depth
        print()

print(total - 1)
