#!/usr/bin/env python3

from sys import stdin
from re import findall
from itertools import count
from math import prod
from collections import Counter

robots = []
for line in stdin:
    ns = findall(r'[0-9+-]+', line.strip())
    a, b, c, d = (int(n) for n in ns)
    p = complex(a, b)
    v = complex(c, d)
    robots.append((p, v))

width, height = 101, 103

# Detect sample puzzle and ajust dimensions
if robots[0][0] == 4j:
    width, height = 11, 7


def move(p, v):
    p_next = p + v
    x = p_next.real % width
    y = p_next.imag % height
    return complex(x, y)


def is_tree(robots):
    points = set(p for p, _ in robots)

    # Is `p` the summit of an isosceles triangle of height >= 3?
    def has_triangle(p):
        return all(all((p + dy * 1j + dx) in points
                       for dx in range(-dy, dy+1))
                   for dy in range(1, 3))

    # Find a "summit", i.e. a point with two adjacent points on the following
    # row as follows:
    #
    #   *
    #  * *
    for p in points:
        left = p - 1 + 1j
        right = p + 1 + 1j

        # This aggressively assumes that, if the summit found is not the summit
        # of a larger triangle, there are no trees elsewhere in the map. This
        # works for my input and cuts execution time by 65%. If this does not
        # solve your puzzle, replace
        #
        #    return has_triangle(p)
        #
        # with
        #
        #   if has_triangle(p): return True
        #
        if left in points and right in points:
            return has_triangle(p)

    return False


for t in count(1):
    robots = [(move(p, v), v) for p, v in robots]

    if t == 100:
        mw, mh = width // 2, height // 2
        # Boolean algebra, collections.Counter and math.prod? Totally overkill,
        # but fun.
        quadrants = Counter(((p.real > mw) | (p.imag > mh) << 1)
                            for p, _ in robots
                            if p.real != mw and p.imag != mh)
        print(prod(quadrants.values()))

    if is_tree(robots):
        print(t)
        # draw(robots)
        break

# def draw(robots):
#     M = set(p for p, _ in robots)
#     for y in range(height):
#         for x in range(width):
#             print('#' if complex(x, y) in M else ' ', end='')
#         print('')
