#!/usr/bin/python

x = 0
step = 3
trees = 0
f = open('3.data')
for line in f:
  if list(line)[x] == '#':
    trees += 1
  x = (x + step) % (len(line) - 1)

print trees


