print("hello!")

input = """...0...
...1...
...2...
6543456
7.....7
8.....8
9.....9"""
input = """89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732"""

file = open("day10input.txt", "r")
input = file.read()

lines = input.splitlines()

def search_trail(r, c, step):
    if r < 0 or c < 0 or r >= len(lines) or c >= len(lines[r]):
        return 0 # out of bounds
    if lines[r][c] == "." or step != int(lines[r][c]):
        return 0 # wrong elevation
    # print(f"{r}, {c}, {step}")
    if step == 9:
        return 1
    step += 1
    return search_trail(r - 1, c, step) + search_trail(r + 1, c, step) + search_trail(r, c - 1, step) + search_trail(r, c + 1, step)

total = 0

for r in range(len(lines)):
    for c in range(len(lines[r])):
        trailheadscore = search_trail(r, c, 0)
        if trailheadscore > 0: print(trailheadscore)
        total += trailheadscore

print(total)