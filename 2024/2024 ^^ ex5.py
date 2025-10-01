import random

with open("ex5.txt") as test:
    data = test.readlines()
    rules = [i.strip() for i in data if "|" in i]
    lists = [i.strip() for i in data if "," in i]

# part1

total = 0

invalid_lists = []


for l in lists:
    l = l.split(",")
    l = [int(i) for i in l]
    rules_valid = True
    for r in rules:
        a, b = r.split("|")
        a, b = int(a), int(b)
        if a in l and b in l:
            if l.index(a) > l.index(b):
                # print("error", l)
                rules_valid = False
                invalid_lists.append(l)
                break

    if rules_valid:
        ans = l[len(l) // 2]
        total += ans

# print(total)


# part2
total = 0
for l in invalid_lists:
    # print("Liste de départ : \n", l)
    rules_valid = False
    while not rules_valid:
        rules_valid = True
        for r in rules:
            # print(r)
            a, b = r.split("|")
            a, b = int(a), int(b)
            if a in l and b in l:
                if l.index(a) > l.index(b):
                    # print("Liste erronnée : \n", l, r)
                    l[l.index(a)], l[l.index(b)] = l[l.index(b)], l[l.index(a)]
                    # print("Liste rectifiée : \n", l)
                    rules_valid = False
                    break
            rules_valid = True
    total += l[len(l) // 2]

print(total)
