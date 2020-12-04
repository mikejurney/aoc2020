#!/usr/bin/python

REQUIRED_FIELDS = {
    'byr',
    'iyr',
    'eyr',
    'hgt',
    'hcl',
    'ecl',
    'pid',
}

OPTIONAL_FIELDS = {
    'cid',
}

f = open('4.data')

def Validate(passport):
  passport_fields = set() 
  for field in passport.split(' '):
    passport_fields.add(field.split(':')[0])
  if passport_fields == REQUIRED_FIELDS:
    return True
  if passport_fields == REQUIRED_FIELDS | OPTIONAL_FIELDS:
    return True
  return False 

valid_passports = 0

passport = ''
for line in f:
  line = line.rstrip()
  if len(line) == 0:
    if Validate(passport[1:]):
      valid_passports += 1
    passport = ''
  else:
    passport = passport + ' ' + line
if Validate(passport[1:]):
  valid_passports += 1

print valid_passports

