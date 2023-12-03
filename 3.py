from collections import defaultdict
import re

# filename = '3.test.txt'
filename =  '3.txt'

regex = '(\d+)'
pattern = re.compile(regex)

numbers = defaultdict(list) # number to list of tuple; all places number exists: (grid line, start pos, end pos)
grid = []

with open(filename, 'r') as f:
    for i, line in enumerate(f):
        line = line.strip()
        if not line:
            continue

        grid.append(list(line))

        for match in re.finditer(pattern, line):
            numbers[match.groups()[0]].append((i, match.start(), match.end() - 1,))

valid = [] # not a set; duplicates are okay

def check_left(start, grid_line):
    left = start - 1
    if left > 0:
        left_ch = grid[grid_line][left]
        if not left_ch.isdigit() and left_ch != '.':
            return True
    return False

def check_right(end, grid_line):
    right = end + 1
    if right < len(grid[grid_line]):
        right_ch = grid[grid_line][right]
        if not right_ch.isdigit() and right_ch != '.':
            return True
    return False

def check_above(start, end, grid_line):
    if grid_line - 1 >= 0:
        for x in range(start - 1, end + 2):
            if x < 0 or x >= len(grid[grid_line - 1]):
                continue
            ch = grid[grid_line - 1][x]
            if not ch.isdigit() and ch != '.':
                return True
    return False

def check_below(start, end, grid_line):
    if grid_line + 1 < len(grid):
        for x in range(start - 1, end + 2):
            if x < 0 or x >= len(grid[grid_line + 1]):
                continue
            ch = grid[grid_line + 1][x]
            if not ch.isdigit() and ch != '.':
                return True
    return False

for num, locs in numbers.items():
    for grid_line, start, end in locs:
        if check_above(start, end, grid_line) or check_below(start, end, grid_line) or check_left(start, grid_line) or check_right(end, grid_line):
            valid.append(int(num))

print(sum(valid))
