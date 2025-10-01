from itertools import cycle

with open("ex3.txt") as exercise:
    data = exercise.readlines()
    data = [i.replace("\n", "") for i in data]


n = 0
x = 0

for y, line in enumerate(data):
    if y % 2 == 0:
        line_cycle = cycle(line)

        for _ in range(x):
            next(line_cycle)

        tree_or_ok = next(line_cycle)
        print(f"ligne : {y} | symbole {tree_or_ok} | x : {x}")

        if tree_or_ok == "#":
            n += 1
        x += 1

print(n)

results = [63, 254, 62, 56, 30]

total = 1

for i in results:
    total *= i

print(total)
