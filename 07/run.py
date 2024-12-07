#!/usr/bin/env python3

from sys import stdin
from re import split
from operator import add, mul
from multiprocessing import Pool, freeze_support
from functools import partial


def concat(a, b):  # Faster than int(''.join(str(...
    n = b
    while n:
        a *= 10
        n //= 10
    return a + b


OPERATORS = [mul, add, concat]


def solve(line, base=2):
    target, *operands = line
    for i in range(base ** (len(operands) - 1)):
        acc = operands[0]
        for opd in operands[1:]:
            acc = OPERATORS[int(i % base)](acc, opd)
            if acc > target:
                break
            i //= base
        if acc == target:
            return target
    return 0


if __name__ == '__main__':
    freeze_support()
    lines = [list(map(int, split(r':?\s', line.strip()))) for line in stdin]
    pool = Pool()
    print(sum(pool.map(partial(solve, base=2), lines)))
    print(sum(pool.map(partial(solve, base=3), lines)))
