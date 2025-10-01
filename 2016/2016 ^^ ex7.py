with open("ex7.txt") as exercise:
    data = exercise.readlines()
    data = [i.strip() for i in data]


def splitter(input_str) -> str:
    data = input_str.split("[")
    outsides = [data[0]]
    insides = []
    for i in data[1:]:
        inside, outside = i.split("]")
        insides.append(inside)
        outsides.append(outside)
    return (insides, outsides)


# part_1
def abba_finder(string) -> bool:
    for i in range(len(string) - 3):
        window = string[i : i + 4]
        if (
            window[0] == window[-1]
            and window[1] == window[2]
            and window[0] != window[1]
        ):
            return True
    return False


def TLS_checker(line: str) -> bool:
    insides, outsides = splitter(line)

    for elt in insides:
        if abba_finder(elt):
            return False

    for elt in outsides:
        if abba_finder(elt):
            return True

    return False


# part_2
def aba_finder(string) -> str:  #
    windows = []
    for i in range(len(string) - 2):
        window = string[i : i + 3]
        if window[0] == window[-1] and window[0] != window[1]:
            windows.append(window)
    return windows


def reversed_aba(aba: str) -> str:
    return aba[1] + aba[0] + aba[1]


def SSL_checker(line: str) -> bool:
    insides, outsides = splitter(line)

    abas = [aba for part in outsides for aba in aba_finder(part)]
    babs = [reversed_aba(aba) for aba in abas]

    return any(bab in inside for bab in babs for inside in insides)


answer = 0
for i in data:
    if SSL_checker(i):
        answer += 1

print(answer)
