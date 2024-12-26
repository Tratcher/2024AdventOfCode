print("hello!")

input = """RRRRIICCFF
RRRRIICCCF
VVRRRCCFFF
VVRCCCJFFF
VVVVCJJCFE
VVIVCCJJEE
VVIIICJJEE
MIIIIIJJEE
MIIISIJEEE
MMMISSJEEE"""
#input = """AAAA
#BBCD
#BBCC
#EEEC"""


file = open("day12input.txt", "r")
input = file.read()

lines = input.splitlines()
gardens = [[None for _ in range(len(lines[0]))] for _ in range(len(lines))]

# Area: Recursive flood fill
def fill_garden(r, c, gardenid, type):
    if r < 0 or c < 0 or r >= len(lines) or c >= len(lines[r]):
        return 0
    if lines[r][c] == type and gardens[r][c] == None:
        gardens[r][c] = gardenid
        return 1 \
            + fill_garden(r - 1, c, gardenid, type) \
            + fill_garden(r + 1, c, gardenid, type) \
            + fill_garden(r, c - 1, gardenid, type) \
            + fill_garden(r, c + 1, gardenid, type)
    return 0

def hasborder(r, c, type):
    if r < 0 or c < 0 or r >= len(lines) or c >= len(lines[r]):
        return 1
    return 0 if lines[r][c] == type else 1

# Perimiter: Visit each space and count how many edges are not shared with a neighbor of the same type (including map edges)
def measure_perimeter(gardenid):
    total = 0
    for r in range(len(lines)):
        for c in range(len(lines[r])):
            if gardens[r][c] == gardenid:
                type = lines[r][c]
                total += hasborder(r - 1, c, type) \
                    + hasborder(r + 1, c, type) \
                    + hasborder(r, c - 1, type) \
                    + hasborder(r, c + 1, type)
    return total

total = 0

gardenid = 0

for r in range(len(lines)):
    for c in range(len(lines[r])):
        if gardens[r][c] == None:
            gardenid += 1
            area = fill_garden(r, c, gardenid, lines[r][c])
            perimeter = measure_perimeter(gardenid)
            total += area * perimeter

print(gardens)
print(total)