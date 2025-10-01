with open("ex6test.txt") as exercise:
    data = exercise.readlines()
    data = [i.strip() for i in data]

orbits = {}
for elt in data:
    key, value = elt.split(")")
    if key not in orbits.keys():
        orbits[key] = [value]
    else:
        orbits[key].append(value)

print(orbits)
