from itertools import groupby, chain

with open("ex9.txt") as exercise:
    data = exercise.readline().strip()

# answer 1
memory = []
n = 0
for i, char in enumerate(data):
    for _ in range(int(char)):
        if i % 2 == 0:
            memory.append(n)
        else:
            memory.append(".")
    if i % 2 == 0:
        n += 1

compressed = []
copy = [i for i in memory if isinstance(i, int)]
max_len = len(copy)

for i in memory:
    if len(compressed) >= max_len:
        break
    elif i != ".":
        compressed.append(i)
    else:
        item = copy.pop()
        if isinstance(item, int):
            compressed.append(item)
        else:
            continue

answer_1 = 0
for i, elt in enumerate(compressed):
    n = i * elt
    answer_1 += n


memory_v2 = [(list(group)) for _, group in groupby(memory)]
candidates = [i for i in memory_v2 if "." not in i][::-1]

for j, elt in enumerate(candidates):

    if 0 in elt:
        break

    index = memory_v2.index(elt)
    size = len(elt)

    for _, item in enumerate(memory_v2[:index]):
        if all(i == "." for i in item) and len(item) >= size:

            # print("candidat =", elt)

            diff = len(item) - size
            elt_dots = diff * ["."]
            elt += elt_dots
            replace_dots = list(size * ".")

            copy = memory_v2.copy()

            copy[index] = replace_dots
            copy[_] = elt

            copy = list(chain.from_iterable(copy))
            # string_version = "".join([str(i) for i in copy])

            memory_v2 = [(list(group)) for _, group in groupby(copy)]

            # print(memory_v2)
            # print()

            break

final_compression = list(chain.from_iterable(memory_v2))

answer_2 = 0
for i, elt in enumerate(final_compression):
    if isinstance(elt, int):
        n = i * elt
        answer_2 += n

print(answer_2)
