print("hello!")

input = """125 17"""

file = open("day11input.txt", "r")
input = file.read()

stones = input.split(" ")

for blink in range(25):
    # print(stones)
    print(F"{blink}, {len(stones)}")

    i = 0
    while i < len(stones):
        # If the stone is engraved with the number 0, it is replaced by a stone engraved with the number 1.
        stone = stones[i]
        if stone == "0":
            stones[i] = "1"

        # If the stone is engraved with a number that has an even number of digits, it is replaced by two stones. The left half of the digits are engraved on the new left stone, 
        # and the right half of the digits are engraved on the new right stone. 
        elif len(stone) % 2 == 0:
            stones[i] = stone[:int(len(stone)/2)]
            i += 1
            righthalf = stone[int(len(stone)/2):]
            # (The new numbers don't keep extra leading zeroes: 1000 would become stones 10 and 0.)
            righthalf = str(int(righthalf))
            stones.insert(i, righthalf)
        
        # If none of the other rules apply, the stone is replaced by a new stone; the old stone's number multiplied by 2024 is engraved on the new stone.
        else:
            stones[i] = str(int(stone) * 2024)

        i += 1

print(stones)
print(len(stones))