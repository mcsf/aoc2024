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


# Capture all visited positions
def walk():
    p = start  # initial position
    r = -1j    # initial rotation
    V = set()  # set[complex]
    while p in P:
        V.add(p)
        if (ahead := p + r) in O:
            r *= 1j
        else:
            p = ahead
    return V


# Walk along visited points looking for loops by placing hypothetical obstacles
def is_obstacle(start: complex,      # Pass globals explicitly
                P: set[complex],     # due to multiprocessing
                O: set[complex],     # constraints.

                o: complex):         # 'o' is the test subject

    # This time, track visits with rotation too
    Vr = set()  # type: set[tuple[complex, complex]]
    p = start
    r = -1j
    O = O | {o}  # Don't mutate O, make a copy # noqa: E741
    while p in P:
        if (p, r) in Vr:
            return True
        Vr.add((p, r))
        if (ahead := p + r) in O:
            r *= 1j
        else:
            p = ahead
    return False


if __name__ == '__main__':
    freeze_support()
    pool = Pool()
    print(len(V := walk()))
    task = partial(is_obstacle, start, P, O)
    print(sum(1 for v in pool.map(task, V) if v))
