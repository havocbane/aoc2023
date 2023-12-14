from typing import List

# filename = '14.test.txt'
filename = '14.txt'

grid: List[List[str]] = []

with open(filename, 'r') as f:
    for line in f:
        line = line.strip()
        grid.append(list(line))

def slide_grid_north(grid) -> List[List[str]]:
    width = len(grid[0])
    columns = list(map(list, zip(*grid)))
    for column in columns:
        i = 0
        while i < width - 1:
            if column[i] == '.':
                j = i + 1
                while j < width - 1 and column[j] == '.':
                    j += 1
                if column[j] == 'O':
                    column[i] = 'O'
                    column[j] = '.'
            i += 1
    return list(map(list, zip(*columns)))

rolled_north = slide_grid_north(grid)

def score(grid) -> int:
    s = 0
    height = len(grid)
    width = len(grid[0])
    for x in range(height):
        for y in range(width):
            if grid[x][y] == 'O':
                s += height - x
    return s

print(score(rolled_north))
