import numpy as np

with open("ex8.txt") as exercise:
    data = [
        tuple(int(n) for n in line.strip().split(",")) for line in exercise.readlines()
    ]


def get_distances(boxes: list[tuple]) -> tuple:
    closest = float("inf")
    distances = []

    for i, b1 in enumerate(boxes):
        p1 = np.array(b1)
        for j in range(i + 1, len(boxes)):
            b2 = boxes[j]
            p2 = np.array(b2)
            distance = float(np.linalg.norm(p2 - p1))
            distances.append([distance, b1, b2])

    return sorted(distances, key=lambda x: x[0])


sorted_distances = get_distances(data)

circuits = [set([sorted_distances[0][1], sorted_distances[0][2]])]

for box in sorted_distances[1:1001]:
    p1, p2 = box[1], box[2]
    added = False

    for c in circuits:
        if p1 in c or p2 in c:
            c.add(p1)
            c.add(p2)
            added = True
            break

    if not added:
        circuits.append(set([p1, p2]))

answer_1 = 1
for i in circuits[:3]:
    answer_1 *= len(i)

print(answer_1)
