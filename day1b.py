print("hello!")

input = """3   4
4   3
2   5
1   3
3   9
3   3"""

file = open("day1input.txt", "r")
input = file.read()

print(input)

lines = input.splitlines()
print(lines)
start = []
end = []
for l in lines:
    parts = l.split()
    start.append(parts[0])
    end.append(parts[1])

print(start)
print(end)

counts = { }
for x in end:
    counts[x] = counts.get(x, 0) + 1

total = 0
for i in start:
    total += int(i) * counts.get(i, 0)

print(total)
# 2252576 too low, needs abs