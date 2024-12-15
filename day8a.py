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

def check_nodes(antenna1, antenna2):
    dY = antenna2[0] - antenna1[0]
    dX = antenna2[1] - antenna1[1]
    n1Y = antenna2[0] + dY
    n1X = antenna2[1] + dX
    n2Y = antenna1[0] - dY
    n2X = antenna1[1] - dX
    # print(f"{antenna1} {antenna2} d[{dY},{dX}] [{n1Y},{n1X}] [{n2Y},{n2X}]")
    if 0 <= n1Y and n1Y < len(lines) \
        and 0 <= n1X and n1X < len(lines[0]):
        antinodes[n1Y][n1X] = 1
    if 0 <= n2Y and n2Y < len(lines) \
        and 0 <= n2X and n2X < len(lines[0]):
        antinodes[n2Y][n2X] = 1

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