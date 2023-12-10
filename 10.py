from collections import deque

# filename = '10.test.txt'
filename = '10.txt'

grid = []

with open(filename, 'r') as f:
    for line in f:
        grid.append(list(line.strip()))

def starting_coordinate(grid):
    for i, row in enumerate(grid):
        for j, column in enumerate(row):
            if column == 'S':
                return i, j

start = starting_coordinate(grid)

visited = {start}
queue = deque()
queue.append(start)

def add_node(node):
    visited.add(node)
    queue.append(node)

# BFS flood from starting position
while queue:
    i, j = queue.popleft()
    pipe = grid[i][j]

    # Up: next can receive current in S|7F, current can go up in S|JL
    if i > 0 and (i - 1, j,) not in visited and grid[i - 1][j] in "S|7F" and pipe in "S|JL":
        add_node((i - 1, j,))

    # Down: next can receive current in S|JL, current can go down in S|7F
    if i < len(grid) - 1 and (i + 1, j,) not in visited and grid[i + 1][j] in "S|JL" and pipe in "S|7F":
        add_node((i + 1, j,))

    # Left: next can receive current in S-FL, current can go left in S-7J
    if j > 0 and (i, j - 1,) not in visited and grid[i][j - 1] in "S-FL" and pipe in "S-7J":
        add_node((i, j - 1,))

    # Right: next can receive current in S-7J, current can go right in S-FL
    if j < len(grid[i]) - 1 and (i, j + 1,) not in visited and grid[i][j + 1] in "S-7J" and pipe in "S-FL":
        add_node((i, j + 1,))

# Half-way point is farthest from S
print(len(visited) // 2)
