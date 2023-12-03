# import math
import operator
from functools import reduce

# filename = '2.test.txt'
filename = '2.txt'

games = {}

with open(filename, 'r') as f:
    for l in f:
        l = l.strip()
        if l:
            # print(l)
            game_number = l.split(':')[0].split()[1].rstrip(':')
            sections = l.split(':')[1].split(';')
            minimums = {
                'red': 0, # math.inf
                'green': 0,
                'blue': 0,
            }
            for section in sections:
                colors = section.split(',')
                for color in colors:
                    num_color, color_name = color.split()
                    minimums[color_name.strip()] = max(int(num_color), minimums[color_name.strip()])
            # print(minimums)
            games[game_number] = reduce(operator.mul, minimums.values())

# print(games)
print(sum(games.values()))
