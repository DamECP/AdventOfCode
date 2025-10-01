from collections import Counter

with open("ex5.txt") as exercise:
    data = exercise.readlines()
    coordinates = []
    for line in data:
        item = line.strip().split(" ")
        one = item[0].split(",")
        x1, y1 = int(one[0]), int(one[1])
        two = item[-1].split(",")
        x2, y2 = int(two[0]), int(two[1])
        if x1 == x2:
            mini, maxi = min(y1, y2), max(y1, y2)
            for i in range(mini, maxi + 1):
                coord = (x1, i)
                coordinates.append(coord)
        elif y1 == y2:
            mini, maxi = min(x1, x2), max(x1, x2)
            for i in range(mini, maxi + 1):
                coord = (i, y1)
                coordinates.append(coord)
        else:
            dx = 1 if x2 > x1 else -1
            dy = 1 if y2 > y1 else -1
            for i in range(abs(x2 - x1) + 1):
                coord = (x1 + i * dx, y1 + i * dy)
                coordinates.append(coord)


counts = Counter(coordinates)
duplicates = [item for item, count in counts.items() if count > 1]
print(len(duplicates))
