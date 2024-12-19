#!/usr/bin/env python3

from sys import stdin
from math import inf
from heapq import heappop, heappush
from dataclasses import dataclass


@dataclass
class Node:
    score: int
    pos: complex
    rot: complex
    path: set[complex]

    def __lt__(self, other):
        return self.score < other.score

    def adjacent(self):
        for ds, dp, dr in [(1, self.rot, 1), (1000, 0, 1j), (1000, 0, -1j)]:
            yield Node(self.score + ds,
                       self.pos + dp,
                       self.rot * dr,
                       self.path | {self.pos + dp})


G = set()  # type: set[complex]
for y, line in enumerate(stdin):
    for x, c in enumerate(line.strip()):
        p = complex(x, y)
        if c == 'S':
            start = p
        elif c == 'E':
            end = p
        if c != '#':
            G.add(p)

Q = [Node(0, start, 1+0j, {start})]  # graph search queue
C = {(start, 1+0j): 0}               # best score at given (pos, rot)

best_score = inf
best_tiles = set()

while Q:
    node = heappop(Q)

    if node.score > C.get((node.pos, node.rot), inf):
        continue

    C[node.pos, node.rot] = node.score

    if node.pos == end:
        if node.score > best_score:
            break
        best_score = node.score
        best_tiles |= node.path

    for adj in node.adjacent():
        if adj.pos in G and adj.score < C.get((adj.pos, adj.rot), inf):
            heappush(Q, adj)


print(best_score)
print(len(best_tiles))
