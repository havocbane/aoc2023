# filename = '5.test.txt'
filename = '5.txt'

modes = {
    'seeds': [],
    'seed-to-soil map': [],
    'soil-to-fertilizer map': [],
    'fertilizer-to-water map': [],
    'water-to-light map': [],
    'light-to-temperature map': [],
    'temperature-to-humidity map': [],
    'humidity-to-location map': [],
}
curr_mode = None

with open(filename, 'r') as f:
    for line in f:
        line = line.strip()
        if ':' in line:
            line = line.split(':')
            curr_mode = line[0].strip()
            if curr_mode == 'seeds':
                modes[curr_mode] = [int(x) for x in line[1].split()]
        elif line:
            mode = modes[curr_mode]
            dst_start, src_start, range_len = [int(x) for x in line.split()]
            mode.append((dst_start, src_start, range_len,))

# Get tuples of (seed_range_start, seed_range_length,):
seeds = list(zip(modes['seeds'][::2], modes['seeds'][1::2]))

# Only remaining items are transforms from source range to projection:
del modes['seeds']

def transform(ranges):
    """The inspiration/algorithm to use range intervals for this is from:
      https://github.com/jonathanpaulson/AdventOfCode/blob/master/2023/5.py
    """
    locs = []
    for mode in curr_mode:
        dst_start, src_start, range_length = mode
        src_end = src_start + range_length

        next_range = []
        while ranges:
            (start, end,) = ranges.pop()

            # Intersection calculations; before our source range, intersecting ranges, after our source range:
            before = (start, min(src_start, end),)
            after = (max(start, src_end), end,)
            intersection = (max(start, src_start), min(end, src_end),)

            if before[1] > before[0]:
                next_range.append(before)

            if after[1] > after[0]:
                next_range.append(after)

            if intersection[1] > intersection[0]:
                # The distance to the value in the projected range is
                # the difference of the source range to the value
                # plus the start of the destination:
                locs.append((intersection[0] - src_start + dst_start, intersection[1] - src_start + dst_start,))

        # Anything outside the intersection,
        # but still mapped in the current projection,
        # needs to be checked on the next transform:
        ranges = next_range

    # Ranges left over (not intersecting) aren't in the destination projection
    # (e.g. input 10 maps to output 10), so add them here:
    return locs + ranges

min_locs = []
for seed_start, seed_length in seeds:
    ranges = [(seed_start, seed_start + seed_length,)]
    for curr_mode in modes.values():
        ranges = transform(ranges)
    min_locs.append(min(ranges)[0])

print(min(min_locs))
