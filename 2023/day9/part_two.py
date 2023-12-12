with open('input.txt', 'r') as file:
    content = [line.strip() for line in file.readlines()]


def check_all_zeros(numbers: list[int]) -> bool:
    for n in numbers:
        if n != 0:
            return False
    return True


def calculate_sum(extrapolate: list[list]) -> int:
    s = 0
    for i in range(len(extrapolate) - 1, 0, -1):
        current_line = extrapolate[i] 
        previous_line = extrapolate[i - 1]
        s = current_line[-1] + previous_line[-1]
        previous_line.append(s)
    return s


content = [[int(l) for l in line.split(" ")] for line in content]
result = 0


for i in range(len(content)):
    current_line = content[i]
    current_line.reverse()
    extrapolates = [current_line.copy()]
    zeros = False

    while not zeros:
        new_extrapolate = []
        for i in range(len(current_line) - 1):
            new_extrapolate.append(current_line[i + 1] - current_line[i])

        extrapolates.append(new_extrapolate)
        current_line = new_extrapolate.copy()

        if check_all_zeros(current_line):
            zeros = True
            result += calculate_sum(extrapolates)

print(result)
