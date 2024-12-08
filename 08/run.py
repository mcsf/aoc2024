#!/usr/bin/env python3

from sys import stdin
from collections import defaultdict
from itertools import combinations

A = defaultdict(set)  # Map freqs to sets of points
for y, line in enumerate(stdin):
    for x, c in enumerate(line.strip()):
        p = complex(x, y)
        if c != '.':
            A[c].add(p)
dim = p + 1+1j  # Capture map dimensions


def is_within(p, dim):
    return 0 <= p.real < dim.real and 0 <= p.imag < dim.imag


def antinodes_simple(a, b):
    for p in (a + (a - b), b - (a - b)):
        if is_within(p, dim):
            yield p


def antinodes_harmonic(a, b):
    delta = a - b
    p = a
    while is_within(p, dim):
        yield p
        p += delta
    p = b
    while is_within(p, dim):
        yield p
        p -= delta


N1 = set()
N2 = set()
for freq, antennae in A.items():
    for a, b in combinations(antennae, 2):
        for antinode in antinodes_simple(a, b):
            N1.add(antinode)
        for antinode in antinodes_harmonic(a, b):
            N2.add(antinode)

print(len(N1))
print(len(N2))
