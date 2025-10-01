with open("ex6test.txt") as exercise:
    data = exercise.readlines()
    data = [tuple(map(int, i.strip().split(","))) for i in data]
    min_x = min(data, key=lambda x: x[0])[0]
    max_x = max(data, key=lambda x: x[0])[0]
    min_y = min(data, key=lambda y: y[1])[1]
    max_y = max(data, key=lambda y: y[1])[1]


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, a: int, b: int):
        x_distance = abs(self.x - a)
        y_distance = abs(self.y - b)
        return x_distance + y_distance

    def __str__(self):
        return f"{self.x}, {self.y}"


points = set()
for i in data:
    x, y = i[0], i[1]
    point = Point(x, y)
    points.add(point)

counter = 0
for i in range(0, max_x):
    for j in range(0, max_y):
        distances = []
        print(i, j)
        for point in points:
            print(point)
            distance = point.distance(i, j)
            distances.append(distance)
        if distances.count(min(distances)) == 1:
            print("+++")
            counter += 1
        print(distances)
        print()
print(counter)
