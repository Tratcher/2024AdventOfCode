print("hello!")

input = """7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9"""

file = open("day2input.txt", "r")
input = file.read()

print(input)

lines = input.splitlines()
print(lines)

total = 0
for l in lines:
    values = list(map(int, l.split()))
    print(values)
    increasting = True
    decreasing = True
    safe = True
    for i in range(1, len(values)):
        v0 = values[i-1]
        v1 = values[i]
        dif = abs(v1-v0)
        increasting = increasting and v1 > v0
        decreasing = decreasing and v0 > v1
        safe = safe and 1 <= dif and dif <= 3
    if safe and (increasting or decreasing):
        total += 1
        print('safe')

print(total)