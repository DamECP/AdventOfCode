total_fuel = []

with open("ex1.txt") as exercise:
    for line in exercise:
        line = line.replace("\n", "")
        fuel = int(line)

        while fuel > 0:
            fuel = fuel // 3 - 2
            if fuel > 0:
                total_fuel.append(fuel)

print(sum(total_fuel))
