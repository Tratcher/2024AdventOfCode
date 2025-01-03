import time

print("hello!")

input = """p=0,4 v=3,-3
p=6,3 v=-1,-3
p=10,3 v=-1,2
p=2,0 v=2,-1
p=0,0 v=1,3
p=3,0 v=-2,-2
p=7,6 v=-1,-3
p=3,0 v=-1,-2
p=9,3 v=2,3
p=7,3 v=-1,2
p=2,4 v=2,-3
p=9,5 v=-3,-3"""


file = open("day14input.txt", "r")
input = file.read()

lines = input.splitlines()

width = 11
height = 7
width = 101
height = 103
midWidth = int(width / 2) # round down
midHeight = int(height / 2)
# print(f"{width}x{height} {midWidth},{midHeight}")

def showgrid():
    print()
    for row in grid:
        buffer = ""
        for i in range(width):
            buffer += '.' if row[i] == None else str(row[i])
        print(buffer)

for t in range(0, 10000):

    grid = [[None for _ in range(width)] for _ in range(height)]

    conflict = False

    for line in lines:
        commaIndex = line.find(',')
        spaceIndex = line.find(' ')
        commaIndex2 = line.find(',', commaIndex + 1)
        x = int(line[len("p="):commaIndex])
        y = int(line[commaIndex + 1:spaceIndex])
        dx = int(line[spaceIndex + len(" v="):commaIndex2])
        dy = int(line[commaIndex2 + 1:])

        x = (x + dx * t) % width
        y = (y + dy * t) % height

        if grid[y][x] == 'x':
            conflict = True
            break

        grid[y][x] = 'x'

    if not conflict:
        showgrid()
        print(t)
        time.sleep(0.25)    

# 392 is too low
# 10,000 is too high