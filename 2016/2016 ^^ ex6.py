from string import ascii_lowercase

data = []
with open("ex6.txt") as exercise:
    for line in exercise:
        data.append(line.strip())

test = ["".join(x) for x in zip(*data)]

for elt in test:
    max = float("inf")
    for char in ascii_lowercase:
        count = elt.count(char)
        if count < max:
            max = count
            ans = char
    print(ans, end="")
