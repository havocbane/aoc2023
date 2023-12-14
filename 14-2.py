# cache intermediate solutions as we rotate so we don't have to re-roll if we're hitting a cycle
from functools import cache
from typing import List

# filename = '14.test.txt'
filename = '14.txt'

grid: List[List[str]] = []

with open(filename, 'r') as f:
    for line in f:
        line = line.strip()
        grid.append(list(line))

def rotate_counter_clockwise(grid):
    height = len(grid)
    width = len(grid[0])
    return [
        [
            grid[j][i]
            for j in range(height)
        ]
        for i in range(width - 1, -1, -1)
    ]

# We have to convert to string for caching since LRU cache keys have to be hashable:
def to_string(grid: List[List[str]]) -> str:
    height = len(grid)
    result = ""
    for row in range(height):
        result += "".join(grid[row])
        result += "\n"
    return result

@cache
def from_string(grid) -> List[List[str]]:
    return [
        list(line)
        for line in grid.split()
    ]

@cache
def slide_grid_north(grid: str) -> List[List[str]]:
    grid = from_string(grid)
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

@cache
def slide_grid_east(grid: str):
    # East: rotate once counter clockwise, slide north, then rotate back three times counter clockwise
    grid = from_string(grid)
    grid = rotate_counter_clockwise(grid)

    grid = to_string(grid)
    grid = slide_grid_north(grid)

    for _ in range(3):
        grid = rotate_counter_clockwise(grid)
    return grid

@cache
def slide_grid_west(grid: str):
    grid = from_string(grid)
    # West: rotate three times counter clockwise, slide north, then rotate back once counter clockwise
    for _ in range(3):
        grid = rotate_counter_clockwise(grid)

    grid = to_string(grid)
    grid = slide_grid_north(grid)

    grid = rotate_counter_clockwise(grid)
    return grid

@cache
def slide_grid_south(grid: str):
    grid = from_string(grid)
    # South: rotate two times counter clockwise, slide north, then rotate back twice counter clockwise
    for _ in range(2):
        grid = rotate_counter_clockwise(grid)

    grid = to_string(grid)
    grid = slide_grid_north(grid)

    for _ in range(2):
        grid = rotate_counter_clockwise(grid)
    return grid

# Score is the same as part 1 (north railing only)
def score(grid) -> int:
    s = 0
    height = len(grid)
    width = len(grid[0])
    for x in range(height):
        for y in range(width):
            if grid[x][y] == 'O':
                s += height - x
    return s

def main(grid) -> str:
    # 1 cycle is tilt N, then W, then S, then E in order
    cycles = 1000000000
    seen = list()
    for c in range(cycles):
        grid = to_string(grid)
        grid = slide_grid_north(grid)

        grid = to_string(grid)
        grid = slide_grid_west(grid)

        grid = to_string(grid)
        grid = slide_grid_south(grid)

        grid = to_string(grid)
        grid = slide_grid_east(grid)

        # Cycle detection; our answer is the offset into the cycle
        grid_str = to_string(grid)
        if grid_str in seen:
            start_of_cycle = seen.index(grid_str)
            cycle = seen[start_of_cycle:]
            len_cycle = len(cycle)
            loc = (cycles - c) % len_cycle - 1
            grid = cycle[loc]
            break

        seen.append(grid_str)
    return grid

print(score(from_string(main(grid))))

# time python 14-2.py
# 97241
# python 14-2.py  0.87s user 0.12s system 80% cpu 1.237 total
