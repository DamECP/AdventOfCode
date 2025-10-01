list1 = []
list2 = []

with open("ex1.txt") as exo:
    for line in exo:
        line = line.replace("\n", "")
        data = line.split()
        list1.append(int(data[0]))
        list2.append(int(data[1]))

list1.sort()
list2.sort()

def diff():
    differences = []
    for i, index in enumerate(list1):
        differences.append(abs(index - list2[i]))
    print(sum(differences))

def similarity():
    total = []
    for i in list1:
        n = 0
        for j in list2:
            if i == j:
                n+=1
        i *= n
        total.append(i)
    print(sum(total))

similarity()