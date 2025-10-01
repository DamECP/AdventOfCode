from collections import deque

with open("ex6.txt") as exercise:
    data = exercise.read()
    data = [int(i) for i in data.split(",")]

test = data
test = [test.count(i) for i in range(9)]

while len(test) < 9:
    test.append(0)

test = deque(test)
print(test)

for i in range(256):

    new_fishes = test.popleft()
    test[6] += new_fishes
    test.append(new_fishes)
    print(test)

print(sum(test))
