with open("ex2.txt") as exercise:
    for line in exercise:
        line = line.replace("\n", "")
        instructions_list = line.split(",")
        instructions_list = [int(i) for i in instructions_list]

        for n in range(0, 100):
            for n2 in range(0, 100):
                instructions = instructions_list[:]
                instructions[1] = n
                instructions[2] = n2
                i = 0

                while i < len(instructions):
                    operation = instructions[i]
                    index1 = instructions[i + 1]
                    index2 = instructions[i + 2]
                    index3 = instructions[i + 3]
                    if operation == 99:
                        break

                    elif operation == 1:
                        instructions[index3] = (
                            instructions[index1] + instructions[index2]
                        )

                    elif operation == 2:
                        instructions[index3] = (
                            instructions[index1] * instructions[index2]
                        )

                    i += 4

                result = instructions[0]
                if result == 19690720:
                    print(result)
                    print(n * 100 + n2)
