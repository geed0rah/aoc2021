file = open("data")
data = file.read().splitlines()

hPos = 0
depth = 0
aim = 0

for line in data:
    move = line.split(' ')
    direction = move[0]
    units = int(move[1])
    if direction == "forward":
        hPos = hPos + units
    if direction == "up":
        depth = depth - units
    if direction == "down":
         depth = depth + units

print("PART 1")
print(depth)
print(hPos)
print(depth * hPos)
hPos = 0
depth = 0
aim = 0
for line in data:
    move = line.split(' ')
    direction = move[0]
    units = int(move[1])
    if direction == "forward":
        hPos = hPos + units
        depth = depth + (aim * units)
    if direction == "up":
        # depth = depth - units
        aim = aim - units
    if direction == "down":
        # depth = depth + units
        aim = aim + units
print("PART 2")
print(depth)
print(hPos)
print(depth * hPos)