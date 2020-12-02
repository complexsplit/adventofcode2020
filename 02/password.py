with open('02/input.txt') as pwlist:
    counter = 0
    for line in pwlist:
        constraint, passwd = line.rstrip().split(':')
        countconstraint, charac = constraint.split()
        # print(countconstraint)
        xrange = range(int(countconstraint.split('-')[0]), int(countconstraint.split('-')[1])+1)
        # print(xrange)
        # print(list(passwd).count(charac))
        if list(passwd).count(charac) in xrange:
            print(passwd, charac, xrange)
            counter = counter + 1
    print(counter)

with open('02/input.txt') as pwlist2:
    counter2 = 0
    for line in pwlist2:
        constraint2, passwd2 = line.rstrip().split(':')
        countconstraint, charac2 = constraint2.split()
        pos1, pos2 = int(countconstraint.split('-')[0]), int(countconstraint.split('-')[1])
        print(pos1, pos2)
        if (list(passwd2)[pos1-1] == charac2) and (list(passwd2)[pos2-1] != charac2):
            print(passwd2, pos1, pos2, charac2)
            counter2 = counter2 + 1
        if (list(passwd2)[pos1-1] != charac2) and (list(passwd2)[pos2-1] == charac2):
            print(passwd2, pos1, pos2, charac2)
            counter2 = counter2 + 1
    print(counter2)

import re

with open("02/input.txt") as f:
    data_in = f.readlines()

valid = 0
for line in data_in:
    pos1, pos2, letter, skip, password = re.split('[: \-]', line)
    if (password[int(pos1) - 1] == letter) ^ (password[int(pos2) - 1] == letter):
        valid += 1

print(valid)