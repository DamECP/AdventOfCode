with open("ex8.txt") as exercise:
    data = [int(i) for i in exercise.readline().split(" ")]

n = 0

while True:
    start = data[n]
    next_n = data[n + 1]

    n += next_n

print(n)
