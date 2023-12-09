with open('input.txt', 'r') as file:
    content = [line.strip() for line in file.readlines()]

moves = content[0]
content = content[2:]



nodes = {}

for line in content:
    l = line.split("=")
    n = l[0].strip()

    children = l[1].strip().split(",")
    left = children[0][1:]
    right = children[1][:-1].strip()

    nodes[n] = (left, right)



current_move, count, i = 0, 0, 0
current_node = 'AAA'

while current_node != 'ZZZ':
    step = moves[count % len(moves)]       

    if step == 'L':
        current_node = nodes[current_node][0]
    else:
        current_node = nodes[current_node][1]
    
    count += 1


print(count)
