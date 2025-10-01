with open('ex11.txt') as exercise:
    for line in exercise:
        line = line.replace('\n', '')
        print(line)