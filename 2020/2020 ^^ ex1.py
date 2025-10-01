numbers = []

with open('ex1.txt') as exercise:
    for line in exercise:
        line = line.replace('\n', '')
        numbers.append(int(line))
    
for i, item in enumerate(numbers):
    for j in numbers[i+1:]:
        for k in numbers[i+2:]:
            if item + k + j == 2020:
                print(item * k* j)