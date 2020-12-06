import re
with open('04_input.txt', 'r') as file:
    passports = file.read().split("\n\n")

valid = 0

def passport_is_valid(passport):
    if not re.match(r'^\d{4}$', passport.get('byr', '')) or not 1920 <= int(passport['byr']) <= 2002:
        return False
    if not re.match(r'^\d{4}$', passport.get('iyr', '')) or not 2010 <= int(passport['iyr']) <= 2020:
        return False
    if not re.match(r'^\d{4}$', passport.get('eyr', '')) or not 2020 <= int(passport['eyr']) <= 2030:
        return False
    if re.match(r'^(\d+)(in|cm)$', passport.get('hgt', '')):
        if passport['hgt'][-2:] == 'cm' and not 150 <= int(passport['hgt'][:-2]) <= 193:
            return False
        if  passport['hgt'][-2:] == 'in' and not 59 <= int(passport['hgt'][:-2]) <= 76:
            return False
    else:
        return False
    if not re.match(r'^#[\da-f]{6}$', passport.get('hcl', '')):
        return False
    if not passport.get('ecl', '') in 'amb blu brn gry grn hzl oth'.split():
        return False
    return bool(re.match(r'^\d{9}$', passport.get('pid', '')))

for passport in passports:
    passport = dict(field.split(':') for field in passport.replace('\n', ' ').split(' '))
    print(passport)
    if passport_is_valid(passport):
        valid += 1

print(valid)