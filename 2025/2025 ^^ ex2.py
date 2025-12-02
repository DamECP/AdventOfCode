import re

with open("ex2.txt") as exercise:
    data = [i.split("-") for i in exercise.readline().split(",")]
    data = [range(int(i[0]), int(i[1]) + 1) for i in data]


def is_silly(number: int) -> bool:
    number = str(number)
    length = len(number)

    if length % 2 == 1:
        return False

    start = number[: length // 2]
    end = number[length // 2 :]
    return start == end


def is_super_silly(number: int) -> bool:
    number = str(number)
    pattern = re.compile(r"^(.+?)\1+$")

    return re.match(pattern, number)


part_1 = []
part_2 = []

for d in data:
    silly = [i for i in list(d) if is_silly(i)]
    part_1.extend(silly)

    super_silly = [i for i in list(d) if is_super_silly(i)]
    part_2.extend(super_silly)

print(sum(part_1))
print(sum(part_2))
