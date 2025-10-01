import string
import jellyfish
import difflib

# part1

"""
list_codes = []
with open("ex2.txt") as exercise:
    counter1 = 0
    counter2 = 0    
    for line in exercise:
        line = line.replace("\n", "")
        result = [0, 0]
        for i in string.ascii_lowercase:
            if line.count(i) == 2:
                result[0] += 1
            if line.count(i) == 3:
                result[1] += 1
        if result[0] != 0:
            counter1 += 1
        if result[1] != 0:
            counter2 += 1

        list_codes.append(line)


test = ["abcde", "fghij", "klmno", "pqrst", "fguij", "axcye", "wvxyz"]
"""

# part2

with open("ex2.txt") as exercise:
    data = exercise.readlines()
    data = [i.strip() for i in data]

for i, line in enumerate(data):
    ref = i
    while ref < len(data) - 1:
        diff = jellyfish.damerau_levenshtein_distance(line, data[ref + 1])
        # print(i, ref + 1, line, data[ref + 1])
        if diff == 1:
            answer = line, data[ref + 1]
        ref += 1
        # print(diff)

print(answer)

matcher = difflib.SequenceMatcher(None, answer[0], answer[1])

common_values = []

ok = matcher.get_matching_blocks()

print(answer[0][0:9] + answer[0][10:26] + answer[0][26:])

for i in ok:
    print(i)
