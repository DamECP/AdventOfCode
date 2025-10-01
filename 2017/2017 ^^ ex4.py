total  = 0
with open('ex4.txt') as exercise:
    for line in exercise:
        line = line.replace('\n', '')
        line = line.split(" ")

        line = [''.join(sorted(i)) for i in line]

        if len(set(line)) == len(line):
            total +=1

print(total)