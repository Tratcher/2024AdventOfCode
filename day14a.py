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

time = 100
width = 11
height = 7
width = 101
height = 103
midWidth = int(width / 2) # round down
midHeight = int(height / 2)
# print(f"{width}x{height} {midWidth},{midHeight}")

q1 = 0
q2 = 0
q3 = 0
q4 = 0

for line in lines:
    commaIndex = line.find(',')
    spaceIndex = line.find(' ')
    commaIndex2 = line.find(',', commaIndex + 1)
    x = int(line[len("p="):commaIndex])
    y = int(line[commaIndex + 1:spaceIndex])
    dx = int(line[spaceIndex + len(" v="):commaIndex2])
    dy = int(line[commaIndex2 + 1:])

    # print(f"{x},{y} {dx},{dy}")

    x = (x + dx * time) % width
    y = (y + dy * time) % height
    
    # print(f"{x},{y}")

    # Skip bots on boundaries
    if x < midWidth and y < midHeight: q1 += 1 #; print("q1")
    if x > midWidth and y < midHeight: q2 += 1 #; print("q2")
    if x < midWidth and y > midHeight: q3 += 1 #; print("q3")
    if x > midWidth and y > midHeight: q4 += 1 #; print("q4")

# print(f"{q1},{q2},{q3},{q4}")
total = q1 * q2 * q3 * q4

print(total)
# 85845240 is too low