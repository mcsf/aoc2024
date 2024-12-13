#!/usr/bin/env python3

from sys import stdin
from functools import lru_cache


@lru_cache(maxsize=None)
def count(n: int, i):
    if i == 0:
        return 1
    if n == 0:
        return count(1, i - 1)
    if len(str(n)) % 2 == 0:
        s = str(n)
        a = int(s[:len(s)//2])
        b = int(s[len(s)//2:])
        return count(a, i - 1) + count(b, i - 1)
    return count(n * 2024, i - 1)


ns = [int(n) for n in next(stdin).strip().split(' ')]
print(sum(count(n, 25) for n in ns))
print(sum(count(n, 75) for n in ns))
