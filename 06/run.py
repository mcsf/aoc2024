#!/usr/bin/env python3

from sys import stdin
from multiprocessing import Pool, freeze_support
from functools import partial

# Build sets of Points and Obstacles
P = set()  # type: set[complex]
O = set()  # type: set[complex]  # noqa: E741
for y, line in enumerate(stdin):
    for x, c in enumerate(line.strip()):
        p = complex(x, y)
        if c == '^':
            start = p
        elif c == '#':
            O.add(p)
        P.add(p)

# Vary (x, y) according to rotation r
ROT = [1, 1j, -1, -1j]


# Capture all visited positions
def walk():
    p = start  # initial position
    r = 3      # initial rotation, facing up
    V = set()  # set[complex]
    while p in P:
        V.add(p)
        if (ahead := p + ROT[r]) in O:
            r = (r + 1) % 4
        else:
            p = ahead
    return V


# Walk along visited points looking for loops by placing hypothetical obstacles
def is_obstacle(start: complex,      # Pass globals explicitly
                P: set[complex],     # due to
                ROT: list[complex],  # multiprocessing
                O: set[complex],     # constraints.

                o: complex):         # 'o' is the test subject

    # This time, track visits with rotation too
    Vr = set()  # type: set[tuple[complex, int]]
    p = start
    r = 3
    O = O | {o}  # Don't mutate O, make a copy # noqa: E741
    while p in P:
        if (p, r) in Vr:
            return True
        Vr.add((p, r))
        if (ahead := p + ROT[r]) in O:
            r = (r + 1) % 4
        else:
            p = ahead
    return False


if __name__ == '__main__':
    freeze_support()
    pool = Pool()
    print(len(V := walk()))
    task = partial(is_obstacle, start, P, ROT, O)
    print(sum(1 for v in pool.map(task, V) if v))
