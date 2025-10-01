with open("ex6.txt") as exercise:
    data = exercise.read()


def window(list: list):
    start = 0
    instruction = 14  # part 1 => 4
    while start <= len(list) - instruction:
        check = list[start : start + instruction]
        if len(set(check)) == instruction:
            return start + instruction
        start += 1
    print("Fail")


print(window(data))
