from string import ascii_letters
from collections import Counter
import heapq
from itertools import cycle

real_rooms = []

with open("ex4.txt") as exercise:
    result = 0
    for line in exercise:
        room = line
        data = {}
        line = line.replace("\n", "")
        line = line.split("-")
        strings = "".join(line[:-1])
        key = (line[-1].split("["))[1][:-1]
        n = int((line[-1].split("["))[0])

        data = dict(Counter(strings))
        sorted_dict = dict(sorted(data.items()))

        top5 = heapq.nlargest(5, sorted_dict, key=sorted_dict.get)

        if "".join(top5) == key:
            result += n
            real_rooms.append(room)

import string

cesar = {}

for i in range(26):
    cesar[string.ascii_lowercase[i]] = i

reverse_cesar = {v: k for k, v in cesar.items()}


def cesar_decrytp(test, key):
    new_text = ""
    for char in test:
        if char == "-":
            new_text += " "
        elif char.lower() in cesar:
            new_index = (cesar[char] + key) % 26
            new_text += reverse_cesar[new_index]
    return new_text


test = ["qzmt-zixmtkozy-ivhz-343"]

for i in real_rooms:
    key = int(i[-11:-8])
    message = cesar_decrytp(i, key)
    if message.count("pole") == 1:
        print(key, message)
