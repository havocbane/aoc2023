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

def find_reflection(grid):
    odd = 1 if len(grid) % 2 == 1 else 0
    for x in range(len(grid) - 1):
        if grid[x] == grid[x + 1]:
            left = grid[:x + 1]
            left.reverse()
            right = grid[x + 1:]

            if len(left) > len(right):
                left = left[:len(right)]
            else:
                right = right[:len(left)]
            if left == right:
                return x + odd
    return -1

r_ct = c_ct = 0
for grid in grids:
    rows_before = find_reflection(grid)
    if rows_before == -1:
        columns = list(zip(*grid))
        cols_before = find_reflection(columns)
        if cols_before != -1:
            c_ct += cols_before
    else:
        r_ct += rows_before

print(c_ct + 100 * r_ct)
