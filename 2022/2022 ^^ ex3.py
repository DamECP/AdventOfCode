import string

values = {}
for i, char in enumerate(string.ascii_lowercase, 1):
    values[char] = i
for i, char in enumerate(string.ascii_uppercase, 27):
    values[char] = i

# part 1
"""
with open("ex3.txt") as exercise:
    result = 0
    group_line = 0
    for line in exercise:
        line = line.replace("\n", "")
        item1, item2 = line[0 : (len(line) // 2)], line[(len(line) // 2) :]
        double = set(item1) & set(item2)
        double = list(double)[0]
        result += values[double]

print(result)
"""

with open("ex3.txt") as exercise:
    result = 0
    trios = []
    for line in exercise:
        line = line.replace("\n", "")
        trios.append(line)
        if len(trios) == 3:
            item1, item2, item3 = trios[0], trios[1], trios[2]
            unique = set(item1) & set(item2) & set(item3)
            unique = list(unique)[0]
            result += values[unique]
            trios = []


print(result)
