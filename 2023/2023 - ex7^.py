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
        return [card_values.get(i) for i in self.hand]

    def get_poker_score(self) -> int:
        hand = self.type_of_hand()
        if 5 in hand:
            return 7
        elif 4 in hand:
            return 6
        elif 3 in hand:
            if 2 in hand:
                return 5
            else:
                return 4
        elif 2 in hand:
            if hand.count(2) == 2:
                return 3
            else:
                return 2
        else:
            return 1

    def __repr__(self):
        return self.hand


all_hands = []
with open("ex7.txt") as exercise:
    data = exercise.readlines()
    data = [i.strip() for i in data]
    for card in data:
        hand, bid = card.split(" ")
        hand = Hand(hand, bid)
        all_hands.append(hand)


def sort_by_poker(hands: list[Hand]):
    sorted_by_poker = {
        i: [hand for hand in hands if hand.get_poker_score() == i] for i in range(1, 8)
    }
    return sorted_by_poker


def same_poker_sorter(hands: list[Hand]):
    return sorted(hands, key=lambda h: h.value)


hands_by_poker = sort_by_poker(all_hands)

part1_sort = []
for key, value in hands_by_poker.items():
    for hand in same_poker_sorter(value):
        part1_sort.append(hand)

part1_score = 0
for multiplier, hand in enumerate(part1_sort, 1):
    hand: Hand
    part1_score += multiplier * hand.bid

print(part1_score)
