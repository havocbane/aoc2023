# filename = '2.test.txt'
filename = '2.txt'

config = {
    'red': 12,
    'green': 13,
    'blue': 14,
}
valid = set()
invalid = set()

with open(filename, 'r') as f:
    for l in f:
        l = l.strip()
        if l:
            # print(l)
            game_number = l.split(':')[0].split()[1].rstrip(':')
            valid.add(game_number)
            # print(game_number)
            sections = l.split(':')[1].split(';')
            for section in sections:
                # print(section)
                colors = section.split(',')
                for color in colors:
                    num_color, color_name = color.split()
                    if config[color_name] < int(num_color):
                        invalid.add(game_number)

valid_games = valid - invalid
# print(valid_games)
print(sum([int(x) for x in valid_games]))
