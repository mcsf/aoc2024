#!/usr/bin/env python3

from sys import stdin
from itertools import groupby


def fix(update):
    fixed = False
    for i, a in enumerate(update):
        for j in range(i + 1, len(update)):
            b = update[j]
            if (b, a) in rules:
                fixed = True
                for k in range(j, i, -1):
                    if (update[k-1], update[k]) in rules:
                        break
                    update[k-1], update[k] = update[k], update[k-1]
    return fixed


def middle(update):
    return update[len(update)//2]


lines = (line.strip() for line in stdin)
parts = (list(xs) for ok, xs in groupby(lines, lambda s: s != '') if ok)

rules = {tuple(map(int, line.split('|'))) for line in next(parts)}
updates = [list(map(int, line.split(','))) for line in next(parts)]

sums = [0, 0]
for u in updates:
    sums[int(fix(u))] += middle(u)


print(*sums, sep='\n')
