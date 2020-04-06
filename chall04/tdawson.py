#!/usr/bin/python3
# Python 3.6.9

import sys

def error(error_msg):
    sys.exit('Error: ' + error_msg)

size = input()
if not (size.isdigit()):
    error('Not a positive integer.')
size = int(size)

grid = []
for _ in range(size):
    row = input()
    if len(row) != size:
        error('Input length different than size.')
    if not all(c in ' #.' for c in row):
        error('Forbidden characters in input.')
    grid.append(list(row))

settled = False
while (not settled):
    settled = True
    for row in range(size - 2, -1, -1):
        for col, c in enumerate(grid[row]):
            if (c is '.' and grid[row+1][col] is ' '):
                settled = False
                grid[row+1][col], grid[row][col] = grid[row][col], grid[row+1][col]

for row in grid:
    print(''.join(row))
