import re
import bisect


with open("ex3.txt") as exo:
    exo = exo.read().splitlines()
    exo = "".join(exo)

reg = r"mul\(\d{1,3},\d{1,3}\)"
regdo = r"do()"
regdont = r"don't()"

allmul = {}
do_dont = {}


data = re.finditer(reg, exo)
dos = re.finditer(regdo, exo)
donts = re.finditer(regdont, exo)
for match in data:
    mul = match.group()
    index = match.start()
    mul = mul.removeprefix("mul(").removesuffix(")").split(",")
    term1, term2 = int(mul[0]), int(mul[1])
    allmul[int(index)] = (term1, term2)
for do in dos:
    index = do.start()
    do_dont[int(index)] = "do"
for dont in donts:
    index = dont.start()
    do_dont[int(index)] = "don't"


enable = True
valid_inputs = []
for i in range(len(exo)):
    if i in do_dont.keys():
        if do_dont[i] == "don't":
            enable = False
        if do_dont[i] == "do":
            enable = True
    if enable == True:
        valid_inputs.append(i)

n = 0
for key, value in allmul.items():
    if key in valid_inputs:
        n += value[0] * value[1]

print(n)
