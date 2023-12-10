from collections import deque

# filename = '10-2-2.test.txt'
filename = '10.txt'

grid = []

with open(filename, 'r') as f:
    for line in f:
        grid.append(list(line.strip()))

def replace_start(i, j, grid):
    # Replace the start tile with its real value in order for the flip logic to work:
    up = i > 0 and grid[i - 1][j] in "|7F"
    down = i < len(grid) - 1 and grid[i + 1][j] in "|JL"
    left = j > 0 and grid[i][j - 1] in "-FL"
    right = j < len(grid[0]) - 1 and grid[i][j + 1] in "-7J"

    if up and down:
        return "|"
    if left and right:
        return "-"
    if left and down:
        return "7"
    if right and down:
        return "F"
    if left and up:
        return "J"
    if right and up:
        return "L"

def starting_coordinate(grid):
    for i, row in enumerate(grid):
        for j, column in enumerate(row):
            if column == 'S':
                grid[i][j] = replace_start(i, j, grid)
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

count = 0
for i in range(len(grid)):
    in_loop = False
    for j in range(len(grid[0])):
        # visited nodes are the loop nodes only:
        if (i, j,) in visited:
            # Someone online said we should only flip if we have a loop tile going up
            # (or down, but only check one or the other); this represents a transition
            # in the flow of the loop:
            #   https://www.reddit.com/r/adventofcode/comments/18ey1s7/comment/kcr1jga/
            if grid[i][j] in "|JL":
                in_loop = not in_loop
            continue
        if in_loop:
            count += 1
print(count)
