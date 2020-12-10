with open(f'10/input.txt') as course:
    entries = sorted([int(line.strip()) for line in course])

maxdiff = 3
currvol = 0
numones, numthrees = 0, 0

for x in entries:
    if x == currvol + 1:
        currvol += 1
        numones +=1
        print('a one')
        print('currvol is ' + str(currvol))
    if x == currvol + 2:
        # never happens?
        print('!!!!!')
        pass
    if x == currvol + 3:
        currvol += 3
        numthrees += 1
        print('a three')
        print('currvol is ' + str(currvol))

print(numones)
print(numthrees)

numoptions = 0
endvoltage = max(entries) + 3
print('computer voltage is ' + str(endvoltage))
currvol = endvoltage

# part 2

from functools import lru_cache

@lru_cache(maxsize=None)
def explore(num):
    if num == entries[-1]:
        return 1
    # print(num)
    return sum(explore(num + i) for i in range(1, 4) if num + i in entries)
    

print(explore(0))