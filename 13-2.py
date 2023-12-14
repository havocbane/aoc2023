from collections import Counter

# filename = '13.test.txt'
filename = '13.txt'

grids = []

with open(filename, 'r') as f:
    grid = []
    for line in f:
        if not line.strip():
            grids.append(grid)
            grid = []
            continue
        grid.append(list(line.strip()))
    grids.append(grid)

def diff_lines(left, right):
    return sum([
        1 for x in range(len(left))
        if left[x] != right[x]
    ])

def find_reflection(grid):
    for x in range(len(grid) - 1):
        left = grid[:x + 1]
        left.reverse()
        right = grid[x + 1:]

        max_c = min(len(left), len(right))
        diff_counts = Counter(
            diff_lines(left[y], right[y])
            for y in range(max_c)
        )
        if diff_counts[1] == 1 and set(diff_counts.keys()) - {0, 1} == set():
            assert diff_counts[0] + diff_counts[1] == max_c, diff_counts
            return x + 1
    return -1

r_ct = c_ct = 0
for grid in grids:
    rows_before = find_reflection(grid)
    if rows_before != -1:
        r_ct += rows_before
    else:
        columns = list(zip(*grid))
        cols_before = find_reflection(columns)
        if cols_before != -1:
            c_ct += cols_before
print(c_ct + 100 * r_ct)
