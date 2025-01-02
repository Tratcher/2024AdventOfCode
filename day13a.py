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
    pX = int(prizeText[len("Prize: X="):commaIndex])
    pY = int(prizeText[commaIndex+len(", Y="):])

    best = None

    for a in range(1, 101):
        aaX = a * aX
        aaY = a * aY
        if aaX > pX or aaY > pY: break
        b1 = (pX - aaX) / bX
        b2 = (pY - aaY) / bY
        if b1 != int(b1) or b2 != int(b2) or b1 != b2: continue
        cost = int(a * 3 + b1)
        if best == None or cost < best: best = cost

    print(f"ax:{aX},ay:{aY}; bx:{bX},by:{bY}; px:{pX},py:{pY}; best:{best}")
    if best is not None: total += best

print(total)