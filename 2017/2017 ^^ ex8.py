import operator

with open("ex8.txt") as exercise:
    data = [i.strip() for i in exercise.readlines()]

part_2 = 0

registers = {}
operators = {
    "==": operator.eq,
    "!=": operator.ne,
    ">": operator.gt,
    "<": operator.lt,
    ">=": operator.ge,
    "<=": operator.le,
    "inc": operator.add,
    "dec": operator.sub,
}


for i in data:
    instruction = i.split(" ")
    print(instruction)
    mod_reg, ref_reg = instruction[0], instruction[-3]
    op_nb, comp_nb = int(instruction[2]), int(instruction[-1])
    op, comp = operators[instruction[1]], operators[instruction[-2]]

    for reg in (mod_reg, ref_reg):
        if reg not in registers:
            registers[reg] = 0

    if comp(registers[ref_reg], comp_nb):
        result = op(registers[mod_reg], op_nb)
        registers[mod_reg] = result
        if result > part_2:
            part_2 = result


# part1
print(max(registers.values()))

print(part_2)
