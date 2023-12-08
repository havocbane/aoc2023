import math
from pprint import pprint

# filename = '8-2.test.txt'
filename = '8.txt'

instructions = ""
nodes = {}

with open(filename, 'r') as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
        if not instructions:
            instructions = line
        else:
            node, coords = line.split('=')
            node = node.strip()
            left, right = coords.replace('(', '').replace(')', '').split(',')
            nodes[node] = {
                'L': left.strip(),
                'R': right.strip(),
            }

# Find the distances from starting nodes to end nodes and include cycle distances from end nodes;
# the least common multiple of all those distances is the answer because it would be the smallest
# number of cycles to have all nodes reach the end at the same time:
distances = {}
curr_nodes = [node for node in nodes.keys() if node[-1] in ('A', 'Z')]
for curr_node in curr_nodes:
    steps = 0
    instruction = 0
    while curr_node[-1] != 'Z' or steps == 0:
        l_or_r = instructions[instruction]
        curr_node = nodes[curr_node][l_or_r]
        steps += 1
        instruction = (instruction + 1) % len(instructions) # account for looping
    distances[curr_node] = steps

pprint(distances)
print(math.lcm(*distances.values()))
