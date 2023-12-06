# from pprint import pprint

# filename = '6.test.txt'
filename = '6.txt'

times = []
distances = []

with open(filename, 'r') as f:
    for i, line in enumerate(f):
        line = line.strip()
        if line:
            data = list(map(lambda x: int(x.strip()), line.split(':')[1].split()))
            if i % 2 == 0:
                times.extend(data)
            else:
                distances.extend(data)

# values = list(zip(times, distances))
# pprint(values)

result = 1

# d < xt - x^2
for t, d in zip(times, distances):
    num_solns = 0
    for x in range(1, t):
        if d < x * t - x * x:
            num_solns += 1
    result *= num_solns
print(result)
