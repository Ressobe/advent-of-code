def part_one():
    with open('input.txt', 'r') as file:
        content = [line.strip() for line in file.readlines()]
    

    result = 0
    for line in content:
        left, right = line.split("|")[0], line.split("|")[1].strip()
        left = left.split(":")[1].strip().split(" ")
        right = right.split(" ")


        winning_numbers = set()
        your_numbers = set()

        for l in left:
            if l.isnumeric():
                winning_numbers.add(int(l))

        for r in right:
            if r.isnumeric():
                your_numbers.add(int(r))

        amount_winning_numbers = len(winning_numbers.intersection(your_numbers))

        if amount_winning_numbers > 0:
            result += pow(2, amount_winning_numbers - 1)


    print(result)


def part_two():
    with open('input.txt', 'r') as file:
        content = [line.strip() for line in file.readlines()]
    
    result = 0
    played = [0] * len(content)
    for i, line in enumerate(content):
        left, right = line.split("|")[0], line.split("|")[1].strip()
        left = left.split(":")[1].strip().split(" ")
        right = right.split(" ")

        played[i] += 1
        winning_numbers = set()
        your_numbers = set()

        for l in left:
            if l.isnumeric():
                winning_numbers.add(int(l))

        for r in right:
            if r.isnumeric():
                your_numbers.add(int(r))

        amount_winning_numbers = len(winning_numbers.intersection(your_numbers))

        for j in range(amount_winning_numbers):
            played[i+j+1] += played[i]

    result = sum(played)

    print(result)


def main():
    part_two()


if __name__ == '__main__':
    main()
