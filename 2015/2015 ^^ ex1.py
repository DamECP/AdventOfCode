import os

os.chdir(r'C:\Users\damie\Documents\Code\Adventcode\2015')


with open('ex1.txt') as exercise:
    result = 0
    for line in exercise:
        line = line.replace('\n', '')
        for i, char in enumerate(line,1): 
            if char == "(":
                result += 1
            if char ==")":
                result -= 1
            if result == -1:
                print(i)