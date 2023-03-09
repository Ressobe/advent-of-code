def read_winning_numbers(filename: str) -> list:
    with open(filename, 'r') as file:
        content = [line.strip().split(',') for line in file.readlines()]
        return [int(line) for line in content[0]]


def create_board(content: list, index: int) -> list:
    board = []
    for i in range(index, index+5):
        numbers = content[i].split()
        numbers = {int(num):0 for num in numbers}
        board.append(numbers)
    return board


def read_boards(filename: str) -> list:
    with open(filename, 'r') as file:
        content = [line.strip() for line in file.readlines()]
        boards = []
        for i in range(0, len(content), 6):
            boards.append(create_board(content, i))
        return boards


def check_board(board: dict, numbers: list):
    for row in board:
        for num in row.keys():
            if num in numbers:
                row[num] = 1

        if sum(row.values()) == 5:
            return board


    for i in range(len(board)):
        indx = 0 
        for j in range(len(board[0])):
            current_num = list(board[j].keys())[i]
            if current_num in numbers:
                board[j][current_num] = 1
                indx += 1
        if indx == 5:
            return board
                
    return {}


def part_one(boards: list, numbers: list):
    for i in range(len(numbers)):
        win_board = False
        for board in boards:
            current_numbers = numbers[0:i]
            result = check_board(board, current_numbers)
            if result:
                win_board = True
                suma = sum_board(board, current_numbers[-1])
                print(suma)
                break
        if win_board:
            break


def sum_board(board: dict, last_number: int) -> int:
    suma = 0
    for row in board:
        for key, value in row.items():
            if not value:
                suma += key
    return suma * last_number


def check_when_board_win(board: dict, numbers: list):
    for i in range(len(numbers)):
        current_numbers = numbers[0:i]
        if check_board(board, current_numbers):
            return i 


def part_two(boards: list, numbers: list):
    boards_wins = []
    for b in boards:
        boards_wins.append(check_when_board_win(b, numbers))
    
    board_index = -1
    max_value = boards_wins[0]

    for index, value in enumerate(boards_wins):
        if value > max_value:
            board_index = index
            max_value = value

    last_win_board = check_board(boards[board_index], numbers[0:max_value])
    suma = sum_board(last_win_board, numbers[max_value - 1])
    print(suma)


def main():
    numbers = read_winning_numbers('dane2.txt')
    boards = read_boards('dane.txt')

    part_one(boards, numbers)
    part_two(boards, numbers)


if __name__ == '__main__':
    main()
