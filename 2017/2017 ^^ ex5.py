with open("ex5.txt") as exercise:
    data = exercise.readlines()
    data = [int(i.strip()) for i in data]

n = 0
steps = 0

while 0 <= n < len(data):
    jump = data[n]
    if jump >= 3:
        data[n] -= 1
    else:
        data[n] += 1
    n += jump
    steps += 1


print(steps)
