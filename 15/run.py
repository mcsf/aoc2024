#!/usr/bin/env python3

from sys import stdin

# Populate both the regular and the expanded maps in one pass
grid_1 = {}
grid_2 = {}
for y, line in enumerate(stdin):
    if not line.strip():
        break
    for x, c in enumerate(line.strip()):
        grid_1[p_1 := complex(x, y)] = c
        grid_2[p_2 := complex(2 * x, y)] = c
        if c == '@':
            start_1 = p_1
            start_2 = p_2
            grid_2[p_2 + 1] = '.'
        elif c == '#':
            grid_2[p_2 + 1] = '#'
        elif c == 'O':
            grid_2[p_2 + 0] = '['
            grid_2[p_2 + 1] = ']'
        elif c == '.':
            grid_2[p_2 + 1] = '.'

width_1 = x + 1
width_2 = 2 * x + 1
height = y

# Parse move instructions as complex numbers
moves = []  # type: list[complex]
char_moves = {'>': 1, 'v': 1j, '<': -1, '^': -1j}
for line in stdin:
    moves += [char_moves[c] for c in line.strip()]


def can_move(p, move, grid):
    c = grid[p + move]
    if c == '#':
        return False
    if c == '.':
        return True
    if c == 'O' or move in (-1, 1):
        return can_move(p + move, move, grid)
    return (can_move(p + move, move, grid) and
            can_move(p + move + (1 if c == '[' else -1), move, grid))


def do_move(p, move, grid):
    c = grid[p + move]
    if c in 'O[]':
        do_move(p + move, move, grid)
    if c in '[]' and move in (-1j, 1j):
        do_move(p + move + (1 if c == '[' else -1), move, grid)
    grid[p + move] = grid[p]
    grid[p] = '.'


def run(start, grid):
    p = start
    for move in moves:
        if can_move(p, move, grid):
            do_move(p, move, grid)
            p += move
    return sum(100 * int(p.imag) + int(p.real)
               for p in grid if grid[p] in 'O[')


print(run(start_1, grid_1))
print(run(start_2, grid_2))
