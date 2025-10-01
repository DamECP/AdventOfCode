"""Part 1

def counter(n):
    score = 1
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        for i in range(n - 1):
            score *= 2
    return score

with open("ex4.txt") as exercise:
    score = 0
    for line in exercise:
        line = line.strip()
        card_number, card_content = line.split(":")

        winning_numbers, player_numbers = card_content.split("|")

        winning_numbers = {i for i in winning_numbers.split(" ") if i != ""}

        player_numbers = {i for i in player_numbers.split(" ") if i != ""}

        ans = winning_numbers & player_numbers

        score += counter(len(ans))

print(score)
"""

with open("ex4.txt") as exercise:
    cards = {}
    n = 1
    for line in exercise:
        line = line.strip()
        cards[n] = [line, 1]  # id of card = content, item (1ex for the moment)
        n += 1


for id_, card in cards.items():

    for repetition in range(
        card[1]
    ):  # repeats the operation according to the number of cards there is

        # print(f"Carte : {card}")

        card_number, card_content = card[0].split(":")
        winning_numbers, player_numbers = card_content.split("|")
        winning_numbers = {i for i in winning_numbers.split(" ") if i != ""}
        player_numbers = {i for i in player_numbers.split(" ") if i != ""}

        ans = len(winning_numbers & player_numbers)

        for n in range(1, ans + 1):
            cards[id_ + n][1] += 1

    # print(card[0], card[1])

final_answer = 0
for value in cards.values():
    final_answer += value[1]

print(final_answer)
