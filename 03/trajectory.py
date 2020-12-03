stepright = 3
stepdown = 1
treecount = 0
with open('03/input.txt') as course:
    next(course)
    linenum = 2
    for row in course:
        print(list(row.rstrip()))
        print('position(index) is ' + str(stepright))
        
        if list(row.rstrip())[stepright] == '#':
            treecount = treecount + 1
            print('treecount is ' + str(treecount))
        print('row is ' + str(linenum))
        linenum = linenum + 1
        if stepright == 30:
            stepright = 2
        elif stepright == 29:
            stepright = 1
        elif stepright == 28:                
            stepright = 0
        else:
            stepright = stepright + 3
        print('')

from math import prod

with open(f'03/input.txt') as course:
    entries = [line.strip() for line in course]

def part1(entries, right=3, down=1):
    return sum((1 for i, entry in enumerate(entries[::down]) if entry[i * right % len(entry)] == '#'))


def part2(entries, movements:(int, int)):
    return prod((part1(entries, movement[0], movement[1]) for movement in movements))

if __name__ == '__main__':
    print(part1(entries))
    print(part2(entries, {(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)}))