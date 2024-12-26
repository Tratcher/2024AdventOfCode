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
input = """AAAA
BBCD
BBCC
EEEC"""
input = """EEEEE
EXXXX
EEEEE
EXXXX
EEEEE""" # 236
input = """AAAAAA
AAABBA
AAABBA
ABBAAA
ABBAAA
AAAAAA""" # 368

file = open("day12input.txt", "r")
input = file.read()

lines = input.splitlines()
gardens = [[None for _ in range(len(lines[0]))] for _ in range(len(lines))]

#print(lines)
#print(gardens)

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
        return True
    return lines[r][c] != type

# Perimiter: Visit each space and count how many edges are not shared with a neighbor of the same type (including map edges)
def measure_perimeter(gardenid):
    total = 0
    for r in range(len(lines)):
        for c in range(len(lines[r])):
            if gardens[r][c] == gardenid:
                type = lines[r][c]
                # north border, and west border or no border north of west
                if hasborder(r - 1, c, type) and (hasborder(r, c - 1, type) or not hasborder(r - 1, c - 1, type)):
                    total += 1
                # south border, and west border or no border south of west
                if hasborder(r + 1, c, type) and (hasborder(r, c - 1, type) or not hasborder(r + 1, c - 1, type)):
                    total += 1
                # west border, and north border or no border west of north
                if hasborder(r, c - 1, type) and (hasborder(r - 1, c, type) or not hasborder(r - 1, c - 1, type)):
                    total += 1
                # east border, and north border or no border east of north
                if hasborder(r, c + 1, type) and (hasborder(r - 1, c, type) or not hasborder(r - 1, c + 1, type)):
                    total += 1
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

for row in gardens:
    print(row)
print(total)