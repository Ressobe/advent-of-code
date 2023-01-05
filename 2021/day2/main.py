def part_one():
    with open('input.txt', 'r') as file:
        lines = file.read()
    lines = lines.split('\n')
    del lines[-1]

    x, y = 0, 0

    for i in range(0, len(lines)):
        if 'forward' in lines[i]:
            value = lines[i]
            value = value[-1]
            x += int(value)
        elif 'down' in lines[i]:
            value = lines[i]
            value = value[-1]
            y += int(value)
        elif 'up' in lines[i]:
            value = lines[i]
            value = value[-1]
            y -= int(value)

    return x, y

def part_two():
    with open('input.txt', 'r') as file:
        lines = file.read()
    lines = lines.split('\n')
    del lines[-1]
    x, y, z = 0, 0, 0
    for i in range(0, len(lines)):
        if 'forward' in lines[i]:
            value = lines[i]
            value = value[-1]
            x += int(value[-1])

            if z > 0:
                y = (int(value[-1]) * z) + y

        elif 'down' in lines[i]:
            value = lines[i]
            value = value[-1]
            z += int(value)

        elif 'up' in lines[i]:
            value = lines[i]
            value = value[-1]
            z -= int(value)

            
    return x * y

print(part_two())

