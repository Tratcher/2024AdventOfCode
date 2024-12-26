import math

print("hello!")

input = """125 17"""

file = open("day11input.txt", "r")
input = file.read()

items = input.split(" ")
itterations = 75

number_stats = {}

class stats:
    def __init__(self):
        self.itteration_totals = { }
    def __repr__(self):
        return f"{self.itteration_totals}"

def explore(stone, itterations):
    new_stones = 1
    start_stone = stone

    if itterations == 0: return 1

    for i in range(itterations, 0, -1):

        stat = number_stats.get(stone)
        if stat == None:
            stat = stats()
            number_stats[stone] = stat
        
        # Have we already solved this variation?
        itteration_total = stat.itteration_totals.get(i)
        if itteration_total != None:
            new_stones += itteration_total - 1
            break

        # If the stone is engraved with the number 0, it is replaced by a stone engraved with the number 1.

        digits = 1 if stone == 0 else int(math.log(stone, 10)) + 1

        if stone == 0:
            stone = 1

        # If the stone is engraved with a number that has an even number of digits, it is replaced by two stones. The left half of the digits are engraved on the new left stone, 
        # and the right half of the digits are engraved on the new right stone. (The new numbers don't keep extra leading zeroes: 1000 would become stones 10 and 0.)
        elif digits % 2 == 0:
            halflength = int(digits/2)
            base = int(math.pow(10, halflength))
            lefthalf = int(stone / base)
            righthalf = int(stone % base)
            # print(f"{stone}: {digits}/2={halflength}, base={base}, left={lefthalf}, right={righthalf}")
            stone = lefthalf
            new_stones += explore(righthalf, i - 1)
        
        # If none of the other rules apply, the stone is replaced by a new stone; the old stone's number multiplied by 2024 is engraved on the new stone.
        else:
            stone = stone * 2024
    
    # if itterations > 35: print(number_stats)
    if itterations > 35: print(f"{stone}, {total}")

    number_stats[start_stone].itteration_totals[itterations] = new_stones

    return new_stones


total = 0
for item in items:
    total += explore(int(item), itterations)
    print(f"{item}, {total}")

print(len(number_stats))
# print(number_stats)
print(total)