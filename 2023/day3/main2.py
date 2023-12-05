with open('input.txt', 'r') as file:
    content = [line.strip() for line in file.readlines()]


n = len(content)
m = len(content[0])

gears = [ [ [] for _ in range(m) ] for _ in range(n)]


def add_gears(y, x, num) -> bool:
    if not (0 <= y < n and 0 <= x < m):
        return

    if content[y][x] == "*":
        gears[y][x].append(num)


def part_two():
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

            add_gears(y, start-1, num)  
            add_gears(y, x, num)

            for k in range(start-1, x+1):
                add_gears(y-1, k, num)
                add_gears(y+1, k, num)
            

    for y in range(n):
        for x in range(m):
            if content[y][x] == '*' and len(gears[y][x]) == 2:
                answer += gears[y][x][0] * gears[y][x][1]
        




    print(answer)

def main():
    part_two()


if __name__ == '__main__':
    main()
