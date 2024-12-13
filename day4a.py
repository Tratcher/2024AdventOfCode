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

def check_dir(r, c, r_offset, c_offset):
    r_end = r + r_offset * 3
    c_end = c + c_offset * 3
    if r_end < 0 or r_end >= len(lines) or c_end < 0 or c_end >= len(lines[r]):
        return False
    return lines[r][c] == 'X' \
        and lines[r + 1 * r_offset][c + 1 * c_offset] == 'M' \
        and lines[r + 2 * r_offset][c + 2 * c_offset] == 'A' \
        and lines[r + 3 * r_offset][c + 3 * c_offset] == 'S'

total = 0
for r in range(len(lines)):
    for c in range(len(lines[r])):
        if check_dir(r, c, 0, 1): # e
            total += 1
        if check_dir(r, c, 1, 1): # se
            total += 1
        if check_dir(r, c, 1, 0): # s
            total += 1
        if check_dir(r, c, 1, -1): # sw
            total += 1
        if check_dir(r, c, 0, -1): # w
            total += 1
        if check_dir(r, c, -1, -1): # nw
            total += 1
        if check_dir(r, c, -1, 0): # n
            total += 1
        if check_dir(r, c, -1, 1): # ne
            total += 1

print(total)