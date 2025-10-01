import string

instructions = []
wires = {}

with open("ex7.txt") as exercise:
    for line in exercise:
        line = line.replace("\n", "")
        line = line.split(" ")
        # print(line)
        instructions.append(line)

# prépare liste pour les instructions inutilisables au départ
unprocessed_instructions = []

# crée les cables dont les valeurs sont explicites
# ajoute les autres instructions à unprocessed_instructions
for i in instructions:
    if len(i) == 3:
        try:
            i[0] = int(i[0])
            name, value = i[-1], i[0]
            wires[name] = int(value)
        except:
            continue
    else:
        unprocessed_instructions.append(i)


# fonction pour le shift
def shift(inputkey, direction, value: int, outputkey):
    # vérifie que le cable d'origine a une valeur à shifter
    if inputkey in wires and wires[inputkey] is not None:
        if direction == "LSHIFT":
            outputvalue = wires[inputkey] << value
        elif direction == "RSHIFT":
            outputvalue = wires[inputkey] >> value
        wires[outputkey] = outputvalue
        return True
    return False


def and_or(input1, andor, input2, output):
    if (
        input1 in wires
        and wires[input1] is not None
        and input2 in wires
        and wires[input2] is not None
    ):
        if andor == "AND":
            outputvalue = wires[input1] & wires[input2]
        if andor == "OR":
            outputvalue = wires[input1] | wires[input2]
        wires[output] = outputvalue
        return True

    elif (
        input1 == "1"
        and andor == "AND"
        and input2 in wires
        and wires[input2] is not None
    ):
        outputvalue = 1 & wires[input2]
        wires[output] = outputvalue
        return True

    return False


def NOT(inputwire, outputwire):
    if inputwire in wires and wires[inputwire] is not None:
        wires[outputwire] = ~wires[inputwire]
        return True
    return False


# identifie les prochaines instrctions utilisables (celles dont la valeur numérique
# a été attibuée => c = 0 et b = 1674)
while unprocessed_instructions:
    i = 0
    while i < len(unprocessed_instructions):
        instr = unprocessed_instructions[i]

        if "RSHIFT" in instr or "LSHIFT" in instr:
            inputkey, direction, value, outputkey = (
                instr[0],
                instr[1],
                int(instr[2]),
                instr[-1],
            )
            if shift(inputkey, direction, value, outputkey):
                unprocessed_instructions.pop(i)
            else:
                i += 1

        elif "AND" in instr or "OR" in instr:
            input1, andor, input2, output = instr[0], instr[1], instr[2], instr[-1]
            if and_or(input1, andor, input2, output):
                unprocessed_instructions.pop(i)
            else:
                i += 1

        elif "NOT" in instr:
            inputwire, outputwire = instr[1], instr[-1]
            if NOT(inputwire, outputwire):
                unprocessed_instructions.pop(i)
            else:
                i += 1
        if i < len(unprocessed_instructions) and unprocessed_instructions[i] == instr:
            i += 1

for key, values in wires.items():
    print(key, values)

print(len(unprocessed_instructions))
