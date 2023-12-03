def part_one():
    with open('input.txt', 'r') as file:
        content = [line.strip() for line in file.readlines()]

    suma = 0 
    for line in content:
        red, green, blue = 0, 0, 0

        splited_line = line.split(":")
        game_id = int(splited_line[0].split(" ")[1])


        cubes = splited_line[1].strip().split(";")

        save = True

        for c in cubes:
            sc = c.split(",")
            
            wyjscie = False
            for z in sc:
                 x = z.strip().split(" ")
                 number = int(x[0])
                 color = x[1]
                 
                 if color == "red":
                     if number > 12:
                         wyjscie = True
                         break
                 if color == "green":
                     if number > 13:
                         wyjscie = True
                         break
                 if color == "blue":
                     if number > 14:
                         wyjscie = True
                         break

            if wyjscie:
                save = False
                break

        if save:
            suma += game_id

    print(suma)


def part_two():
    with open('input.txt', 'r') as file:
        content = [line.strip() for line in file.readlines()]

    suma = 0 
    for line in content:
        splited_line = line.split(":")
        game_id = int(splited_line[0].split(" ")[1])


        cubes = splited_line[1].strip().split(";")

        save = True

        maxRed, maxGreen, maxBlue = 1, 1, 1
        for c in cubes:
            sc = c.split(",")

            for z in sc:
                 x = z.strip().split(" ")
                 number = int(x[0])
                 color = x[1]
                 
                 if color == "red":
                     if number > maxRed:
                         maxRed = number
                 if color == "green":
                     if number > maxGreen:
                         maxGreen = number
                 if color == "blue":
                     if number > maxBlue:
                         maxBlue = number

        suma += maxRed * maxGreen * maxBlue
    print(suma)

def main():
    part_two()


if __name__ == '__main__':
    main()
