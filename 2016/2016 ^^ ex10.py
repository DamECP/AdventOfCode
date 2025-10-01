class Container:
    def __init__(self, name: str):
        self.name = name
        self.values = []

    def get_value(self, value):
        self.values.append(value)

    def share(self):
        if len(self.values) == 2 and "bot" in self.name:
            return [self.values[0], self.values[1]]

    def reset(self):
        self.values = []

    def __str__(self):
        return f"{self.name} => {self.values}"


with open("ex10.txt") as exercise:
    data = exercise.readlines()
    data = [i.strip() for i in data]

start_instructions = []
share_instructions = []

for i in data:
    if i.split(" ")[0] == "value":
        start_instructions.append(i)
    else:
        share_instructions.append(i)

container_list = {}

# prepare the bots with one value
for i in start_instructions:
    value, name = int(i.split(" ")[1]), "".join(i.split(" ")[-2:])
    if name not in container_list:
        container_list[name] = Container(name)
    container_list[name].get_value(value)

executed_instructions = set()

while len(executed_instructions) < len(share_instructions):
    for instruction in share_instructions[:]:
        if instruction in executed_instructions:
            continue

        i = instruction.split(" ")
        giver_name = "".join(i[0:2])
        receiver_1_name = "".join(i[5:7])
        receiver_2_name = "".join(i[-2:])

        checked_characters = (giver_name, receiver_1_name, receiver_2_name)

        for character in checked_characters:
            if character not in container_list:
                container_list[character] = Container(character)

        values = container_list[giver_name].share()

        if values is not None:

            print(instruction)
            if "output" in instruction:
                print("**************************")

            print("donneur =>", container_list[giver_name])
            print(
                "Avant ==>",
                container_list[receiver_1_name],
                container_list[receiver_2_name],
            )

            low, high = min(values), max(values)
            container_list[receiver_1_name].get_value(low)
            print("Après", container_list[receiver_1_name])
            container_list[receiver_2_name].get_value(high)
            print("Après", container_list[receiver_2_name])

            if giver_name.startswith("bot"):
                container_list[giver_name].reset()

            executed_instructions.add(instruction)


n1 = container_list["output0"]
n2 = container_list["output1"]
n3 = container_list["output2"]

print(n1, n2, n3)
