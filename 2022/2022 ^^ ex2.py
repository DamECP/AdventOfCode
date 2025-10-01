score = 0
draw = [
    ["A", "rock"],
    ["B", "paper"],
    ["C", "scissor"],
]
lose = [["A", "scissor"], ["B", "rock"], ["C", "paper"]]
win = [["A", "paper"], ["B", "scissor"], ["C", "rock"]]

with open("ex2.txt") as exercise:
    for line in exercise:
        line = line.replace("\n", "")
        line = line.split(" ")

        choice = None

        if line[1] == "Y":
            score += 3
            for i in draw:
                if i[0] == line[0]:
                    choice = i[1]

        elif line[1] == "X":
            for i in lose:
                if i[0] == line[0]:
                    choice = i[1]

        elif line[1] == "Z":
            score += 6
            for i in win:
                if i[0] == line[0]:
                    choice = i[1]

        if choice == "rock":
            score += 1
        elif choice == "paper":
            score += 2
        elif choice == "scissor":
            score += 3

print(score)
