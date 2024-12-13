print("hello!")

input = """xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"""

file = open("day3input.txt", "r")
input = file.read()

print(input)

def is_valid_mul(text, offset):
    if len(text) - offset < 8: # mul(0,0), min length
        return { 'valid': False }
    print(text[offset:offset+8])
    if text[offset:offset+4] != "mul(":
        return { 'valid': False }
    index_comma = text.find(',', offset+4)
    if index_comma == -1:
        return { 'valid': False }
    num1text = text[offset+4:index_comma]
    print(num1text)
    if not num1text.isdigit():
        return { 'valid': False }
    index_paren = text.find(')', index_comma + 1)
    if index_paren == -1:
        return { 'valid': False }
    num2text = text[index_comma+1:index_paren]
    print(num2text)
    if not num2text.isdigit():
        return { 'valid': False }
    result = int(num1text) * int(num2text)
    return { 'valid': True, 'result': result, 'end': index_paren}
    
index = 0
total = 0
enabled = True
while index < len(input):
    if input.startswith("do()", index):
        enabled = True
        index += len("do()")
        print("do()")
        continue

    if input.startswith("don't()", index):
        enabled = False
        index += len("don't()")
        print("don't()")
        continue

    if not enabled:
        index += 1
        # print("skip")
        continue

    status = is_valid_mul(input, index)
    if status['valid']:
        total += status['result']
        index = status['end']
    index += 1

print(total)