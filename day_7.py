from collections import Counter
from utils.read_input import read_input


def convert_card_to_int(card, use_jokers=False):
    if card == 'A':
        return 14
    elif card == 'K':
        return 13
    elif card == 'Q':
        return 12
    elif card == 'J':
        return 1 if use_jokers else 11
    elif card == 'T':
        return 10
    else:
        return int(card)


class Hand:
    def __init__(self, cards, bid, use_jokers=False):
        self.cards = [convert_card_to_int(card, use_jokers) for card in cards]
        self.bid = bid
        self.val_counts = None
        self._result = None
        self._use_jokers = use_jokers

    def get_result(self):
        if self._result is not None:
            return self._result
        
        self.val_counts = Counter(self.cards)
        is_five_of_a_kind = False
        is_four_of_a_kind = False
        is_three_of_a_kind = False
        num_pairs = 0
        joker_count = 0
        for val, count in self.val_counts.most_common():
            if self._use_jokers and val == 1:
                joker_count = count
            elif count == 5:
                is_five_of_a_kind = True
            elif count == 4:
                is_four_of_a_kind = True
            elif count == 3:
                is_three_of_a_kind = True
            elif count == 2:
                num_pairs += 1
        
        # 6 = 5 of a kind
        # 5 = 4 of a kind
        # 4 = full house
        # 3 = 3 of a kind
        # 2 = 2 pairs
        # 1 = 1 pair
        # 0 = high card
        if is_five_of_a_kind:
            self._result = 6
        
        elif is_four_of_a_kind:
            if joker_count == 1:
                self._result = 6
            else:
                self._result = 5
        
        elif is_three_of_a_kind:
            if num_pairs > 0:
                self._result = 4
            elif joker_count == 2:
                self._result = 6 # 2 jokers + 3 of a kind
            elif joker_count == 1:
                self._result = 5 # 1 joker + 3 of a kind
            else:
                self._result = 3
        
        elif num_pairs == 2:
            if joker_count == 1:
                self._result = 4
            else:
                self._result = 2
        
        elif num_pairs == 1:
            if joker_count == 3:
                self._result = 6
            elif joker_count == 2:
                self._result = 5
            elif joker_count == 1:
                self._result = 3
            else:
                self._result = 1
        
        # High card or only jokers
        elif joker_count == 5:
            self._result = 6
        elif joker_count == 4:
            self._result = 6 # 4 jokers + 1 card
        elif joker_count == 3:
            self._result = 5 # 3 jokers + 1 card
        elif joker_count == 2:
            self._result = 3 # 2 jokers + 1 card
        elif joker_count == 1:
            self._result = 1 # 1 joker + 1 card
        else:
            self._result = 0

        return self._result

    def is_higher_hand(self, other_hand):
        for i in range(len(self.cards)):
            if self.cards[i] > other_hand.cards[i]:
                return True
            elif self.cards[i] < other_hand.cards[i]:
                return False

    def beats_hand(self, other_hand):
        """
        Get hand results first, if they're not equal we can use that, and if
        they are equal we can check the highest card instead
        """
        result_a = self.get_result()
        result_b = other_hand.get_result()
        if result_a == result_b:
            result = self.is_higher_hand(other_hand)
        else:
            result = result_a > result_b

        return result
    

    def __lt__(self, other):
        return self.beats_hand(other)


def solve_part_1(all_cards, all_bids):
    total = 0
    hands = []
    for cards, bids in zip(all_cards, all_bids):
        hand = Hand(cards, bids)
        hands.append(hand)
    
    for rank, hand in enumerate(sorted(hands, reverse=True), 1):
            total += rank * hand.bid
    
    print(f"Part 1: {total}")


def solve_part_2(all_cards, all_bids):
    """Treat J as jokers"""
    total = 0
    hands = []
    for cards, bids in zip(all_cards, all_bids):
        hand = Hand(cards, bids, use_jokers=True)
        hands.append(hand)
    
    for rank, hand in enumerate(sorted(hands, reverse=True), 1):
            total += rank * hand.bid
    
    print(f"Part 2: {total}")


if __name__ == "__main__":
    input_data = read_input("ac7.txt")
    all_cards = [line.split()[0] for line in input_data] 
    all_bids = [int(line.split()[1]) for line in input_data] 

    # solve_part_1(all_cards, all_bids)
    solve_part_2(all_cards, all_bids)
