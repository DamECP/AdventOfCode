import re
import string

with open("ex5.txt") as exercise:
    words = []
    for line in exercise:
        line = line.replace("\n", "")
        words.append(line)

nice = []


def vowels(word):
    vowels = r"[aeiou]"
    if len(re.findall(vowels, word)) >= 3:
        return word


def doubles_with_space(word):
    regex = r"([a-z]).\1"
    if re.findall(regex, word):
        return True


def forbidden(word):

    forbidden = ["ab", "cd", "pq", "xy"]
    for item in forbidden:
        if item in word:
            return None
    return word


def doubles(word):
    seen_pairs = {}

    for i in range(len(word) - 1):
        pair = word[i : i + 2]

        if pair in seen_pairs and seen_pairs[pair] < i - 1:
            return True

        seen_pairs[pair] = i

    return False


counter = 0
for word in words:
    if doubles(word) and doubles_with_space(word):
        counter += 1

print(counter)
