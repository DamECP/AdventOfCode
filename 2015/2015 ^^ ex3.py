import os
os.chdir(r'C:\Users\damie\Documents\Code\Adventcode\2015')

def path(line: list):
    x = 0
    y = 0
    path = [(x,y)]
    position = (x,y)
    for i, char in enumerate(line):
            if char == ">":
                x += 1
            elif char == "<":
                x -= 1
            elif char == "^":
                y += 1
            elif char == "v":
                y -= 1
            position = (x,y)
            path.append(position)
    return path

with open('ex3.txt') as exercise:
    even = ""
    odd = ""
    for line in exercise:
        line = line.replace('\n', '')
        for i, char in enumerate(line):
            if i %2 == 0:
                even += char
            else:
                odd += char

total = path(even) + path(odd)

print(len(list(set(total))))