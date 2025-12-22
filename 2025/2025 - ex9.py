with open("ex9.txt") as exercise:
    data = [i.strip().split(",") for i in exercise.readlines()]


def get_surface(point: list, points: list[tuple]) -> int:
    a, b = (int(i) for i in point)
    ref = 0
    for p in points:
        x, y = int(p[0]), int(p[1])
        surface = (abs(a - x) + 1) * (abs(b - y) + 1)
        if surface > ref:
            ref = surface

    return ref


largest = 0
for i, coord in enumerate(data[:-1]):
    current = get_surface(coord, data[i + 1 :])
    if current > largest:
        largest = current

print(largest)
