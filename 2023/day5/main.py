with open('input.txt', 'r') as file:
    content = [line.strip() for line in file.readlines()]


seeds = content[0].split(":")[1].strip().split(" ")

seeds_ranges = []
for i in range(len(seeds) - 1):
    seeds_ranges.append((seeds[i], seeds[i+1]))


content = content[2:]

maps = []

i = 0
while i < len(content):
    current_map = []
    while i < len(content) and content[i] != '':
        if not content[i][0].isnumeric():
            i += 1
            continue
        current_map.append([int(n) for n in content[i].split(' ')])
        i += 1

    maps.append(current_map)
    i += 1


def find_localization(seed: int) -> int:
    current_number = seed
    for map in maps:

        for line in map:
            destination_start, source_start, range_length = line
            source_end = source_start + range_length - 1 
            if source_start <= current_number <= source_end:
                current_number = (current_number - source_start) + destination_start
                break

    return current_number


min_local = []
for i, s in enumerate(seeds_ranges):
    seed_start = int(s[0])
    seed_end = seed_start + int(s[1])

    localizations = [find_localization(n) for n in range(seed_start, seed_end)]
    min_local.append(min(localizations))

print(min(min_local))


# localizations = [find_localization(s) for s in seeds ]
#
# print(min(localizations))
