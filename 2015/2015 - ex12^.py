import string

with open('ex12.txt') as exercise:
    for line in exercise:
        line = line.replace('\n', '')

new_str = ""

for char in line:
    if char in string.digits or char in ["-", ","]:
        new_str += char

answer = 0
for i in new_str.split(","):
    try:
        answer+=(int(i))
    except:
        TypeError

print(answer)
