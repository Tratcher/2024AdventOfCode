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
    start.append(int(parts[0]))
    end.append(int(parts[1]))

print(start)
print(end)

start.sort()
end.sort()

print(start)
print(end)

diff = []
for i in range(len(start)):
    diff.append(abs(end[i] - start[i]))

print(diff)

total = sum(diff)
print(total)
# 2252576 too low, needs abs