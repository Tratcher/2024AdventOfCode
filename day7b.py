print("hello!")

input = """190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20"""

file = open("day7input.txt", "r")
input = file.read()

lines = input.splitlines()

total = 0

def check_equation(testValue, equation, index, currentValue, debug):
    if currentValue > testValue:
        return False
    if index == len(equation):
        if currentValue == testValue:
            print(f"{testValue}={debug}; {equation}")
            return True
        else:
            return False
    return check_equation(testValue, equation, index + 1, currentValue + equation[index], debug + '+' + str(equation[index])) \
        or check_equation(testValue, equation, index + 1, currentValue * equation[index], debug + '*' + str(equation[index])) \
        or check_equation(testValue, equation, index + 1, int(str(currentValue) + str(equation[index])), debug + '||' + str(equation[index]))

for line in lines:
    split = line.index(':')
    testValue = int(line[:split])
    parts = line[split + 2:].split(' ')
    equation = [int(x) for x in parts]
    if check_equation(testValue, equation, 1, equation[0], str(equation[0])):
        total += testValue

print(total)