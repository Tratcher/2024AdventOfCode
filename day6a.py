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

lines = input.splitlines()

rows = []
for line in lines:
    row = []
    for c in line:
        row.append(c)
    rows.append(row)

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
print(currentRow)
print(currentCol)
print(dir)

total = 1
while True:
    print(str(currentRow) + ',' + str(currentCol) + ',' + dir)
    if rows[currentRow][currentCol] == '.':
        total += 1
        rows[currentRow][currentCol] = 'X'
    
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