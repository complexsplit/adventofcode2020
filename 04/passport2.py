def validate_range(value, minv, maxv):
    if value.isnumeric() and int(value) >= minv and int(value) <= maxv:
        return True
    else:
        return False


def validate_hcl(value):
    if len(value) != 7:
        return False
    if value[0] != "#":
        return False
    for letter in value[1:]:
        if letter not in "0123456789" and letter not in "abcdef":
            return False
    return True


def validated(fields):
    oks = []
    for field in fields:
        ok = False
        key, value = field.split(":")
        if key == "cid":
            continue
        if key == "byr":
            ok = validate_range(value, 1920, 2002)
        if key == "iyr":
            ok = validate_range(value, 2010, 2020)
        if key == "eyr":
            ok = validate_range(value, 2020, 2030)
        if key == "hgt":
            if value[-2:] not in ["cm", "in"]:
                ok = False
            else:
                if value[-2:] == "cm":
                    ok = validate_range(value[:-2], 150, 193)
                elif value[-2:] == "in":
                    ok = validate_range(value[:-2], 59, 76)
        if key == "hcl":
            ok = validate_hcl(value)
        if key == "ecl":
            ok = value in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
        if key == "pid":
            if value.isnumeric() and len(value) == 9:
                ok = True
            else:
                ok = False
        oks.append(ok)
    return all(oks)


with open("04/input.txt", "r") as dfile:
    rows = dfile.readlines()

rows = [row.rstrip() for row in rows]

passports = []
current = ""
for row in rows:
    if row == "":
        passports.append(current)
        current = ""
    current += row + " "

passports.append(current)

valid = 0

required = set(["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"])

for passport in passports:
    fields = passport.split()
    keys = []
    for field in fields:
        key, _ = field.split(":")
        keys.append(key)
    if "cid" in keys:
        keys.remove("cid")
    if set(keys) == required and validated(fields):
        valid += 1

print(valid)
