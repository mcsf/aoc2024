#!/usr/bin/env python3

from sys import stdin
from collections import defaultdict

M = {}
for y, line in enumerate(stdin):
    for x, c in enumerate(line.strip()):
        M[complex(x, y)] = c


def main() -> None:
    pt1 = 0
    pt2 = 0

    # Standard traversal algorithm with just two main modifications:
    # - `prev_visited` allows determining different regions of points
    # - `edges` collects points immediately beyond a region

    prev_visited = set()
    for start in M:
        if start in prev_visited:
            continue

        queue = [start]
        visited = set()

        # Collect outside points found immediately beyond a region. For
        # convenience for solving part 2, group those points according to the
        # direction in which they were seen (right, down, etc.).
        edges = defaultdict(set)

        while queue:
            p = queue.pop()

            if p in visited:
                continue

            visited.add(p)
            prev_visited.add(p)

            for dir in [1, 1j, -1, -1j]:
                adj = p + dir
                if M.get(adj) == M[start]:
                    queue.append(adj)
                else:
                    edges[dir].add(p)

        area = len(visited)
        perimeter = sum(map(len, edges.values()))
        sides_count = sum(map(count_clusters, edges.values()))

        pt1 += area * perimeter
        pt2 += area * sides_count

    print(pt1)
    print(pt2)


# Same as before, but simpler. Group points into contiguous regions and return
# the number of said regions.
def count_clusters(points: set[complex]) -> int:
    prev_visited = set()
    n = 0
    for start in points:
        if start in prev_visited:
            continue
        queue = [start]
        visited = set()
        while queue:
            p = queue.pop()
            if p in visited:
                continue
            visited.add(p)
            prev_visited.add(p)
            for adj in [p + 1, p + 1j, p - 1, p - 1j]:
                if adj in points:
                    queue.append(adj)
        n += 1
    return n


main()
