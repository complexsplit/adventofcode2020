import bisect

li = []

with open('01/input.txt') as nums:
    for line in nums:
        bisect.insort(li, int(line.rstrip()))

il = li[::-1]

for x in li:
    for y in li:
        if x + y == 2020:
            print(x)
            print(y)

for a in li:
    for b in li:
        for c in li:
            if a + b + c == 2020:
                print(a)
                print(b)
                print(c)
