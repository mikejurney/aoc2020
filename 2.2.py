#!/usr/bin/python

f = open("2.data")

valid_count = 0
for line in f:
  (span, char, pwd) = line.split()
  (pos1, pos2) = span.split('-')
  pos1 = int(pos1)
  pos2 = int(pos2)
  char = char[0]
  pwd = '0' + pwd
  pos1 = pwd[pos1] == char
  pos2 = pwd[pos2] == char
  if pos1 and not pos2:
    valid_count += 1
  if pos2 and not pos1:
    valid_count += 1
print valid_count
