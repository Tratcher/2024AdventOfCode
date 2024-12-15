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

# attempt to move whole files to the leftmost span of free space blocks that could fit the file. Attempt to move each file exactly once in order of 
# decreasing file ID number starting with the file with the highest file ID number. If there is no span of free space to the left of a file that is 
# large enough to fit the file, the file does not move.

nextId = int((len(input) - 1) / 2)
idstart = len(fileIds) - 1

while nextId >= 0:
    idlength = 0
    print(f"Id: {nextId}")
    # find the id, count it's length
    while idstart >= 0:
        if fileIds[idstart] == nextId:
            idlength += 1
            if idstart == 0 or fileIds[idstart - 1] != nextId:
                break
        idstart -= 1

    print(f"Length: {idlength}")

    # find an empty space big enough for it
    emptyStart = 0
    while emptyStart < idstart:
        if fileIds[emptyStart] == EMPTY:
            emptyLength = 0
            while fileIds[emptyStart + emptyLength] == EMPTY: emptyLength += 1
            if emptyLength < idlength:
                emptyStart = emptyStart + emptyLength
                continue
            # move it
            for i in range(idlength):
                fileIds[emptyStart + i] = nextId
                fileIds[idstart + i] = EMPTY
            break
        emptyStart += 1
    nextId -= 1

render()

# 00992111777.44.333....5555.6666.....8888..

# Count the results
total = 0

# To calculate the checksum, add up the result of multiplying each of these blocks' position with the file ID number it contains.

for i in range(len(fileIds)):
    value = fileIds[i]
    if value != EMPTY:
        total += i * value

print(total)