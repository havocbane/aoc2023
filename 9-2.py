from typing import List
from functools import reduce

# filename = '9.test.txt'
filename = '9.txt'

sensor_readings = []

with open(filename, 'r') as f:
    for line in f:
        sensor_readings.append([int(r) for r in line.split()])

def differences(readings) -> List[int]:
    pairs = zip(readings[::1], readings[1::1])
    return [r - l for l, r in pairs]

result = 0
for sensor_reading in sensor_readings:
    diffs = [sensor_reading[0]]
    sensor_reading = differences(sensor_reading)
    while not all([r == 0 for r in sensor_reading]):
        diffs.append(sensor_reading[0])
        sensor_reading = differences(sensor_reading)
    diffs.reverse()
    result += reduce(lambda x, y: y - x, diffs)
print(result)
