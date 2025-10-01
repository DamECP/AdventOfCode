with open("ex9test_v2.txt") as exercise:
    for line in exercise.readlines()[3]:
        line = line.replace("\n", "")

        def builder(line):
            # part_1
            copy = []  # stocke la chaine modifiée

            i = 0
            while i < len(line):  # boucle en for pour maitriser l'index en cours
                char = line[i]

                if char != "(":  # on avance jusqu'à croiser une décompression
                    copy.append(char)
                    i += 1

                else:
                    current = line[i:]  # chaine à partir du début de la parenthèse
                    index_x = current.find("x")
                    section = int(
                        current[1:index_x]
                    )  # extrait le nombre de caractères à multiplier
                    index_closing = current.find(")")
                    repetition = int(
                        current[index_x + 1 : index_closing]
                    )  # extrait le nb d'itération attendu
                    substring = current[
                        index_closing + 1 : index_closing + 1 + section
                    ]  # crée la substring répétée
                    for _ in range(repetition):
                        copy.append(substring)
                    i += (
                        index_closing + 1 + section
                    )  # reprend la boucle au caractère suivant la substring

            result = "".join(copy)
            print(result, len(result))


"""
with open("ex9.txt") as exercise:
    for line in exercise.readlines():
        test = line.replace("\n", "")
        print(test)

        monitor = 0
        while "(" in test:

            beginning = test[: test.find("(")]
            # print(beginning)

            # print(test)
            instructions = test[test.find("(") + 1 : test.find(")")]
            # print("instructions =>", instructions)
            len_sequence, repetitions = [int(i) for i in instructions.split("x")]

            start = test.find(")") + 1
            substring = test[start : start + len_sequence]
            remainder = test[start + len_sequence :]

            new_string = substring * repetitions
            test = beginning + new_string + remainder
            # print()
            monitor += 1

            print(monitor)
        print("Résultat", len(test))
"""
# programme trop long à cause des str en mémoire, faire une récursion en ne prenant en compte que la longueur sans construire chaque séquence


def decompress(test, start=0, end=None):
    if end is None:
        end = len(test)

    i = start
    total_len = 0

    while i < end:
        if test[i] == "(":

            closed_bracket = test.find(")", i)
            instructions = test[i + 1 : closed_bracket]
            len_sequence, repetitions = [int(i) for i in instructions.split("x")]

            substring_start = closed_bracket + 1
            substring_end = substring_start + len_sequence

            # récursion
            segment_length = decompress(test, substring_start, substring_end)

            total_len += segment_length * repetitions

            # Saute à la prochaine consigne
            i = substring_end

        else:
            # chaque caractère intérmédiaire != "("
            total_len += 1
            i += 1

    return total_len


with open("ex9.txt") as exercise:
    for line in exercise.readlines():
        test = line.replace("\n", "")

print(decompress(test))
