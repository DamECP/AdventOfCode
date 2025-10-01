import os
os.chdir(r'C:\Users\damie\Documents\Code\Adventcode\2015')

def surface(gift: list) -> int:
    result = (2*gift[0]*gift[1])+(2*gift[0]*gift[2])+(2*gift[1]*gift[2])
    extra = sorted(gift)[0] * sorted(gift)[1]
    result += extra
    return result

def ribbon(gift: list) -> int:
    result = ((sorted(gift)[0]*2) + (sorted(gift)[1]*2) + (gift[0]*gift[1]*gift[2]))
    return result
    

with open('ex2.txt') as exercise:
    total = []
    for line in exercise:
        line = line.replace('\n', '')
        gift = line.split("x")
        gift = [int(x) for x in gift]
        total.append(ribbon(gift))

print(sum(total))
