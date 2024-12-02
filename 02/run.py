#!/usr/bin/env python3

import fileinput


def find_bad_level(ns):
    pitch = (ns[1] - ns[0]) >= 0
    for i, (a, b) in enumerate(zip(ns, ns[1:])):
        diff = b - a
        dist = diff if diff >= 0 else -diff
        if pitch != (diff >= 0) or dist < 1 or dist > 3:
            return i


def is_safe(ns):
    return find_bad_level(ns) is None


def is_tolerably_safe(ns):
    return is_safe(ns) \
            or any(find_bad_level(without(ns, i)) is None
                   for i in range(len(ns)))


def without(xs, i):
    return xs[:i] + xs[i+1:]


ns = [[int(n) for n in line.strip().split(' ')]
      for line in fileinput.input()]

print(sum(1 for ns in ns if is_safe(ns)))
print(sum(1 for ns in ns if is_tolerably_safe(ns)))
