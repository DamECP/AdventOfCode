with open("ex5.txt") as exercise:
    data = exercise.read()
    data = [int(i.strip()) for i in data.split(",")]


def opcode1(par1, par2, data: list, par3) -> list:
    n3 = data[par1] + data[par2]
    data[par3] = n3
    return data


def opcode2(par1, par2, data: list, par3) -> list:
    n3 = data[par1] * data[par2]
    data[par3] = n3
    return data


def opcode3(input_, par1, data):
    data[par1] = input_
    return data


def opcode4(par1, data):
    output = data[par1]
    return output


def mode(one_or_two: int, n: int, data: list) -> int:
    if one_or_two == 0:
        return data[n]
    elif one_or_two == 1:
        return n


memorised_n = 1
for i, elt in enumerate(data):
    par1, par2, output = (
        data[i + 1],
        data[i + 2],
        data[i + 3],
    )
    if elt == 1:
        data = opcode1(par1, par2, data, par3)
    elif elt == 2:
        data = opcode2(par1, par2, data, par3)
    elif elt == 3:
        data = opcode3(start, par1, data)
    elif elt == 4:
        memorised_n = opcode4(par1)

    if str(elt[0]) != "-" and len(str(elt)) == 4:
        op, mod1, mod2 = (
            str(elt[-1]),
            str(elt[-3]),
            str(elt[-4]),
        )
        if op == 1:
            data = opcode1(par1, par2, data, par3)
        elif op == 2:
            data = opcode2(par1, par2, data, par3)
        elif op == 3:
            data = opcode3(start, par1, data)
        elif op == 4:
            memorised_n = opcode4(par1)
