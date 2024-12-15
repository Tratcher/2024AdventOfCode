print("hello!")

input = """47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47"""

file = open("day5input.txt", "r")
input = file.read()

lines = input.splitlines()

divider = lines.index("")

rule_lines = lines[:divider]
update_pages = lines[divider+1:]

rules = []
for line in rule_lines:
    rules.append(line.split("|"))

def is_ordered_list(pages):
    for rule in rules:
            page0_index = pages.index(rule[0]) if rule[0] in pages else -1
            page1_index = pages.index(rule[1]) if rule[1] in pages else -1
            if page0_index != -1 and page1_index != -1 and page0_index > page1_index:
                return False
    return True

def is_ordered_pair(valueA, valueB):
    for rule in rules:
         if rule[0] == valueA and rule[1] == valueB:
              return True
         if rule[0] == valueB and rule[1] == valueA:
              return False
    return True

def order(pages):
     print("Before: " + str(pages))
     while True:
        for i in range(0, len(pages) - 1):
            valueA = pages[i]
            valueB = pages[i+1]
            if not is_ordered_pair(valueA, valueB):
                pages[i] = valueB
                pages[i+1] = valueA
        if is_ordered_list(pages):
            print("After: " + str(pages))
            break

total = 0
for update in update_pages:
    pages = update.split(",")
    if not is_ordered_list(pages):
        order(pages)
        total += int(pages[int(len(pages)/2)])

print(total)