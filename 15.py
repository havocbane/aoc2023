# filename = '15.test.txt'
filename = '15.txt'

sequence = []

with open(filename, 'r') as f:
    for line in f:
        line = line.strip()
        sequence = line.split(',')

def ascii_value(ch):
    return ord(ch)

def main(s):
    hashes = []
    for code in s:
        value = 0
        for ch in code:
            value += ord(ch)
            value = (value * 17) % 256
        hashes.append(value)
    return sum(hashes)

print(main(sequence))

# time python 15.py
# 513172
# python 15.py  0.02s user 0.04s system 19% cpu 0.314 total
