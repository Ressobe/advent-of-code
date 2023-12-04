def part_one():
    with open('sample.txt', 'r') as file:
        content = [line.strip() for line in file.readlines()]

    symbols = "*#+$"

    for y in range(0, len(content)):
        for x in range(0, len(content[y])):
            if content[y][x].isnumeric():
                left_index = x 
                right_index = x
                
                i = 1
                while (x + i < len(content[y])) and content[y][x+1].isnumeric():
                    right_index = x + i
                    i += 1

                print(f"{left_index}{right_index}", end=' ')
        print("")



def main():
    part_one()


if __name__ == '__main__':
    main()
