from collections import Counter, defaultdict
from functools import cmp_to_key
from typing import Dict, List, Tuple

# filename = '7.test.txt'
filename = '7.txt'

card_value = {
    'A': 14,
    'K': 13,
    'Q': 12,
    'J': 11,
    'T': 10,
    **{str(x): x for x in range(2, 10)},
}

with open(filename, 'r') as f:
    hands_bids = {
        line.split()[0]: int(line.split()[1])
        for line in f
    }

hands: Dict[str, List[int]] = {
    hand: [
        card_value[card]
        for card in hand
    ]
    for hand in hands_bids.keys()
}

def hand_type(hand):
    def is_five_of_a_kind(test_hand):
        return len(set(test_hand)) == 1

    def is_four_of_a_kind(test_hand):
        counts = Counter(test_hand)
        return any(map(lambda count: count == 4, counts.values()))

    def is_full_house(test_card):
        counts = Counter(test_card)
        return all(map(lambda count: count in (2, 3), counts.values()))

    def is_three_of_a_kind(test_hand):
        counts = Counter(test_hand)
        return any(map(lambda count: count == 3, counts.values()))

    def is_two_pair(test_hand):
        counts = Counter(test_hand)
        return len(list(filter(lambda count: count == 2, counts.values()))) == 2

    def is_pair(test_hand):
        counts = Counter(test_hand)
        return any(map(lambda count: count == 2, counts.values()))

    if is_five_of_a_kind(hand[0]):
        return '5-kind'
    elif is_four_of_a_kind(hand[0]):
        return '4-kind'
    elif is_full_house(hand[0]):
        return 'full-house'
    elif is_three_of_a_kind(hand[0]):
        return '3-kind'
    elif is_two_pair(hand[0]):
        return '2-pair'
    elif is_pair(hand[0]):
        return '1-pair'
    return 'high-card'

def compare_hands(left: Tuple[str, List[int]], right) -> int:
    # -1, 0, 1 = less-than, equal, greater-than
    for i in range(5):
        if left[1][i] > right[1][i]:
            return 1
        if left[1][i] < right[1][i]:
            return -1
    return 0

# Note: I wanted to use itertools.groupby here, but it requires the items to be sorted already
groups = defaultdict(list)
for hand in hands.items():
    groups[hand_type(hand)].append(hand)

sorted_groups = {}
for group in groups.items():
    # group[0] is the hand type, group[1] is the list of hands (str: list of card values)
    sorted_group = sorted(group[1], key=cmp_to_key(compare_hands))
    sorted_groups[group[0]] = sorted_group

ordered_bids = [
    *[hands_bids[hand[0]] for hand in sorted_groups.get('high-card', [])],
    *[hands_bids[hand[0]] for hand in sorted_groups.get('1-pair', [])],
    *[hands_bids[hand[0]] for hand in sorted_groups.get('2-pair', [])],
    *[hands_bids[hand[0]] for hand in sorted_groups.get('3-kind', [])],
    *[hands_bids[hand[0]] for hand in sorted_groups.get('full-house', [])],
    *[hands_bids[hand[0]] for hand in sorted_groups.get('4-kind', [])],
    *[hands_bids[hand[0]] for hand in sorted_groups.get('5-kind', [])],
]
print(sum([
    i * bid
    for i, bid in enumerate(ordered_bids, start=1)
]))
