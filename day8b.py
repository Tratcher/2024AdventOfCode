print("hello!")

input = """............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............"""

file = open("day8input.txt", "r")
input = file.read()

lines = input.splitlines()

# Find all the antennas
antennas = {}
for l in range(len(lines)):
    line = lines[l]
    for c in range(len(line)):
        ch = line[c]
        if ch != '.':
            antennas.setdefault(ch, []).append([l, c])

# Find the antinode
antinodes = [ [0]*len(lines[0]) for i in range(len(lines))]

def check_location(row, column):
    if 0 <= row and row < len(lines) \
        and 0 <= column and column < len(lines[0]):
        antinodes[row][column] = 1
        return True
    return False

def check_nodes(antenna1, antenna2):
    dY = antenna2[0] - antenna1[0]
    dX = antenna2[1] - antenna1[1]

    multiplier = 0
    while check_location(antenna1[0] - multiplier * dY, antenna1[1] - multiplier * dX):
        multiplier += 1

    multiplier = 0
    while check_location(antenna2[0] + multiplier * dY, antenna2[1] + multiplier * dX):
        multiplier += 1

for antennaName in antennas:
    print(f"{antennaName}; {antennas[antennaName]}")
    group = antennas[antennaName]
    for i in range(len(group)):
        antenna1 = group[i]
        for j in range(i + 1, len(group)):
            antenna2 = group[j]
            check_nodes(antenna1, antenna2)

# Count the results
total = 0

for row in antinodes:
    for value in row:
        total += value

print(total)