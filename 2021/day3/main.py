def read_from_file(filename: str) -> list:
    with open(filename, 'r') as file:
        return [line.strip() for line in file.readlines()]


def find_numbers(content: list, num: str, index: int) -> list:
    numbers = []
    for line in content:
        if line[index] == num:
            numbers.append(line)
    return numbers


def oxygen(content: list):
    i = 1
    oxg =  bits_for_oxygen(content, 0)
    numbers = find_numbers(content, oxg, 0)
    ln = len(numbers)

    while ln != 1 :
        oxg = bits_for_oxygen(numbers, i)
        numbers = find_numbers(numbers, oxg, i)
        ln = len(numbers)
        i += 1

    return int(numbers[0], 2)


def co2(content: list):
    i = 1
    c =  bits_for_co2(content, 0)
    numbers = find_numbers(content, c, 0)
    ln = len(numbers)

    while ln != 1 :
        c = bits_for_co2(numbers, i)
        numbers = find_numbers(numbers, c, i)
        ln = len(numbers)
        i += 1

    return int(numbers[0], 2)


def gamma_epsilon_rate(content: list) -> tuple:
    rows = len(content)
    columns = len(content[0])
    gamma_rate = ''
    epsilon_rate = ''

    for i in range(columns):
        bit_1 = 0
        bit_0 = 0
        for j in range(rows):
            bit = content[j][i]
            if bit == '0':
                bit_0 += 1
            else:
                bit_1 += 1

        gamma_rate += '1' if bit_1 >= bit_0 else '0'
        epsilon_rate += '0' if bit_1 >= bit_0 else '1'

    return (gamma_rate, epsilon_rate)


def bits_for_oxygen(content: list, index: int):
    bit_1 = 0
    bit_0 = 0
    for line in content:
            bit = line[index]
            if bit == '0':
                bit_0 += 1
            else:
                bit_1 += 1

    if bit_1 >= bit_0:
        return '1'
    else:
        return '0'


def bits_for_co2(content: list, index: int):
    bit_1 = 0
    bit_0 = 0
    for line in content:
            bit = line[index]
            if bit == '0':
                bit_0 += 1
            else:
                bit_1 += 1

    if bit_0 <= bit_1:
        return '0'
    return '1'


def main():
    content = read_from_file('dane.txt')
    a = oxygen(content)
    b = co2(content)

    print(a*b)


if __name__ == '__main__':
    main()

