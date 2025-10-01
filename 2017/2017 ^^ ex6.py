with open("ex6.txt") as exercise:
    data = exercise.read().strip().split("\t")
    data = [int(i) for i in data]

test = [0, 2, 7, 0]
test = data
answer = list()
counter = 0
cycle = 0

while True:
    if tuple(test) not in answer:
        answer.append(tuple(test))
    else:
        print(len(answer))
        break
    biggest = max(test)
    position = test.index(biggest)
    test[position] = 0
    for i in range(1, biggest + 1):
        test[(position + i) % len(test)] += 1

    cycle += 1

print(len(answer) - list(answer).index(tuple(data)))
