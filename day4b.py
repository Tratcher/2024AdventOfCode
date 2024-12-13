print("hello!")

# 18
input = """MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX"""

file = open("day4input.txt", "r")
input = file.read()

lines = input.splitlines()

def check_x(r, c):
    if r == 0 or r == len(lines) - 1 or c == 0 or c == len(lines[r]) - 1:
        return False
    return lines[r][c] == 'A' \
        and (\
                (lines[r + 1][c + 1] == 'M' \
                and lines[r - 1][c - 1] == 'S') \
                or (lines[r + 1][c + 1] == 'S' \
                and lines[r - 1][c - 1] == 'M') \
            ) \
        and (\
                (lines[r + 1][c - 1] == 'M' \
                and lines[r - 1][c + 1] == 'S') \
                or (lines[r + 1][c - 1] == 'S' \
                and lines[r - 1][c + 1] == 'M') \
            )

total = 0
for r in range(len(lines)):
    for c in range(len(lines[r])):
        if check_x(r, c):
            total += 1

print(total)