with open("ex4.txt") as exercise:
    for line in exercise:
        line = line.replace("\n", "")

import re


def adjacent(n):
    pattern = r"(\d)\1"
    matches = re.findall(pattern, str(n))

    for i in matches:
        if i[0] * 3 not in str(n):
            return True


def increase(n):
    n = str(n)
    if "".join(sorted(n)) == n:
        return True


n = 0
for i in range(245182, 790572):
    if adjacent(i) and increase(i):
        n += 1

print(n)
