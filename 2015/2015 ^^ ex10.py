with open("ex10.txt") as exercise:
    for line in exercise:
        line = line.replace("\n", "")

test = "1321131112"


def number_counter(test):
    new_str = []
    i = 0
    while True:
        counter = 1
        try:
            while test[i] == test[i + 1]:
                counter += 1
                i += 1

            piece = str(counter) + test[i]
            new_str.append(piece)

            i += 1

        except IndexError:
            new_str += str(counter) + test[i]
            break

    return "".join(i for i in new_str)


for i in range(50):
    print(i)
    answer = number_counter(test)
    test = answer
print(len(test))
