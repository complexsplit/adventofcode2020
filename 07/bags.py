import re

with open(f'07/input.txt') as course:
    entries = [line.strip() for line in course]

bags = dict()

for x in entries:
    splitbag = re.split('bags |bag', x)[:-1] # ['mirrored magenta ', ' contain 5 drab teal ', ', 3 striped bronze ', ', 3 striped magenta ', ', 5 dark tan ']
    parentbag, childbags = splitbag[0].strip(), [' '.join(z.strip().split(' ')[2:]) for z in splitbag[1:]]
    bags[parentbag] = childbags

def contains(outerbag):
    return bags[outerbag]

goldbags = []

def accum(baglist):
    for x in baglist:
        if 'shiny gold' in bags[x]:
            goldbags.append(x)

print(len(goldbags))

