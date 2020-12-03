#!/usr/bin/python

def InitializeGrid(f):
  grid = []
  for line in f:
    grid.append(list(line.rstrip()))
  return grid

def Downhill(grid, x_step, y_step):
  trees = 0
  x = 0
  y = 0
  while y < len(grid) - 1:
    x = (x + x_step) % len(grid[y])
    y = y + y_step
    if grid[y][x] == '#':
      trees += 1
  return trees

f = open('3.data')

grid = InitializeGrid(f)
total = (Downhill(grid, 1, 1) * 
        Downhill(grid, 3, 1) *
        Downhill(grid, 5, 1) *
        Downhill(grid, 7, 1) *
        Downhill(grid, 1, 2))

print total


