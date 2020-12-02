#!/usr/bin/python

f = open("2.data")

valid_count = 0
for line in f:
  (span, char, pwd) = line.split()
  (req_min, req_max) = span.split('-')
  req_min = int(req_min)
  req_max = int(req_max)
  char = char[0]
  count = pwd.count(char)
  if count >= req_min and count <= req_max:
    valid_count += 1
print valid_count
