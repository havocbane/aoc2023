from pprint import pprint

# filename = '6.test.txt'
filename = '6.txt'

time = 0
distance = 0

with open(filename, 'r') as f:
    for i, line in enumerate(f):
        line = line.strip()
        if line:
            data = line.split(':')[1].strip().replace(' ', '')
            if i % 2 == 0:
                time = int(data)
            else:
                distance = int(data)

print(f'Time: {time}, Distance: {distance}')

# d < xt - x^2
num_solns = 0
for x in range(1, time):
    if distance < x * time - x * x:
        num_solns += 1
print(num_solns)
