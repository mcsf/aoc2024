#!/usr/bin/env python3

from sys import stdin
from operator import add

# Build sets of Points and Obstacles
P = set()  # type: set[tuple[int, int]]
O = set()  # type: set[tuple[int, int]]  # noqa: E741
for y, line in enumerate(stdin):
    for x, c in enumerate(line.strip()):
        if c == '^':
            start = x, y  # Initial position
        elif c == '#':
            O.add((x, y))
        P.add((x, y))


# Vector addition
def vadd(*vs): return tuple(map(add, *vs))


# Vary (x, y) according to rotation r
ROT = [(1, 0), (0, 1), (-1, 0), (0, -1)]

# PART 1
#
# Capture all visited positions

V = set()  # type: set[tuple[int, int]]
p = start  # initial position
r = 3      # initial rotation, facing up

while p in P:
    V.add(p)
    if (ahead := vadd(p, ROT[r])) in O:
        r = (r + 1) % 4
    else:
        p = ahead

# PART 2
#
# Walk along visited points looking for loops by placing hypothetical obstacles

count = 0

for maybe_obstacle in V:
    # This time, track visits with rotation too
    Vr = set()  # type: set[tuple[int, int, int]]
    p = start
    r = 3

    O.add(maybe_obstacle)

    while p in P:
        if (*p, r) in Vr:
            count += 1
            break
        Vr.add((*p, r))
        if (ahead := vadd(p, ROT[r])) in O:
            r = (r + 1) % 4
        else:
            p = ahead

    O.remove(maybe_obstacle)

print(len(V))
print(count)
