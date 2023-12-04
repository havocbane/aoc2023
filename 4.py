# filename = '4.test.txt'
filename = '4.txt'

card_values = []
with open(filename, 'r') as f:
    for line in f:
        line = line.strip()
        winning_numbers, your_numbers = line.split('|')
        winning_numbers = set(winning_numbers.split(':')[1].split())
        your_numbers = set(your_numbers.split())

        value = 0
        for your_number in your_numbers:
            if your_number in winning_numbers:
                if value > 0:
                    value *= 2
                else:
                    value = 1
        if value > 0:
            card_values.append(value)

print(sum(card_values))
