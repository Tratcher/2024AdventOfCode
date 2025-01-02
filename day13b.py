import math


print("hello!")

input = """Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=8400, Y=5400

Button A: X+26, Y+66
Button B: X+67, Y+21
Prize: X=12748, Y=12176

Button A: X+17, Y+86
Button B: X+84, Y+37
Prize: X=7870, Y=6450

Button A: X+69, Y+23
Button B: X+27, Y+71
Prize: X=18641, Y=10279"""


file = open("day13input.txt", "r")
input = file.read()

lines = input.splitlines()

total = 0

for mIndex in range(0, len(lines), 4):
    buttonAText = lines[mIndex]
    buttonBText = lines[mIndex + 1]
    prizeText = lines[mIndex + 2]
    # blank line mIndex + 3

    commaIndex = buttonAText.find(',')
    aX = int(buttonAText[len("Button A: X+"):commaIndex])
    aY = int(buttonAText[commaIndex+len(", Y+"):])
    commaIndex = buttonBText.find(',')
    bX = int(buttonBText[len("Button B: X+"):commaIndex])
    bY = int(buttonBText[commaIndex+len(", Y+"):])
    commaIndex = prizeText.find(',')
    pX = int(prizeText[len("Prize: X="):commaIndex]) + 10000000000000
    pY = int(prizeText[commaIndex+len(", Y="):]) + 10000000000000

    b = round((pX*aY/aX - pY)/(bX*aY/aX - bY), 3) # round a little to account for float imprecision, but not too much, we don't want to include real fractional values
    a = (pX - b*bX)/aX
    cost = int(3 * a + b)

    print(f"ax:{aX},ay:{aY}; bx:{bX},by:{bY}; px:{pX},py:{pY}; a:{a},b:{b}; best:{cost}")
    if a == int(a): total += cost

print(total)
# 65408147403533 is too low
# 78922452919552 is too low
# 87596249540359 is correct!
# 89516009073810 is too high
