# Part 1

"""with open("ex8.txt") as exercise:
    score = 0
    for line in exercise:
        line = line.replace("\n", "")
        input_section, output_section = (i.strip() for i in line.split("|"))

        elements = [i for i in output_section.split(" ") if len(i) in [2, 3, 4, 7]]
        score += len(elements)


print(score)
"""

# part 2

with open("ex8.txt") as exercise:

    answer = 0
    for line in exercise:
        numbers = {}

        line = line.replace("\n", "")
        input_section, output_section = (i.strip() for i in line.split("|"))
        data = [i for i in input_section.split(" ")]

        numbers[1] = [i for i in data if len(i) == 2][0]
        data.remove(numbers[1])

        numbers[4] = [i for i in data if len(i) == 4][0]
        data.remove(numbers[4])

        numbers[7] = [i for i in data if len(i) == 3][0]
        data.remove(numbers[7])

        numbers[8] = [i for i in data if len(i) == 7][0]
        data.remove(numbers[8])

        numbers[9] = [
            i for i in data if len(i) == 6 and all(n in i for n in numbers[4])
        ][0]
        data.remove(numbers[9])

        numbers[0] = [
            i for i in data if len(i) == 6 and all(n in i for n in numbers[1])
        ][0]
        data.remove(numbers[0])

        numbers[6] = [i for i in data if len(i) == 6][0]
        data.remove(numbers[6])

        numbers[3] = [i for i in data if all(n in i for n in numbers[1])][0]
        data.remove(numbers[3])

        numbers[5] = [i for i in data if all(n in numbers[6] for n in i)][0]
        data.remove(numbers[5])

        numbers[2] = data[0]

        reverse = {"".join(sorted(v)): k for k, v in numbers.items()}

        value = [
            str(reverse.get("".join(sorted(elt)))) for elt in output_section.split(" ")
        ]
        value = int("".join(value))

        answer += value


print(answer)
