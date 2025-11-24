from collections import defaultdict

with open("ex10test.txt") as exercise:
    data = [i.strip() for i in exercise.readlines()]

print(data)

coordinates = defaultdict(list)

for y, row in enumerate(data):
    for x, col in enumerate(row):
        try:
            col = int(col)
        except ValueError:
            pass
        coordinates[col].append((x, y))

print(coordinates)


def get_next(current: tuple, n, path):
    if n not in coordinates:
        return path

    for candidate in coordinates[n]:
        if current[0] == candidate[0] or current[1] == candidate[1]:

            sub_path = get_next(candidate, n + 1, path + [candidate])
            all_paths.extend(sub_path)
    return False


all_paths = []

for start in coordinates[0]:
    for next_value in coordinates[1]:
        if start[0] == next_value[0] or start[1] == next_value[1]:
            result = get_next(next_value, 2, [start, next_value])
            if result:
                full_paths.append(result)


print(len(full_paths))
