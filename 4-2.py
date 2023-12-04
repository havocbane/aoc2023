from collections import defaultdict

# filename = '4.test.txt'
filename = '4.txt'

cards = defaultdict(list)
with open(filename, 'r') as f:
    for line in f:
        line = line.strip()
        winning_numbers, your_numbers = line.split('|')
        card_num = winning_numbers.split(':')[0].split('Card')[1].strip()
        winning_numbers = set(winning_numbers.split(':')[1].split())
        your_numbers = set(your_numbers.split())
        cards[card_num].append((winning_numbers, your_numbers,))

card_num = int(card_num)

i = 1
while i <= card_num:
    current = str(i)
    card_copies = cards[current]
    for card_copy in card_copies:
        winning_numbers, your_numbers = card_copy[0], card_copy[1]
        winners = 0
        for your_number in your_numbers:
            if your_number in winning_numbers:
                winners += 1
        if winners > 0:
            copies_won = range(i + 1, i + winners + 1)
            for copy in copies_won:
                copy_num = str(copy)
                cards[copy_num].append(cards[copy_num][0])
    i += 1

total = 0
for v in cards.values():
    total += len(v)
print(total)
