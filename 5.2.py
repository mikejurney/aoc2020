#!/usr/bin/python

def Partition(spec, low, high, sep_low='F', sep_high='B'):
  if low == high:
    return high
  if spec[0] == sep_low:
    high = high - ((high - low + 1) // 2)
  elif spec[0] == sep_high:
    low = high - ((high - low) / 2)
  return Partition(spec[1:], low, high, sep_low, sep_high)

def SeatId(seat):
  row = Partition(seat, 0, 127)
  column = Partition(seat[-3:], 0, 7, sep_low='L', sep_high='R')
  return row * 8 + column

f = open('5.data')

seat_ids = []
for seat in f:
  seat = seat.rstrip()
  seat_ids.append(SeatId(seat))
seat_ids.sort()

for i in range(1, len(seat_ids) -1):
  if seat_ids[i] - seat_ids[i-1] == 2:
    print seat_ids[i] - 1
    break
