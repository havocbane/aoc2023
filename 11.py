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

# Expand grid (TODO)

galaxies = []
adj_matrix = {}  # Every grid cell to every neighboring grid cell with edge weight 1
for i in range(len(grid)):
    for j in range(len(grid[0])):
        vertex = i * len(grid[0]) + j

        if grid[i][j] == "#":
            galaxies.append(vertex)
        grid[i][j] = vertex

        neighboring_vertices = []
        if i > 0:
            up = (i - 1) * len(grid[0]) + j
            neighboring_vertices.append(up)
        if i < len(grid) - 1:
            down = (i + 1) * len(grid[0]) + j
            neighboring_vertices.append(down)
        if j > 0:
            left = i * len(grid[0]) + j - 1
            neighboring_vertices.append(left)
        if j < len(grid[0]) - 1:
            right = i * len(grid[0]) + j + 1
            neighboring_vertices.append(right)
        adj_matrix[vertex] = neighboring_vertices

# pprint(galaxies)
# pprint(grid)
# pprint(adj_matrix)

# Working, but too slow @ O(|V|^3) yuck!
# Apply Floyd-Warshall where every grid cell (i, j) is a vertex and every neighbor is an edge of weight 1 (above):
def floydwarshall():
    # https://brilliant.org/wiki/floyd-warshall-algorithm/
    def doesEdgeExist(start, end):
        for edge in adj_matrix[start]:
            if edge == end:
                return True
        return False

    M = [
        [
            math.inf # x * len(adj_matrix) + y
            for _ in range(len(adj_matrix)) # y
        ] for _ in range(len(adj_matrix)) # x
    ]
    for x in range(len(M)):
        for y in range(len(M[0])):
            if x == y:
                M[x][y] = 0
            exists = doesEdgeExist(x, y)
            if exists:
                M[x][y] = 1

    for k in range(len(M)):
        for i in range(len(M)):
            for j in range(len(M)):
                newDistance = M[i][k] + M[k][j]
                if newDistance < M[i][j]:
                    M[i][j] = newDistance
    return M

# Locate the paths in the resulting matrix and sum them up to get the answer
M = floydwarshall()
# pprint(M)

s = 0
for i, j in itertools.combinations(galaxies, 2):
    if i != j:
        distance = M[i][j]
        s += distance
        # print(i, j, distance)
print(s)
