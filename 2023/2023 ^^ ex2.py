ok_games = []
redlimit = 12
greenlimit = 13
bluelimit = 14
power = 0

with open("ex2.txt") as exercise:
    for line in exercise:
        # print(line)
        line = line.replace("\n", "")
        line = line.replace(",", "")
        line = line.split(";")
        game = line[0].split(":")[0]
        game = int(game.split(" ")[-1])
        print(game)
        line[0] = line[0].split(":")[1]

        red = []
        green = []
        blue = []

        for i in line:
            tirage = i.strip()
            tirage = tirage.split()
            for index, elt in enumerate(tirage):
                if elt == "red":
                    red.append(int(tirage[index - 1]))
                elif elt == "green":
                    green.append(int(tirage[index - 1]))
                elif elt == "blue":
                    blue.append(int(tirage[index - 1]))

        print(red, blue, green)

        power += max(red) * max(green) * max(blue)

        # if max(red) <= redlimit and max(green) <= greenlimit and max(blue) <= bluelimit:
        #    ok_games.append(game)

# print(sum(ok_games))

print(power)
