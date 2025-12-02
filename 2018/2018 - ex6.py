with open("ex6test.txt") as exercise:
    data = exercise.readlines()
    data = [[int(i.strip()) for i in elt.split(",")] for elt in data]

max_x = max([i[0] for i in data])
max_y = max([i[1] for i in data])
min_x = min([i[0] for i in data])
min_y = min([i[1] for i in data])

# build a counter for each input
closest = {tuple(coord): 0 for coord in data}

# build all area for each place
for i in range(min_x, max_x + 1):
    for j in range(min_y, max_y + 1):
        distances = {
            tuple(coord): abs(coord[0] - i) + abs(coord[1] - j) for coord in data
        }
        min_dist = min(distances.values())
        closest_coords = [
            coord for coord, dist in distances.items() if dist == min_dist
        ]
        # increment only if it is the unique closest
        if len(closest_coords) == 1:
            closest[closest_coords[0]] += 1

infinite_coords = set()

# left and right infinite
for i in range(min_x, max_x + 1):
    for j in [min_y, max_y]:
        distances = {
            tuple(coord): abs(coord[0] - i) + abs(coord[1] - j) for coord in data
        }
        min_dist = min(distances.values())
        closest_coords = [
            coord for coord, dist in distances.items() if dist == min_dist
        ]
        if len(closest_coords) == 1:
            infinite_coords.add(closest_coords[0])

# up and down infinite
for j in range(min_y, max_y + 1):
    for i in [min_x, max_x]:
        distances = {
            tuple(coord): abs(coord[0] - i) + abs(coord[1] - j) for coord in data
        }
        min_dist = min(distances.values())
        closest_coords = [
            coord for coord, dist in distances.items() if dist == min_dist
        ]
        if len(closest_coords) == 1:
            infinite_coords.add(closest_coords[0])

# filter out infinite elts
finite_closest = {
    coord: size for coord, size in closest.items() if coord not in infinite_coords
}

# part_1
print(max(finite_closest.values()))

print(finite_closest)
