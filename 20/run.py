#!/usr/bin/env python3

from heapq import heappush, heappop
from dataclasses import dataclass
from collections import defaultdict
from math import inf


class Graph(dict):
    def __init__(self, it):
        super()
        for y, line in enumerate(open(0)):
            for x, c in enumerate(line.strip()):
                p = complex(x, y)
                if c == 'S':
                    self.start = p
                    c = '.'
                elif c == 'E':
                    self.end = p
                    c = '.'
                self[p] = c
        self.is_sample = len(self) == 225


@dataclass
class QueueItem:
    time: int
    pos: complex
    path: list[complex]

    def __lt__(self, other):
        return self.time < other.time


G = Graph(open(0))

queue = [QueueItem(0, G.start, [G.start])]
times = defaultdict(lambda: inf, {G.start: 0})
while queue:
    node = heappop(queue)

    if times[node.pos] < node.time:
        continue

    times[node.pos] = node.time

    if node.pos == G.end:
        break

    for d in [1, -1, 1j, -1j]:
        pos = node.pos + d
        if G.get(pos) == '.' and times[pos] >= node.time + 1:
            heappush(queue, QueueItem(node.time + 1, pos, node.path + [pos]))

pt1 = 0
min_saved = 1 if G.is_sample else 100
for pos in node.path:
    for d in [2, -2, 2j, -2j]:
        p = pos + d
        if times[p] + 2 + min_saved <= times[pos]:
            pt1 += 1
print(pt1)  # sample expects 44 with min_saved=1


def dist(p1, p2):
    return abs(p1.real - p2.real) + abs(p1.imag - p2.imag)


# FIXME:
# no need for this slow "radius" approach
# go along the final path, fast-forward n path items, compare dist
pt2 = 0
min_saved = 50 if G.is_sample else 100
for pos in node.path:
    exits = set()
    for dt in range(2, 21):
        for dx in range(-dt, dt + 1):
            for dy in range(-dt, dt + 1):
                p = pos + complex(dx, dy)
                if dist(pos, p) != dt:
                    continue
                if times[p] + dt + min_saved <= times[pos]:
                    exits.add(p)
    pt2 += len(exits)
print(pt2)  # sample expects 285 with min_saved=50
