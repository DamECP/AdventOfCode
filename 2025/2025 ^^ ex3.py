with open("ex3.txt") as exercise:
    data = [i.strip() for i in exercise.readlines()]


def battery(number: str, size: int) -> int:
    answer = []
    left = 0

    while len(answer) < size:
        right = len(number) - (size - len(answer)) + 1
        window = number[left:right]
        max_value = max([int(i) for i in window])
        index = window.index(str(max_value))
        answer.append(str(max_value))
        left += index + 1

    return int("".join(answer))


answer_1 = 0
answer_2 = 0

for elt in data:
    answer_1 += battery(elt, 2)
    answer_2 += battery(elt, 12)

print(answer_1)
print(answer_2)
