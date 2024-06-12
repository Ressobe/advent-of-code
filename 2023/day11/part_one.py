with open("sample.txt") as file:
    content = [line.strip() for line in file.readlines()]



def have_galaxies(line: list) -> bool:
    for l in line:
        if l != '.':
            return True
    return False

def expand_rows(space: list) -> list:
    new_board = []
    for i in range(len(space)):
        current_line = space[i]
        if have_galaxies(current_line):
            new_board.append(current_line)
        else:
            new_board.append(current_line)
            new_board.append(current_line)
    return new_board    


def expand_columns(space: list) -> list:
    new_board = []

    for i in range(len(space[0])):
        for j in range(len(space)):
            print(space[i + j][i])
        print("\n")

    pass
        

c = expand_rows(content)
expand_columns(c)
