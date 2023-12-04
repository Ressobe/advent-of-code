class Number:
    def __init__(self, left_index, right_index, number):
        self.left_index = left_index
        self.right_index = right_index
        self.number = number

    def __repr__(self):
        return f"{self.number}"


def create_board(content: list) -> list:
    board = []
    for y in range(len(content)):
        current_line = content[y]

        left_index, right_index = -1, -1
        new_line = ['.'] * len(content[y])

        for x in range(len(content[y])):

            current_char = content[y][x]

            if current_char.isnumeric():
                if left_index == -1:
                    left_index = x
                    right_index = x
                else:
                    right_index = x
            else:
                if left_index != -1:
                    number = content[y][left_index:right_index + 1]
                    for i in range(left_index, right_index + 1):
                        new_line[i] = Number(left_index, right_index, int(number))
                    left_index = -1
                    right_index = -1

        board.append(new_line)

    return board


def part_one():
    with open('input.txt', 'r') as file:
        content = [line.strip() for line in file.readlines()]

    
    board = create_board(content)



    neighbours = [
        # left top diagonal
        [-1, -1],

        # top,
        [-1, 0],

        # right top diagonal
        [-1, 1],

        # right 
        [0, 1],

        # right bottom diagonal
        [1, 1],

        # bottom 
        [1, 0],

        # left bottom diagonal
        [1, -1],

        # left 
        [0, -1],
    ]

    suma = 0
    for y in range(len(content)):
        for x in range(len(content[y])):
            current_char = content[y][x]

            if not current_char.isnumeric() and current_char != '.':

                for n in neighbours:
                    new_y = y + n[0]
                    new_x = x + n[1]

                    if new_y > (len(content) - 1) or new_y < 0:
                        continue
                    if new_x > (len(content[y]) - 1) or new_x < 0:
                        continue


                    if isinstance(board[new_y][new_x], Number):
                        numberObject = board[new_y][new_x]
                        suma += numberObject.number

                        for i in range(numberObject.left_index, numberObject.right_index + 1):
                            board[new_y][i] = '.'

    print(suma)


def main():
    part_one()


if __name__ == '__main__':
    main()
