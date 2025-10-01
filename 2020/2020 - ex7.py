with open("ex7.txt") as exercise:
    data = exercise.readlines()
    data = [i.strip() for i in data]

for line in data:
    print(line)
