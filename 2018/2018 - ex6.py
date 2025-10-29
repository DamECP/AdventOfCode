with open("ex6.txt") as exercise:
    data = exercise.readlines()
    data = [int(i.strip()) for i in data]
    print(data)
