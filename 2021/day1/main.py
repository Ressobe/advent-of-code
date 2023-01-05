file = open('input.txt', 'r')
lines = file.readlines()
lines = [int(lines.strip()) for lines in lines]
increased = 0
index = 0


while index < len(lines) - 1:
    if lines[index] < lines[index + 1]:
        increased += 1
    index += 1

count = sum(lines[i] > lines [i - 3] for i in range(3, len(lines)))

print(count)
