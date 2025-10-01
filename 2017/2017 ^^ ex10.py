from collections import deque

"""origin = list(range(256))
test_input = [192, 69, 168, 160, 78, 1, 166, 28, 0, 83, 198, 2, 254, 255, 41, 12]
size = len(origin)
current_position = 0
skip_size = 0

for length in test_input:

    indices = [(current_position + i) % size for i in range(length)]
    values = [origin[i] for i in indices]

    values.reverse()

    for idx, val in zip(indices, values):
        origin[idx] = val

    current_position = (current_position + length + skip_size) % size
    skip_size += 1

part1 = origin[0] * origin[1]"""


second_input = "192,69,168,160,78,1,166,28,0,83,198,2,254,255,41,12"
second_input = [ord(x) for x in second_input] + [17, 31, 73, 47, 23]

numbers = list(range(256))
size = len(numbers)
current_position = 0
skip_size = 0
print(size)

for _ in range(64):
    for length in second_input:

        indices = [(current_position + i) % size for i in range(length)]
        values = [numbers[i] for i in indices]

        values.reverse()

        for idx, val in zip(indices, values):
            numbers[idx] = val

        current_position = (current_position + length + skip_size) % size
        skip_size += 1

sequences = []
sub = []
for i, number in enumerate(numbers, start=1):
    sub.append(number)
    if i % 16 == 0:
        sequences.append(sub)
        sub = []

new_seq = []
for seq in sequences:
    xor = 0
    for num in seq:
        xor = xor ^ num
    new_seq.append(xor)


test = new_seq

hexa = "".join([hex(i)[-2:].replace("x", "0") for i in test])
print(hexa)
