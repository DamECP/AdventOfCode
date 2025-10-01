with open("ex5.txt") as exercise:
    data = exercise.read()

dataset = data.replace("\n", " ").split(" ")

seeds = [int(i) for i in dataset[1:21]]

seeds_v2 = [seeds[i : i + 2] for i in range(0, len(seeds), 2)]
new_set_of_seeds = []

for line in seeds_v2:
    start, end = line[0], line[0] + line[1]
    for i in range(start, end):
        print(i)
    print()


"""
seed_to_soil = {}
s_to_s_data = dataset[24:51]
s_to_s_data = [s_to_s_data[i : i + 3] for i in range(0, len(s_to_s_data), 3)]


s_to_f_data = dataset[54:183]
s_to_f_data = [s_to_f_data[i : i + 3] for i in range(0, len(s_to_f_data), 3)]


f_to_w_data = dataset[186:324]
f_to_w_data = [f_to_w_data[i : i + 3] for i in range(0, len(f_to_w_data), 3)]


w_to_l_data = dataset[327:447]
w_to_l_data = [w_to_l_data[i : i + 3] for i in range(0, len(w_to_l_data), 3)]


l_to_t_data = dataset[450:561]
l_to_t_data = [l_to_t_data[i : i + 3] for i in range(0, len(l_to_t_data), 3)]


t_to_h_data = dataset[564:618]
t_to_h_data = [t_to_h_data[i : i + 3] for i in range(0, len(t_to_h_data), 3)]


h_to_l_data = dataset[621:-1]
h_to_l_data = [h_to_l_data[i : i + 3] for i in range(0, len(h_to_l_data), 3)]


def converter(n, conversion: list) -> int:
    for line in conversion:
        destination, source, range_length = map(int, line)
        if int(n) in range(source, source + range_length):
            value = n - source + destination
            return value

    return n


operations = [
    s_to_s_data,
    s_to_f_data,
    f_to_w_data,
    w_to_l_data,
    l_to_t_data,
    t_to_h_data,
    h_to_l_data,
]


smallest_value = float("inf")

for seed in seeds:
    for operation in operations:
        seed = converter(seed, operation)

    smallest_value = min(smallest_value, seed)

print(smallest_value)
"""
