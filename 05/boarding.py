with open(f'05/input.txt') as course:
    entries = [line.strip() for line in course]

def seatid(boardingpass):
    row, seatnum = boardingpass[:7], boardingpass[7:]
    low = 0
    high = 127
    counter = 6
    for x in list(row):
        if x == 'B':
            low = low + (2 ** counter)
        if x == 'F':
            high = high - (2 ** counter)
        counter -= 1
    print(low, high)
    seatlow = 0
    seathigh = 7
    seatcounter = 2
    for y in list(seatnum):
        if y == 'R':
            seatlow = seatlow + (2 ** seatcounter)
        if y == 'L':
            seathigh = seathigh - (2 ** seatcounter)
        seatcounter -= 1
    print(seatlow, seathigh)
    return low * 8 + seatlow

knownseats = [seatid(x) for x in entries]
knownseats.sort()

for x in range(1,842):
    if x not in knownseats and x-1 in knownseats and x+1 in knownseats:
        print(x)