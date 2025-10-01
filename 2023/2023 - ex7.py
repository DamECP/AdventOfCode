with open("ex7.txt") as exercise:
    data = exercise.readlines()
    data = [i.strip() for i in data]


class Hand:
    def __init__(self, hand, bid):
        self.hand = hand
        self.bid = int(bid)
        self.type = self.type_of_hand()
        self.value = self.score()

    def type_of_hand(self):
        groups = [self.hand.count(i) for i in set(self.hand)]
        return sorted(groups, reverse=True)

    def score(self):
        card_values = {
            "2": 2,
            "3": 3,
            "4": 4,
            "5": 5,
            "6": 6,
            "7": 7,
            "8": 8,
            "9": 9,
            "T": 10,
            "J": 11,
            "Q": 12,
            "K": 13,
            "A": 14,
        }
        return sum(card_values[i] * self.hand.count(i) for i in set(self.hand))


for line in data:
    cards, bid = line.split(" ")
    hand = Hand(cards, bid)

    print(cards)
    print(hand.type_of_hand())
    print(hand.value)
    print()
