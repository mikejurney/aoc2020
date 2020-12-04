#!/usr/bin/python

import re

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

def ValidateRange(x, low, high):
  return int(x) >= low and int(x) <= high

def ValidateRegexp(x, regexp):
  try:
    re.match(regexp, x).groups()
    return True
  except:
    return False
  return False

def ValidateHgt(x):
  regexp = '^(\d+)(cm|in)$'
  if ValidateRegexp(x, regexp):
    (mag, unit) = re.match(regexp, x).groups()
    if unit == 'cm':
      return ValidateRange(int(mag), 150, 193)
    if unit == 'in':
      return ValidateRange(int(mag), 59, 76)
  return False
    
VALIDATORS = {
    'byr': lambda x: ValidateRange(x, 1920, 2002),
    'iyr': lambda x: ValidateRange(x, 2010, 2020),
    'eyr': lambda x: ValidateRange(x, 2020, 2030),
    'hgt': lambda x: ValidateHgt(x),
    'hcl': lambda x: ValidateRegexp(x, '^#[0-9a-f]{6}$'),
    'ecl': lambda x: ValidateRegexp(x,'^amb|blu|brn|gry|grn|hzl|oth$'),
    'pid': lambda x: ValidateRegexp(x, '^\d{9}$'),
    'cid': lambda x: True
}

def Validate(passport):
  passport_fields = set() 
  for tok in passport.split(' '):
    (field, value) = tok.split(':')
    if VALIDATORS[field](value):
      passport_fields.add(field)
  if passport_fields == REQUIRED_FIELDS:
    return True
  if passport_fields == REQUIRED_FIELDS | OPTIONAL_FIELDS:
    return True
  return False 


f = open('4.data')
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

