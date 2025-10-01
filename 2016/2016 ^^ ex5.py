import hashlib

with open("ex5.txt") as exercise:
    for line in exercise:
        line = line.replace("\n", "")


test = "abc"


def pass1(input: str):

    n = 0
    regex = r"^0{5}"
    password = ""
    while len(password) < 8:
        test_string = input + str(n)
        md5 = hashlib.md5(test_string.encode()).hexdigest()
        if re.match(regex, md5):
            password += md5[5]
            print(md5, password)
        n += 1


print(pass1(line))


def passv2(input: str):

    n = 0
    password_v2 = ["", "", "", "", "", "", "", ""]
    while "" in password_v2:
        test_string = input + str(n)
        md5 = hashlib.md5(test_string.encode()).hexdigest()
        if md5.startswith("00000"):
            position = md5[5]
            if position.isdigit() and int(position) in range(0, 8):
                if password_v2[int(position)] == "":
                    password_v2[int(position)] = md5[6]
        n += 1
    return "".join(password_v2)


print(passv2(line))
