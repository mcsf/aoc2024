#!/usr/bin/env python3

from sys import stdin
from re import split
from operator import add, mul


def concat(a, b):  # Faster than int(''.join(str(...
    n = b
    while n:
        a *= 10
        n //= 10
    return a + b


OPERATORS = [mul, add, concat]


def is_solvable(target, operands, base=2):
    for i in range(base ** (len(operands) - 1)):
        acc = operands[0]
        for opd in operands[1:]:
            acc = OPERATORS[int(i % base)](acc, opd)
            if acc > target:
                break
            i //= base
        if acc == target:
            return True


pt1 = pt2 = 0
for line in stdin:
    target, *operands = list(map(int, split(r':?\s', line.strip())))
    if is_solvable(target, operands, base=2):
        pt1 += target
    if is_solvable(target, operands, base=3):
        pt2 += target

print(pt1)
print(pt2)
