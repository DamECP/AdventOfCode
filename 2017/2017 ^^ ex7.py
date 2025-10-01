with open("ex7.txt") as exercise:
    data = [i.strip() for i in exercise.readlines()]


class Program:
    def __init__(self, name, weight=0):

        self.name = name
        self.weight = weight
        self.root = None
        self.children = []


programs = {}

for i in data:
    children = []
    i = i.split(" ")
    name, weight = i[0], int(i[1][1:-1])
    if name not in programs:
        programs[name] = Program(name, weight)
    programs[name].weight = weight
    if "->" in i:
        children = [elt.strip(",") for elt in i[3:]]
        programs[name].children = children
        for child in children:
            if child not in programs:
                programs[child] = Program(child)

# part 1
# print(set(children) ^ set(programs.keys()))
# children = [i.strip(",") for i in children]

for prog in programs.values():
    for checked in programs.values():
        if prog.name in checked.children:
            prog.root = checked

origin = [i for i in programs.values() if i.root is None][0]

all_programs = programs.values()


def get_total_weight(program):
    return program.weight + sum(
        get_total_weight(programs[child]) for child in program.children
    )


def print_tree(program, level=0):
    indent = "  " * level
    total = get_total_weight(program)
    print(f"{indent}{program.name} ({program.weight}) => total : {total})")
    for child in program.children:
        print_tree(programs[child], level + 1)


def get_unbalanced_line(program):
    child_weights = [get_total_weight(programs[child]) for child in program.children]
    if len(set(child_weights)) > 1:  # si plusieurs masses, alors déséquilibre
        print(
            programs[program.children[0]].weight,
            programs[program.children[0]].name,
            programs[program.children[0]].root.name,
        )
        print(
            f"Différenciel : {max(child_weights)-min(child_weights)} - {child_weights}"
        )

        for child in program.children:
            next_branche = programs[child]
            total_weight = get_total_weight(next_branche)

    for child in program.children:
        get_unbalanced_line(programs[child])


get_unbalanced_line(origin)
