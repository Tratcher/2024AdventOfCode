print("hello!")

input = """....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#..."""

file = open("day6input.txt", "r")
input = file.read()

total = 0 

lines = input.splitlines()

for rO in range(len(lines)):
    for cO in range(len(lines[rO])):
        print(f"{rO},{cO},{total}")

        debug = rO == 11 and cO == 60

        if lines[rO][cO] != '.':
            # Need a blank space for the obstruction
            continue

        rows = []
        for line in lines:
            row = []
            for c in line:
                row.append(c)
            rows.append(row)

        rows[rO][cO] = '#' # new obstruction

        currentRow = 0
        currentCol = 0

        # Find the start
        for r in range(len(rows)):
            for c in range(len(rows[r])):
                ch = rows[r][c]
                if ch == '^' or ch == '>' or ch == 'v' or ch == '<':
                    currentCol = c
                    currentRow = r

        dir = rows[currentRow][currentCol]

        # clear the current location
        rows[currentRow][currentCol] = '.'

        while True:

            if debug:
                print(f"{currentRow},{currentCol},{dir}")

            # Loop detection, mark current location with direction, break if ever repeated?
            # Visited locations is insufixient, we may cross paths
            if rows[currentRow][currentCol] == dir:
                total += 1
                break
            if rows[currentRow][currentCol] == '.':
                rows[currentRow][currentCol] = dir
            
            match dir:
                case '^':
                    if currentRow == 0:
                        break
                    if rows[currentRow - 1][currentCol] == '#':
                        dir = '>'
                        continue
                    currentRow -= 1
                case '>':
                    if currentCol == len(rows[currentRow]) - 1:
                        break
                    if rows[currentRow][currentCol + 1] == '#':
                        dir = 'v'
                        continue
                    currentCol += 1
                case 'v':
                    if currentRow == len(rows) - 1:
                        break
                    if rows[currentRow + 1][currentCol] == '#':
                        dir = '<'
                        continue
                    currentRow += 1
                case '<':
                    if currentCol == 0:
                        break
                    if rows[currentRow][currentCol - 1] == '#':
                        dir = '^'
                        continue
                    currentCol -= 1

print(total)