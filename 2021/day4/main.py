def read_winning_numbers(filename: str) -> list:
    with open(filename, "r") as file:
        content = file.readline()
        winning_numbers = list(content.split(","))
        winning_numbers = [int(line.strip()) for line in winning_numbers]

    return winning_numbers


def read_board(filename: str) -> list:
    with open(filename, "r") as file:
        boards = file.readlines()
        boards.pop(0)

        for index, element in enumerate(boards):
            if element == "\n":
                boards.pop(index)

        boards = [item.split() for item in boards]

        new_boards = []
        for board in boards:
            row = []
            for i in board:
                row.append(int(i))

            new_boards.append(row)

    return new_boards


def main():
    file = "test.txt"
    # winning_numbers = read_winning_numbers(file)
    boards = read_board(file)
    winning_numbers = [17, 23, 2, 0, 14, 21]
    suma = 0
    for row in boards:
        for num in row:
            if num not in winning_numbers:
                suma += int(num)

    print(suma)


if __name__ == "__main__":
    main()
