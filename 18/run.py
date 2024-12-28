#!/usr/bin/env python3

from heapq import heappush, heappop

positions = [complex(x, y) for x, y in (list(map(int, line.split(',')))
                                        for line in open(0))]
dim, byte = 71, 1024
if positions[0] == 5+4j:
    dim, byte = 7, 12  # Sample input


def search(byte):
    corrupt = {*positions[:byte]}
    start = 0j
    end = complex(dim - 1, dim - 1)
    queue = [(0, str(start))]  # serialize complex nums for heapq
    visited = set()

    while queue:
        cost, p_str = heappop(queue)
        p = complex(p_str)

        if p == end:
            return cost

        if p in visited:
            continue

        visited.add(p)

        for adj in (p + 1, p - 1, p + 1j, p - 1j):
            if 0 <= adj.real < dim and 0 <= adj.imag < dim \
                    and adj not in corrupt:
                heappush(queue, (cost + 1, str(adj)))


def bisect():
    good = byte
    bad = len(positions)
    target = good + (bad - good) // 2

    while target not in (good, bad):
        if search(target) is not None:
            good = target
        else:
            bad = target
        target = good + (bad - good) // 2

    p = positions[target]
    return f'{int(p.real)},{int(p.imag)}'


print(search(byte))
print(bisect())
