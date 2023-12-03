from collections import defaultdict
import re

# filename = '3.test.txt'
filename =  '3.txt'

regex = '(\d+)'
gear_regex = '\*'
pattern = re.compile(regex)
gear_pattern = re.compile(gear_regex)

numbers = defaultdict(list) # grid_line to list of tuple; all places number exists: (number, start pos, end pos)
gears = []
grid = []

with open(filename, 'r') as f:
    for i, line in enumerate(f):
        line = line.strip()
        if not line:
            continue

        grid.append(list(line))

        for match in re.finditer(pattern, line):
            numbers[i].append((match.groups()[0], match.start(), match.end() - 1,))

        for gear_match in re.finditer(gear_pattern, line):
            gears.append((i, gear_match.start(),))

valid = []
for gear_grid_line, gear_pos in gears:
    count = 0

    left = gear_pos - 1
    right = gear_pos + 1

    gear_numbers = []
    if gear_grid_line in numbers:
        for num, start, end in numbers[gear_grid_line]:
            if left == end or right == start:
                count += 1
                gear_numbers.append(int(num))

    if gear_grid_line - 1 in numbers:
        for num, start, end in numbers[gear_grid_line - 1]:
            r = range(start, end + 1)
            if any([left in r, gear_pos in r, right in r]):
                count += 1
                gear_numbers.append(int(num))

    if gear_grid_line + 1 in numbers:
        for num, start, end in numbers[gear_grid_line + 1]:
            r = range(start, end + 1)
            if any([left in r, gear_pos in r, right in r]):
                count += 1
                gear_numbers.append(int(num))

    if count == 2:
        valid.append(gear_numbers[0] * gear_numbers[1])

print(sum(valid))
