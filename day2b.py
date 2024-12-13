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

def is_safe(values):
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
    return safe and (increasting or decreasing)

def is_safe_skip(values):
    for x in range(0, len(values)):
        copy = values.copy()
        copy.pop(x)
        if is_safe(copy):
            return True
    return False

total = 0
for l in lines:
    values = list(map(int, l.split()))
    print(values)
    if is_safe(values) or is_safe_skip(values):
        total += 1
        print('safe')

print(total)