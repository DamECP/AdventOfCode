with open("ex1.txt") as exercise:
    calories_all = []
    calories = 0
    for line in exercise:
        if len(line) > 2:
            line = line.replace("\n", "")
            calories += int(line)
        else:
            calories_all.append(calories)
            calories = 0

print(max(calories_all))
print(sum(sorted(calories_all)[-3:]))
