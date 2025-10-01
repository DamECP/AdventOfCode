import re
import string

possibilities = []

possibilities.extend(zip(string.ascii_lowercase, string.ascii_uppercase))
possibilities.extend(zip(string.ascii_uppercase, string.ascii_lowercase))

all_possibilities = ["".join(i) for i in possibilities]


def make_it_regex(elt):
    elt = "r'" + i + "'"
    return elt


with open("ex5.txt") as exercise:
    for line in exercise:
        line = line.strip()

print(all_possibilities)


def minimal_polymer(line: str):
    while True:
        final_length = len(line)
        for elt in all_possibilities:
            test = re.sub(elt, "", line)
            line = test
        if len(line) == final_length:
            break
    print(f"longueur mini : {len(test)}")


minimal_polymer(line)

for alpha in string.ascii_lowercase:
    print(alpha)
    cleaned_line = line.replace(alpha, "").replace(alpha.upper(), "")
    minimal_polymer(cleaned_line)
