from collections import defaultdict

with open("ex5.txt") as exercise:
    data = [i.strip() for i in exercise.readlines()]

seeds = [int(i) for i in data[0].split() if i.isdigit()]

seed_to_soil = [[int(elt) for elt in i.split(" ")] for i in data[3:12]]
soil_to_fertilizer = [[int(elt) for elt in i.split(" ")] for i in data[14:57]]
fertilizer_to_water = [[int(elt) for elt in i.split(" ")] for i in data[59:105]]
water_to_light = [[int(elt) for elt in i.split(" ")] for i in data[107:147]]
light_to_temperature = [[int(elt) for elt in i.split(" ")] for i in data[149:186]]
temperature_to_humidity = [[int(elt) for elt in i.split(" ")] for i in data[188:206]]
humidity_to_location = [[int(elt) for elt in i.split(" ")] for i in data[208:]]

chain = [
    seed_to_soil,
    soil_to_fertilizer,
    fertilizer_to_water,
    water_to_light,
    light_to_temperature,
    temperature_to_humidity,
    humidity_to_location,
]


def in_and_out(n: int, dataset):
    for i in dataset:
        ref_range = range(i[1], i[1] + i[2])
        if n in ref_range:
            diff = i[0] - i[1]
            new_n = n + diff
            return new_n
    return n


locations = []
for seed in seeds:
    for c in chain:
        seed = in_and_out(seed, c)
    locations.append(seed)

answer_1 = min(locations)
# print(answer_1)


part_2 = []
ranges = [
    (seeds[n], seeds[n] + seeds[n + 1]) for n, seed in enumerate(seeds) if n % 2 == 0
]


test_range = ranges[0]
test_chain = chain[0]


def change(input_range, instructions):
    pending = [input_range]
    output = []

    for dest, src, length in instructions:
        src_start = src
        src_end = src + length - 1
        diff = dest - src

        new_pending = []

        for left, right in pending:

            # pas d'intersection
            if right < src_start or left > src_end:
                new_pending.append((left, right))
                continue

            # partie avant
            if left < src_start:
                new_pending.append((left, src_start - 1))
                left = src_start

            # partie après
            if right > src_end:
                new_pending.append((src_end + 1, right))
                right = src_end

            # partie à convertir
            output.append((left + diff, right + diff))

        pending = new_pending

    return output + pending


final_ranges = []

for r in ranges:
    transformed = [r]
    for c in chain:
        new_list = []
        for interval in transformed:
            new_list.extend(change(interval, c))
        transformed = new_list

    final_ranges.extend(transformed)

print(min(left for left, right in final_ranges))
