def part_one():
    with open('input.txt', 'r') as file:
        lines = file.read()
    lines = lines.split('\n')
    del lines[-1]

    # print(f'Cała lista: {lines}')
    # print(f'Jeden element: {lines[0]}')
    # print(f'Trzeci znak z elementu pierwszego: {lines[0][2]}')

    gamma_rate = ""
    epsilon = ""
    for b in range(0, len(lines[0])):
        bit1, bit0 = 0, 0
        for c in range(0, len(lines)):
            if lines[c][b] == "0":
                bit0 += 1
            else:
                bit1 += 1

        if bit0 > bit1:
            gamma_rate += "0"
            epsilon += "1"

        if bit1 > bit0:
            gamma_rate += "1"
            epsilon += "0"

    g = int(gamma_rate, 2)
    e = int(epsilon, 2)

    return g * e 


print(part_one())


def part_two():
    with open('input.txt', 'r') as file:
        lines = [x for x in file.read().split()]

    return lines


print(part_two())
