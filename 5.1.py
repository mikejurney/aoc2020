#!/usr/bin/python

import argparse

arg_parser = argparse.ArgumentParser(description='Advent of Code: Day 5, problem 1')
arg_parser.add_argument('--test',
    type=bool, default=False, help='Verify correctness with test data.')
args = arg_parser.parse_args()

def Partition(spec, low, high, sep_low='F', sep_high='B'):
  #print('Partitioning: %s (%d, %d)' % (spec, low, high))
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

def VerifySeatId(seat):
  (seat, expected_id) = seat.split(' ')
  return SeatId(seat) == int(expected_id)

if args.test:
  f = open('5.testdata')
else:
  f = open('5.data')

max_id = 0
for seat in f:
  seat = seat.rstrip()
  if args.test:
    print('%s (%s)' % (seat, VerifySeatId(seat)))
  else:
    seat_id = SeatId(seat)
    print('%s: %d' % (seat, seat_id))
    max_id = max(max_id, seat_id)
print max_id

