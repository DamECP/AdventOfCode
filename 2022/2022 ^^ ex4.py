with open("ex4.txt") as exercise:
    useless_elves = 0
    overlapping = 0
    for line in exercise:
        line = line.replace("\n", "").split(",")
        elf_1, elf_2 = line[0].split("-"), line[1].split("-")
        # print(elf_1, elf_2)
        elf_1 = [int(i) for i in range(int(elf_1[0]), int(elf_1[1]) + 1)]
        elf_2 = [int(i) for i in range(int(elf_2[0]), int(elf_2[1]) + 1)]
        # print(len(elf_1), len(elf_2))
        crossed_missions = set(elf_1) & set(elf_2)
        # print(crossed_missions)
        # print(len(crossed_missions))
        # if len(elf_1) == len(crossed_missions) or len(elf_2) == len(crossed_missions):
        # useless_elves += 1
        if len(crossed_missions) > 0:
            overlapping += 1

print(overlapping)
