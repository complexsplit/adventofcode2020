import re
counter = 0
fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid']

with open(f'04/input.txt') as f:
    entries = f.read()

passportstemp = entries.split('\n\n') # splint on blank lines
passportssplit = [re.split('\n| ', x) for x in passportstemp] # split newlines and spaces

def validate(year, checktype):
    if checktype == 'iyr':
        if year >= 2010 and year <= 2020:
            return True
        else:
            return False
    if checktype == 'byr':
        if year >= 1920 and year <= 2002:
            return True
        else:
            return False
    if checktype == 'eyr':
        if year >= 2020 and year <= 2030:
            return True
        else:
            return False

# other validators skipped

for x in passportssplit:
    passfields = set([re.split(':', z)[0] for z in x])
    if set(fields).difference(passfields) in (set(), {'cid'}):
        counter = counter + 1

print(counter)

