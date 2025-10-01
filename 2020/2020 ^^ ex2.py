with open('ex2.txt') as exercise:
    total_counter = 0
    wrong_counter = 0
    ok_counter = 0
    for line in exercise:
        total_counter += 1
        line = line.replace('\n', '')
        elt = line.split(" ")
        n1, n2 = elt[0].split("-")
        n1, n2 = int(n1), int(n2)
        ref = elt[1][0]
        word = elt[2]

        if word[n1-1] == ref:
            if word[n2-1] != ref:
                ok_counter +=1
        elif word[n2-1] == ref:
            if word[n1-1] != ref:
                ok_counter +=1

    print(ok_counter)