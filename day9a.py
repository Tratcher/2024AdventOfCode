print("hello!")

input = "12345"
input = """2333133121414131402"""

file = open("day9input.txt", "r")
input = file.read()

disk = [int(x) for x in input]

# Digits alternate between the length of a file and the lengh of free space

# File IDs 
# 0..111....22222
# 00...111...2...333.44.5555.6666.777.888899

EMPTY = -1

fileIds = []
for i in range(len(disk)):
    length = disk[i]
    value = int(i / 2)
    if i % 2 == 1: # free
        value = EMPTY
    for j in range(length):
        fileIds.append(value)

def render():
    text = ""
    for d in fileIds:
        if d == EMPTY:
            text += '.'
        else:
            text += str(d)
    print(text)

render()

# move file blocks one at a time from the end of the disk to the leftmost free space block (until there are no gaps remaining between file blocks)

nextFreeSpace = 0
lastFileBlock = len(fileIds) - 1

while True:
    while fileIds[nextFreeSpace] != EMPTY: nextFreeSpace += 1
    while fileIds[lastFileBlock] == EMPTY: lastFileBlock -= 1
    if nextFreeSpace >= lastFileBlock:
        break
    fileIds[nextFreeSpace] = fileIds[lastFileBlock]
    fileIds[lastFileBlock] = EMPTY

render()

# 022111222......
# 0099811188827773336446555566..............

# Count the results
total = 0

# To calculate the checksum, add up the result of multiplying each of these blocks' position with the file ID number it contains.

for i in range(len(fileIds)):
    value = fileIds[i]
    if value == EMPTY: break
    total += i * value

print(total)
# 5683949361 is too low