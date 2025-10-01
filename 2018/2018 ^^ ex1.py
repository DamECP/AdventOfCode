# part 1

"""with open("ex1.txt") as exercise:
    start = 0
    results = []
    for line in exercise:
        line = line.replace("\n", "")
        n = int(line[0:])
        start += n
        results.append(start)

set_list = list(set(results))

print(len(results))
print(len(set_list))

"""

with open("ex1.txt") as exercise:
    data = exercise.read().split("\n")
    data = [int(i) for i in data if i != ""]

test = [+3, +3, +4, -2, -4]


def double(data: list):
    start = 0
    results = set()
    while True:

        for i in data:
            start += i
            if start in results:
                return start
            results.add(start)


print(double(data))
