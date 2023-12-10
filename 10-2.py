from collections import deque

# filename = '10-2-2.test.txt'
filename = '10.txt'

grid = []

with open(filename, 'r') as f:
    for line in f:
        grid.append(list(line.strip()))

def replace_start(i, j, grid):
    # We have to replace the start tile with its real value in order for the flip logic to work

    # up connects to me if it's in |, 7, F
    # down connects to me if it's in |, J, L
    # left connects to me if it's in -, F, L
    # right connects to me if it's in -, 7, J

    # | if up and down
    # - if left and right
    # 7 if left and down
    # F if right and down
    # J if left and up
    # L if right and up

    left, right, up, down = False, False, False, False
    if i > 0 and grid[i - 1][j] in "|7F":
        up = True
    if i < len(grid) - 1 and grid[i + 1][j] in "|JL":
        down = True
    if j > 0 and grid[i][j - 1] in "-FL":
        left = True
    if j < len(grid[0]) - 1 and grid[i][j + 1] in "-7J":
        right = True

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

# from pprint import pprint
# visited nodes are the loop nodes only
in_or_out = [
    [
        # [top-bottom in loop, left-right in loop]
        [False, False] if (i, j,) not in visited else ["X", "X"]
        for j in range(len(grid[0]))
    ]
    for i in range(len(grid))
]

# Left to right check:
for i in range(len(grid)):
    in_loop = False
    for j in range(len(grid[0])):
        if in_or_out[i][j][1] == "X":
            # Someone online said we should only flip if we have a loop tile going up
            # (or down, but only check one or the other).

            # if j < len(grid[0]) - 1 and in_or_out[i][j + 1][1] != "X":
            if grid[i][j] in "S|JL":
                in_loop = not in_loop
            continue

        in_or_out[i][j][0] = in_loop
        in_or_out[i][j][1] = in_loop

# Top to bottom check:
# for j in range(len(grid[0])):
#     in_loop = False
#     for i in range(len(grid)):
#         if in_or_out[i][j][0] == "X":
#             # if i < len(grid) - 1 and in_or_out[i + 1][j][0] != "X":
#             if grid[i][j] in "S|JL":
#                 in_loop = not in_loop
#             continue
#         in_or_out[i][j][0] = in_loop

count = 0
# visual_grid = [
#     [
#         "." for _ in range(len(grid[0]))
#     ]
#     for _ in range(len(grid))
# ]
# result = ""
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if in_or_out[i][j][0] is True and in_or_out[i][j][1] is True:
            count += 1
    #         visual_grid[i][j] = "I"
    #         result += "I"
    #     elif in_or_out[i][j][0] == "X":
    #         visual_grid[i][j] = "X"
    #         result += "X"
    #     else:
    #         result += "O"
    # result += "\n"

# pprint(visual_grid)
# print(result)
print(count)
