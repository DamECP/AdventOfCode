with open('ex1.txt') as exercise:
    for line in exercise:
        line = line.replace('\n', '')

test1 = "1122"
test2 = "1111"
test3 = "1234"
test4 = "91212129"



def solution(str):
    ok_strs = []
    for i in range(len(str)-1):
        if str[i] == str[i+1]:
            ok_strs.append(int(str[i]))
    if str[-1]==str[0]:
        ok_strs.append(int(str[-1]))
    print(sum(ok_strs))

test5 = "1212"
test6 = "1221"
test7 = "123425"
test8 = "123123"
test9 = "12131415"


def solutionV2(str):
    ok_strs = []
    ref = len(str)//2
    str = str+str[0:ref]
    for i in range(len(str)-ref):
        if str[i] == str[i+ref]:
            ok_strs.append(int(str[i]))
    if str[-1]==str[0]:
        ok_strs.append(int(str[-1]))
    print(sum(ok_strs))

solutionV2(line)



