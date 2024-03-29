with open('input.txt', 'r') as file:
    content = [line.strip() for line in file.readlines()]


n = len(content)
m = len(content[0])


def is_symbol(y, x) -> bool:
    if not (0 <= y < n and 0 <= x < m):
        return False

    return content[y][x] != "." and not content[y][x].isdigit()


def part_one():
    answer = 0

    for y, row in enumerate(content):

        start = 0
        x = 0

        while x < m:
            start = x
            num = ""

            while x < m and row[x].isdigit():
                num += row[x]
                x += 1

            if num == "":
                x += 1
                continue

            num = int(num)

            if is_symbol(y, start-1) or is_symbol(y, x):
                answer += num
                continue

            for k in range(start-1, x+1):
                if is_symbol(y-1, k) or is_symbol(y+1, k):
                    answer += num
                    break
    print(answer)


def main():
    part_one()


if __name__ == '__main__':
    main()
