with open(f'11/input.txt') as course:
    entries = [list(line.strip()) for line in course]

height, width = len(entries)-1, len(entries[0])-1
# print(entries)

from array import *
from copy import deepcopy


def has_four_occupied(grid, xpos, ypos):
    if (xpos == 0 and ypos == 0) or (xpos == height and ypos == width) or (xpos == 0 and ypos == width) or (xpos == height and ypos == 0):
        return False
    if (xpos == 0 and ypos != 0) or (xpos == 0 and ypos != width):
        # print('pos is ' + str(grid) + ' ' + str(xpos) + ' ' + str(ypos))
        if [grid[0][ypos-1] == '#', grid[1][ypos-1] == '#', grid[1][ypos] == '#', grid[1][ypos+1] == '#', grid[0][ypos+1] == '#'].count(True) >= 4:
            return True
    if (xpos == height and ypos !=0) or (xpos == height and ypos != width):
        if [grid[height][ypos-1] == '#', grid[height-1][ypos-1] == '#', grid[height-1][ypos] == '#', grid[height-1][ypos+1] == '#', grid[height][ypos+1] == '#'].count(True) >= 4:
            return True
    if (ypos == 0 and xpos != 0) or (ypos == 0 and xpos != height):
        if [grid[xpos-1][ypos] == '#', grid[xpos-1][ypos+1] == '#', grid[xpos][ypos+1] == '#', grid[xpos+1][ypos+1] == '#', grid[xpos+1][ypos] == '#'].count(True) >= 4:
            return True
    if (ypos == width and xpos != 0) or (ypos == width and xpos != height):
        if [grid[xpos-1][ypos] == '#', grid[xpos-1][ypos-1] == '#', grid[xpos][ypos-1] == '#', grid[xpos+1][ypos-1] == '#', grid[xpos+1][ypos] == '#'].count(True) >= 4:
            return True
    if [grid[xpos-1][ypos] == '#', grid[xpos-1][ypos+1] == '#', grid[xpos][ypos+1] == '#', grid[xpos+1][ypos+1] == '#', grid[xpos+1][ypos] == '#', grid[xpos+1][ypos-1] == '#', grid[xpos][ypos-1] == '#', grid[xpos-1][ypos-1] == '#'].count(True) >= 4:
        return True
    else:
        return False

def fill_and_empty(grid):
    for x in range(0, height):
        for y in range(0, width):
            if grid[x][y] == 'L':
                grid[x][y] = '#'
    for a in range(0, height):
        for b in range(0, width):
            if grid[a][b] == '#' and has_four_occupied(grid, a, b):
                grid[a][b] = 'L'

def count_filled(grid):
    counter = 0
    for x in entries:
        counter += x.count('L')
    return counter

match = False

while True:
    entries_ = deepcopy(entries)
    fill_and_empty(entries_)
    print(entries_)
    print(count_filled(entries))
    entries = entries_

