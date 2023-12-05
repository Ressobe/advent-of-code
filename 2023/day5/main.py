from pprint import pprint


def fill_missing_numbers(numbers: dict) -> None:
    for i in range(0, max(numbers,key=numbers.get)):
        if (i not in numbers.keys()):
            numbers[i] = i


def dest_source_range(row: str) -> tuple[int, int, int]:
     splited_row = row.split(" ")
     return (int(splited_row[0]), int(splited_row[1]), int(splited_row[2]))


def create_almanac(content: list) -> list[str]:
    i = 0
    almanac = []
    while i < len(content):
        row = []
        while i < len(content) and content[i] != '':
            row.append(content[i])
            i += 1
        almanac.append(row)
        i += 1
    return almanac



def part_one():
    with open('sample.txt', 'r') as file:
        content = [line.strip() for line in file.readlines()]


    seeds = content[0].split(":")[1].strip().split(" ")
    seeds = [int(s) for s in seeds]


    almanac = create_almanac(content[2:])
    numbers = dict()

    
    for index, row in enumerate(almanac):
        for i in range(1, len(row)):
            dest_range_start, source_range_start, range_length = dest_source_range(row[i])


            for j in range(0, range_length):
                numbers[source_range_start + j] =  dest_range_start + j

        fill_missing_numbers(numbers)
        pprint(numbers)

def main():
    part_one()


if __name__ == '__main__':
    main()
