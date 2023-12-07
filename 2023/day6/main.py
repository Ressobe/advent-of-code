with open('input.txt', 'r') as file:
    content = [line.strip() for line in file.readlines()]


times = content[0].split(':')[1].strip().split(" ")
times = [x for x in times if x != '']

distances = content[1].split(':')[1].strip().split(" ")
distances = [x for x in distances if x != '']


def part_one():
    result = 1
    for i in range(len(times)):
        wins = 0
        t = int(times[i])
        distance_record = int(distances[i])
        
        for b in range(1, t):
            boat_distance = (t - b) * b
            if boat_distance > distance_record:
                wins += 1

        result *= wins
    print(result)


def part_two():
    time = ''
    for t in times:
        time += t

    distance_record = ''
    for d in distances:
        distance_record += d

    time = int(time)
    distance_record = int(distance_record)
    
    wins = 0
    for b in range(1, time):
        boat_distance = (time - b) * b
        if boat_distance > distance_record:
            wins += 1

    print(wins)

# part_one()    
part_two()
