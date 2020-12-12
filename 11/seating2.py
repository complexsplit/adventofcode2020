from copy import deepcopy
from functools import lru_cache

puzzle = open('11/input.txt').read()
plane = list(map(list, puzzle.splitlines()))
deltas = [
    (-1, -1), (-1, 0), (-1, 1),
    (0, -1), (0, 1),
    (1, 0), (1, -1), (1, 1),
]
all_seats = [(row_idx, col_idx)
             for row_idx, row in enumerate(plane)
             for col_idx, seat in enumerate(row)
             if seat != '.']


def get_seats(get_adjacent, empty_rule):
    grid = deepcopy(plane)
    while True:
        grid_ = deepcopy(grid)
        for row, col in all_seats:
            seat = grid[row][col]
            adjacent = get_adjacent(grid, row, col)
            if seat == 'L' and adjacent == 0:
                grid_[row][col] = '#'
            elif seat == '#' and adjacent >= empty_rule:
                grid_[row][col] = 'L'
        if grid_ == grid:
            return sum(seat == '#' for line in grid for seat in line)
        grid = grid_


def get_adjacent_1(grid, y, x):
    adj = 0
    for y_, x_ in get_neighbours(y, x):
        if grid[y_][x_] == '#':
            adj += 1
    return adj


@lru_cache(maxsize=len(plane) * len(plane[0]))
def get_neighbours(y, x):
    ret = []
    for delta_y, delta_x in deltas:
        if 0 <= y + delta_y < len(plane) and 0 <= x + delta_x < len(plane[0]):
            ret.append((y + delta_y, x + delta_x))
    return ret


def get_adjacent_2(grid, y, x):
    adj = 0
    for delta_y, delta_x in deltas:
        temp_y, temp_x = y + delta_y, x + delta_x
        while 0 <= temp_y < len(grid) and 0 <= temp_x < len(grid[0]):
            if grid[temp_y][temp_x] == 'L':
                break
            elif grid[temp_y][temp_x] == '#':
                adj += 1
                break
            temp_y += delta_y
            temp_x += delta_x
    return adj


print(get_seats(get_adjacent_1, 4))
print(get_seats(get_adjacent_2, 5))
