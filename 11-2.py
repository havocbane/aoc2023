import itertools
import math
from pprint import pprint

# filename = '11.test.txt'
filename = '11.txt'

grid = None
with open(filename, 'r') as f:
    grid = [
        [
            ch for ch in line.strip()
        ]
        for line in f
    ]

expanded = []
rows_added = set()
for x in range(len(grid)):
    expanded.append(grid[x])
    if all([ch == '.' for ch in grid[x]]):
        rows_added.add(x)
        row = ['.' for _ in range(len(grid[0]))]
        expanded.append(grid[x])

columns_added = set()
for y in range(len(grid[0])):
    column = [
        grid[x][y]
        for x in range(len(grid))
    ]
    if all([ch == '.' for ch in column]):
        columns_added.add(y)

galaxies = []
for i in range(len(grid)):
    for j in range(len(grid[0])):
        vertex = (i, j,)
        if grid[i][j] == "#":
            galaxies.append(vertex)

def manhattan(x, y):
    return abs(x[0] - y[0]) + abs(x[1] - y[1])

s = 0
for i, j in itertools.combinations(galaxies, 2):
    s += manhattan(i, j)

    # Find all empty rows and columns between our points and then
    # pretend like we expanded them by just adding the expansion value
    # which would be the extra steps in each direction we would need to go:

    if i[0] < j[0]:
        row_diff = range(i[0], j[0])
    else:
        row_diff = range(j[0], i[0])
    for r in row_diff:
        if r in rows_added:
            s += 999999

    if i[1] < j[1]:
        col_diff = range(i[1], j[1])
    else:
        col_diff = range(j[1], i[1])
    for c in col_diff:
        if c in columns_added:
            s += 999999
print(s)
