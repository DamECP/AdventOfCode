import string

with open("ex3.txt") as exercise:
    data = exercise.readlines()
    triangles = [sorted(map(int, i.strip().split())) for i in data]

row_1, row_2, row_3 = [], [], []
for line in data:
    line = line.strip().split(" ")
    line = [int(i) for i in line if i != ""]
    row_1.append(line[0])
    row_2.append(line[1])
    row_3.append(line[2])

rows = [row_1, row_2, row_3]


def validate_triangle(measures: list):
    return (measures[0] + measures[1]) > measures[2]


# for triangle in triangles:
#    if validate_triangle(triangle):
#        counter += 1

counter = 0
for row in rows:
    row = [row[i : i + 3] for i in range(0, len(row), 3)]
    for i in row:
        if validate_triangle(sorted(i)):
            counter += 1

print(counter)
