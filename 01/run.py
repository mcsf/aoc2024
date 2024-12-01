#!/usr/bin/env python3

import collections
import fileinput
import re

left, right = [], []
for line in fileinput.input():
    l, r = re.split(r'\s+', line.strip())
    left.append(int(l))
    right.append(int(r))

left.sort()
right.sort()

print(sum(abs(a - b) for a, b in zip(left, right)))

occur = collections.Counter(right)
print(sum(a * occur[a] for a in left))
