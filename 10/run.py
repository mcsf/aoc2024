#!/usr/bin/env python3

from sys import stdin

M = {}  # Map
L = []  # Low points
H = []  # High points
for y, line in enumerate(stdin):
    for x, c in enumerate(line.strip()):
        p = complex(x, y)
        M[p] = int(c) if c != '.' else -1
        if c == '0':
            L.append(p)
        elif c == '9':
            H.append(p)


def walk(start: complex) -> tuple[int, int]:
    queue = [(start, [])]  # type: list[tuple[complex, list[complex]]]

    tops_seen = set()
    paths = []

    while queue:
        p, path = queue.pop()

        if p in H:
            tops_seen.add(p)
            paths.append(path)
            continue

        for next_p in [p + 1, p + 1j, p + -1, p - 1j]:
            if M.get(next_p, -1) == M[p] + 1:
                queue.append((next_p,  path + [next_p]))

    return len(tops_seen), len(paths)


score = rating = 0
for start in L:
    tops_seen, paths = walk(start)
    score += tops_seen
    rating += paths

print(score)
print(rating)
