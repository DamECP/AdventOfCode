instructions = []
with open("ex2.txt") as exercise:
    for line in exercise:
        line = line.replace("\n", "")
        instructions.append(line)


test = ["ULL", "RRDDD", "LURDL", "UUUUD"]


def walk(instructions: list):
    start = 5
    for i in instructions:
        for instruction in i:
            if instruction == "U":
                if start - 3 >= 1:
                    start -= 3
            elif instruction == "D":
                if start + 3 <= 9:
                    start += 3
            elif instruction == "L" and start not in [1, 4, 7]:
                start -= 1
            elif instruction == "R" and start not in [3, 6, 9]:
                start += 1

        print(start)


# walk(instructions)

map_ = ["   1   ", "  234  ", " 56789 ", "  ABC  ", "   D   "]

mapped_data = {}

for i, line in enumerate(map_):
    for j, char in enumerate(line):
        mapped_data[(i, j)] = line[j]

print(mapped_data)

start = (2, 1)
for instruction in instructions:
    for i in instruction:
        new_position = start
        if i == "U" and (start[0] - 1, start[1]) in mapped_data.keys():
            new_position = (start[0] - 1, start[1])
        elif i == "D" and (start[0] + 1, start[1]) in mapped_data.keys():
            new_position = (start[0] + 1, start[1])
        elif i == "R" and (start[0], start[1] + 1) in mapped_data.keys():
            new_position = (start[0], start[1] + 1)
        elif i == "L" and (start[0], start[1] - 1) in mapped_data.keys():
            new_position = (start[0], start[1] - 1)

        if mapped_data[new_position] != " ":
            start = new_position

    print(mapped_data[start])
