import re
from collections import defaultdict

# filename = '15.test.txt'
filename = '15.txt'

sequence = []

with open(filename, 'r') as f:
    for line in f:
        line = line.strip()
        sequence = line.split(',')

def HASH(key):
    value = 0
    for ch in key:
        value += ord(ch)
        value = (value * 17) % 256
    return value

def focusing_power(box_num, slot, focal_length):
    return (box_num + 1) * slot * focal_length

regex = '(\w+)([=-])(\d+)?'
pattern = re.compile(regex)

def main(s):
    hashes = defaultdict(dict)  # This utilizes OrderedDicts in Python 3
    for code in s:
        label, op, focal_length = pattern.match(code).groups()
        h = HASH(label)  # Box #
        if op == "=":
            hashes[h][label] = int(focal_length)
        elif label in hashes[h]:
            del hashes[h][label]

    return sum([
        focusing_power(k, slot, focal_length)
        for k, v in hashes.items()
        for slot, (_, focal_length,) in enumerate(v.items(), start=1)
    ])

print(main(sequence))

# time python 15-2.py
# 237806
# python 15-2.py  0.03s user 0.05s system 23% cpu 0.348 total
