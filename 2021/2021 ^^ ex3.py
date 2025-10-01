with open("ex3.txt") as exercise:
    gamma = ""
    epsilon = ""
    index = 0

    exercise_lines = exercise.readlines()
    exercise_lines = [i.replace("\n", "") for i in exercise_lines]
    line_length = len(exercise_lines[0].strip())
"""
part 1
    while index < line_length:
        word = ""
        for line in exercise_lines:
            line = line.strip()

            word += line[index]

        zero = word.count("0")
        one = word.count("1")

        if zero > one:
            gamma += "0"
            epsilon += "1"

        elif one > zero:
            gamma += "1"
            epsilon += "0"

        index += 1


gamma = int(gamma, 2)
epsilon = int(epsilon, 2)

print(gamma * epsilon)
"""


def higher(array: list, n: int):

    if len(array) == 1:
        return array[0]

    ones = [i for i in array if i[n] == "1"]
    zeros = [i for i in array if i[n] == "0"]

    maxi = ones if len(ones) >= len(zeros) else zeros

    print(maxi)

    return higher(maxi, n + 1)


def lower(array: list, n: int):

    if len(array) == 1 or n >= len(array[0]):
        return array[0]

    ones = [i for i in array if i[n] == "1"]
    zeros = [i for i in array if i[n] == "0"]

    mini = ones if len(ones) < len(zeros) else zeros

    print(mini)

    return lower(mini, n + 1)


# conversion from binary to base 10 int
print(exercise_lines)
n1 = int(higher(exercise_lines, 0), 2)
print()
print(exercise_lines)
n2 = int(lower(exercise_lines, 0), 2)

print(n1 * n2)
