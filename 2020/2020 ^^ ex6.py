with open("ex6.txt") as exercise:
    data = exercise.readlines()
    data = [i.strip() for i in data]

# part1
total = 0
letters = []
for line in data:
    letters.extend(list(line))
    if line == "":
        letters = set(list(letters))
        total += len(letters)
        letters = []
letters = set(list(letters))
total += len(letters)


# print(total)

# part2

total = 0
letters = []
n = -1
for line in data:
    print(line)
    letters.extend(list(line))
    n += 1
    if line == "":
        print(letters)
        print(n)
        for letter in set(letters):
            if letters.count(letter) == n:
                total += 1
        print(f"total = {total}")
        print()
        letters = []
        n = -1
print(letters)
print(n)

n += 1
for letter in set(letters):
    if letters.count(letter) == n:
        total += 1

print()
print(total)
