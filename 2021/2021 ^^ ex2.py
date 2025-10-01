x, aim = 0, 0
depth = 0


with open("ex2.txt") as exercise:
    for line in exercise:
        line = line.replace("\n", "")
        instruction = line.split(" ")

        if instruction[0] == "down":
            aim += int(instruction[1])
        elif instruction[0] == "up":
            aim -= int(instruction[1])
        elif instruction[0] == "forward":
            x += int(instruction[1])
            depth += aim * int(instruction[1])
        print(f"aim = {aim}     x = {x}     depth = {depth}")


print(x * depth)
