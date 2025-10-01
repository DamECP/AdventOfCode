with open("ex8.txt") as exercise:
    data = exercise.read().strip()

width = 2
height = 2

n = 0
start = 0
number = 0

# part1
smallest_zeros_amount = 1000
while n < len(data):
    layer = []
    number += 1
    for i in range(height):
        layer.append(data[start : start + width])
        start += width
    # print(f"layer {number} : {layer}")  # numérote la liste
    string_layer = "".join(layer)  # convertit la liste en str
    zeros_amount = string_layer.count("0")
    if zeros_amount < smallest_zeros_amount:
        smallest_zeros_amount = zeros_amount

        # print(number, zeros_amount, layer)
        # print(string_layer.count("1") * string_layer.count("2"))
        # print()
    n += width * height


width = 25
height = 6

n = 0
start = 0
number = 0

# part2
layers = []
while n < len(data):
    layer = []
    number += 1
    for i in range(height):
        layer.append(data[start : start + width])
        start += width
    layers.append(layer)
    n += width * height


answer = ""

n_layers = len(layers)
# print(n_layers)
n_elts = len(layers[0][0])
# print(n_elts)
len_elt = len(layers[0][0])
# print(len_elt)

# print(layers)

for i in range(len_elt):
    kept_ref = []
    for j in range(n_elts):
        for k in range(n_layers):
            ref = layers[k][i][j]
            # print(ref)
            if ref == "2":
                continue
            elif ref == "1":
                kept_ref.append("|")
                break
            elif ref == "0":
                kept_ref.append(" ")
                break
    print("".join(kept_ref))
