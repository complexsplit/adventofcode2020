f = open('13/input.txt')
lines=f.readlines()
pos=lines[0].strip()
sched = [x for x in lines[1].strip().split(',') if x != 'x']
# print(sched)

