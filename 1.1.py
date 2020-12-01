#!/usr/bin/python

f = open("1.data")

v = []
for i in f:
  v.append(int(i))

for i in v:
  left = i
  right = 2020 - left
  if right in v:
    print left * right
