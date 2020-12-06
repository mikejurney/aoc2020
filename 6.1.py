#!/usr/bin/python

f = open('6.data')

groups = [set()]
for line in f:
  line = line.rstrip()
  if line == '':
    groups.append(set())
  s = groups[-1]
  for char in line:
    s.add(char)

total = 0
for s in groups:
  total += len(s)

print total
