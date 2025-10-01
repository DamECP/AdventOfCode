class Ingredient:
    def __init__(self, name, capacity, durability, flavor, texture, calories):
        self.name = name
        self.capacity = capacity
        self.durability = durability
        self.flavor = flavor
        self.texture = texture
        self.calories = calories

ingredients = []

with open('ex15.txt') as exercise:
    for line in exercise:
        line = line.replace('\n', '')
        name = line.split(":")[0]
        #print(name)
        elt = line.split(",")
        capacity = int(elt[0].split(" ")[-1])
        durability = int(elt[1].split(" ")[-1])
        flavor = int(elt[2].split(" ")[-1])
        texture = int(elt[3].split(" ")[-1])
        calories= int(elt[4].split(" ")[-1])

        ingredient = Ingredient(name, capacity, durability, flavor, texture, calories)
        ingredients.append(ingredient)

def combination_best_score(ingredient1, ingredient2):
    results = []
    totals = []
    for i in range(101):
        j = 100 - i
        capacity = ingredient1.capacity * i + ingredient2.capacity*j
        durability = ingredient1.durability*i + ingredient2.durability*j
        flavor = ingredient1.flavor*i + ingredient2.flavor*j
        texture = ingredient1.texture*i + ingredient2.texture*j
        characteristics = [capacity, durability, flavor, texture]

        #print(f"{ingredient1.name} + {ingredient2.name} = {characteristics}")

        total = 1
        for i in characteristics:
            total *=i

        totals.append(total)

    print(totals)



combination_best_score(ingredients[2], ingredients[3])
"""
for i in ingredients:
    print(i.name, i.calories, i.capacity, i.flavor, i.texture, i.calories)
"""

for n, i in enumerate(ingredients):
    for j in ingredients[n+1:]:
        print(i.name, j.name)
        combination_best_score(i,j)