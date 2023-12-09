import math


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


def n_step(current_node):
    count = 0
    while current_node[2] != 'Z':
        step = moves[count % len(moves)]       
        if step == 'L':
            current_node = nodes[current_node][0]
        else:
            current_node = nodes[current_node][1]
        count += 1
    return count

lens = [n_step(n) for n in nodes if n[2] == 'A']
print(math.lcm(*lens))
