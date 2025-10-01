raw_len = 0
interpreted_len = 0

with open("ex8.txt") as exercise:
    lines = exercise.readlines()
    lines = [i.strip() for i in lines]

general_counter = 0
all_lengths = 0
for line in lines:
    length = len(line)
    all_lengths += length
    counter = 2  # les 2 guillemets
    list_ord = [ord(i) for i in line]
    for _ in list_ord:
        if _ == 34:
            counter += 2
        elif _ == 92:
            counter += 2
        else:
            counter += 1
    general_counter += counter


print(general_counter - all_lengths)
