from pprint import pprint

# filename = '8.test.txt'
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

# pprint(instructions)
# pprint(nodes)

steps = 0
node = 'AAA'
while node != 'ZZZ':
    for step in instructions:
        node = nodes[node][step]
        # print(node)
        steps += 1

print(steps)
