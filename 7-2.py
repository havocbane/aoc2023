from collections import Counter, defaultdict
from functools import cmp_to_key, partial
from typing import Dict, List, Tuple

# filename = '7.test.txt'
filename = '7.txt'

card_value = {
    'A': 14,
    'K': 13,
    'Q': 12,
    'J': 1,
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
    counts = Counter(hand[0])
    j_count = counts.get('J', 0)
    del counts['J']

    def check(check_against, count):
        if count == check_against:
            return True
        if j_count > 0:
            for j in range(1, j_count + 1):
                if count + j == check_against:
                    return True
        return False

    def is_five_of_a_kind():
        if hand[0] == 'JJJJJ':
            return True
        check_fn = partial(check, 5)
        return any(map(check_fn, counts.values()))

    def is_four_of_a_kind():
        check_fn = partial(check, 4)
        return any(map(check_fn, counts.values()))

    def is_full_house():
        full_house = all(map(lambda count: count in (2, 3), counts.values()))
        if full_house:
            return True
        if j_count > 0:
            # We only need to consider one case here because more jacks would have matched already
            if len(list(filter(lambda count: count == 2, counts.values()))) >= 2:
                return True
        return False

    def is_three_of_a_kind():
        check_fn = partial(check, 3)
        return any(map(check_fn, counts.values()))

    def is_two_pair():
        # Any pairs with jacks would have already matched something else; just check for real two-pairs
        return len(list(filter(lambda count: count == 2, counts.values()))) >= 2

    def is_pair():
        # If we have any Jacks, then we always have at least a pair (ABCDJ) -> (AABCD)
        return any(map(lambda count: count == 2, counts.values())) or j_count > 0

    if is_five_of_a_kind():
        return '5-kind'
    elif is_four_of_a_kind():
        return '4-kind'
    elif is_full_house():
        return 'full-house'
    elif is_three_of_a_kind():
        return '3-kind'
    elif is_two_pair():
        return '2-pair'
    elif is_pair():
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
