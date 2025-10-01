total =  0
list_of_lines = []
with open('ex2.txt') as exercise:
    for line in exercise:
        line = line.replace('\n', '')
        line = line.split("\t")

        line = [int(i) for i in line]

        list_of_lines.append(line)    

        mini = min(line)
        maxi = max(line)

        n = maxi - mini

        total += n

def dividables(list):
    divid = []
    for i in sorted(list):
        for j in sorted(list):
            if i%j == 0 and i/j !=1:
                divid.append(i/j)

    return sum(divid)

final_list = []

for i in list_of_lines:
    final_list.append(dividables(i))

print(sum(final_list))