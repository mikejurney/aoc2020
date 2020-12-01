#!/usr/bin/python

import random

def triple_nest(v):
  for a in v:
    for b in v[1:]:
      for c in v[2:]:
        if a + b + c == 2020:
          return a * b * c

def random_pick(v):
  while True:
    a = v[random.randrange(0, len(v)-1)] 
    b = v[random.randrange(0, len(v)-1)] 
    c = v[random.randrange(0, len(v)-1)] 
    if a + b + c == 2020:
      return a * b * c

f = open("1.data")

v = []
for i in f:
  v.append(int(i))

print triple_nest(v)
print random_pick(v)
