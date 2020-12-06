#!/usr/bin/python

f = open('6.data')

groups = []
working_sets = []
for line in f:
  line = line.rstrip()
  if line == '':
    print working_sets
    groups.append(working_sets[0])
    for s in working_sets[1:]:
      groups[-1] = groups[-1] & s 
    print groups[-1]
    working_sets = []
  else:
    s = set()
    for char in line:
      s.add(char)
    working_sets.append(s)
groups.append(working_sets[0])
for s in working_sets[1:]:
  groups[-1] = groups[-1] & s 

total = 0
for s in groups:
  print len(s)
  total += len(s)

print total
