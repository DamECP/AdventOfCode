with open("ex6.txt") as exercise:
    data = exercise.read()


def race(time: int, current_record: int):
    winning_patterns = 0
    for i in range(time + 1):
        speed = time - i
        record = i * speed
        if record > current_record:
            winning_patterns += 1
    return winning_patterns


# part1

result_1 = race(42, 308)
result_2 = race(89, 1170)
result_3 = race(91, 1291)
result_4 = race(89, 1467)

answer = result_1 * result_2 * result_3 * result_4

# print(answer)


# part2

big_race = race(42899189, 308117012911467)
print(big_race)
