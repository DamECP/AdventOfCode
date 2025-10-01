import os
import hashlib
os.chdir(r'C:\Users\damie\Documents\Code\Adventcode\2015')

with open('ex4.txt') as exercise:
    for line in exercise:
        code = line.replace('\n', '')

def md5():
    i = 0
    testcode = "bgvyzdsv"
    while True:
        fullcode = testcode + str(i)
        result = hashlib.md5(fullcode.encode('utf-8')).hexdigest()
        if result.startswith("000000"):
            print(i, fullcode)
            break
        
        i += 1
        print(i)

md5()
