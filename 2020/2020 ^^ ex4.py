import re


def color_check(string: str):
    color = r"^#[0-9a-f]{6}$"
    return bool(re.match(color, string))


def infos_checker(infos: list):
    required_fields = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}
    present_fields = {elt[0] for elt in infos}

    if not required_fields.issubset(present_fields):
        print(f"Missing fields: {required_fields - present_fields}")
        return False

    for elt in infos:
        try:
            if elt[0] == "byr":
                if not 1920 <= int(elt[1]) <= 2002:
                    print(f"Invalid byr: {elt[1]}")
                    return False
            elif elt[0] == "iyr":
                if not 2010 <= int(elt[1]) <= 2020:
                    print(f"Invalid iyr: {elt[1]}")
                    return False
            elif elt[0] == "eyr":
                if not 2020 <= int(elt[1]) <= 2030:
                    print(f"Invalid eyr: {elt[1]}")
                    return False
            elif elt[0] == "hgt":
                if "cm" in elt[1]:
                    size = int(elt[1][:-2])
                    if not 150 <= size <= 193:
                        print(f"Invalid hgt (cm): {elt[1]}")
                        return False
                elif "in" in elt[1]:
                    size = int(elt[1][:-2])
                    if not 59 <= size <= 76:
                        print(f"Invalid hgt (in): {elt[1]}")
                        return False
                else:
                    print(f"Invalid hgt format: {elt[1]}")
                    return False
            elif elt[0] == "hcl":
                if not color_check(elt[1]):
                    print(f"Invalid hcl: {elt[1]}")
                    return False
            elif elt[0] == "ecl":
                valid_ecl = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
                if elt[1] not in valid_ecl:
                    print(f"Invalid ecl: {elt[1]}")
                    return False
            elif elt[0] == "pid":
                valid_n = r"^[0-9]{9}$"
                if not re.match(valid_n, elt[1]):
                    print(f"Invalid pid: {elt[1]}")
                    return False
            elif elt[0] == "cid":
                continue
            else:
                print(f"Unknown field: {elt[0]}")
                return False
        except ValueError:
            print(f"Value error for field: {elt[0]} with value: {elt[1]}")
            return False
    return True


n = 1
with open("ex4.txt") as exercise:
    passports = []
    infos = ""
    for line in exercise:
        line = line.strip()
        infos += " " + line

        if line == "":
            infos = infos.split(" ")[1:-1]
            infos = [i.split(":") for i in infos]
            if infos_checker(infos):
                passports.append(infos)
            infos = ""

print(len(passports))
