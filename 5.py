import math
# from pprint import pprint

# filename = '5.test.txt'
filename = '5.txt'

modes = {
    'seeds': [],
    'seed-to-soil map': {},
    'soil-to-fertilizer map': {},
    'fertilizer-to-water map': {},
    'water-to-light map': {},
    'light-to-temperature map': {},
    'temperature-to-humidity map': {},
    'humidity-to-location map': {},
}
curr_mode = None

with open(filename, 'r') as f:
    for line in f:
        line = line.strip()
        if ':' in line:
            line = line.split(':')
            curr_mode = line[0].strip()
            if curr_mode == 'seeds':
                modes[curr_mode] = list(map(lambda x: int(x), line[1].split()))
        elif line:
            mode = modes[curr_mode]
            dst_start, src_start, range_len = list(map(lambda x: int(x), line.split()))
            # Runs out of memory!
            # dst = range(dst_start, dst_start + range_len)
            # src = range(src_start, src_start + range_len)
            # mode.update(zip(src, dst))

            # src_range: dst_range
            mode[f'{src_start}..{src_start + range_len}'] = f'{dst_start}..{dst_start + range_len}'

# pprint(modes)

def check_src_in_dst_range(src, mode):
    for src_range, dst_range in mode.items():
        src_start, src_end = list(map(lambda x: int(x), src_range.split('..')))
        if src_start <= src <= src_end:
            dst_start, _ = list(map(lambda x: int(x), dst_range.split('..')))
            return int(dst_start) + abs(src - src_start)
    return src

min_loc = math.inf
for seed in modes['seeds']:
    # soil = modes['seed-to-soil map'].get(seed, seed)
    soil = check_src_in_dst_range(seed, modes['seed-to-soil map'])
    # fert = modes['soil-to-fertilizer map'].get(soil, soil)
    fert = check_src_in_dst_range(soil, modes['soil-to-fertilizer map'])
    # water = modes['fertilizer-to-water map'].get(fert, fert)
    water = check_src_in_dst_range(fert, modes['fertilizer-to-water map'])
    # light = modes['water-to-light map'].get(water, water)
    light = check_src_in_dst_range(water, modes['water-to-light map'])
    # temp = modes['light-to-temperature map'].get(light, light)
    temp = check_src_in_dst_range(light, modes['light-to-temperature map'])
    # humid = modes['temperature-to-humidity map'].get(temp, temp)
    humid = check_src_in_dst_range(temp, modes['temperature-to-humidity map'])
    # loc = modes['humidity-to-location map'].get(humid, humid)
    loc = check_src_in_dst_range(humid, modes['humidity-to-location map'])
    min_loc = min(min_loc, loc)

print(min_loc)