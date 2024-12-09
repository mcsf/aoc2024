#!/usr/bin/env python3

from sys import stdin
from dataclasses import dataclass
from copy import deepcopy
from multiprocessing import Pool, freeze_support
from functools import partial


@dataclass
class Block:
    id: int
    size: int


def realloc_1(fs):
    free_ptr = 0
    file_ptr = len(fs) - 1

    while free_ptr != file_ptr:

        for free_ptr in range(free_ptr, len(fs)):
            if fs[free_ptr].id == -1 and fs[free_ptr].size:
                break

        # Enough free space to eat the file
        if fs[free_ptr].size >= fs[file_ptr].size:
            before = Block(fs[file_ptr].id, fs[file_ptr].size)
            fs[free_ptr].size -= fs[file_ptr].size
            fs = fs[:free_ptr] + [before] + fs[free_ptr:-1]

        # Free space is replaced with file fragment
        else:
            fs[free_ptr].id = fs[file_ptr].id
            fs[file_ptr].size -= fs[free_ptr].size

    return fs


def realloc_2(fs):
    last_file = fs[len(fs) - 1].id

    for file in range(last_file, -1, -1):

        for file_ptr in range(len(fs) - 1, -1, -1):
            if fs[file_ptr].id == file:
                break

        found = False
        for free_ptr in range(file_ptr):
            if (fs[free_ptr].id == -1 and
                    fs[free_ptr].size >= fs[file_ptr].size):
                found = True
                break

        if found:
            before = Block(fs[file_ptr].id, fs[file_ptr].size)
            fs[free_ptr].size -= fs[file_ptr].size
            fs[file_ptr].id = -1
            fs = fs[:free_ptr] + [before] + fs[free_ptr:]

    return fs


def checksum(fs):
    i = 0
    s = 0
    for sector in fs:
        for _ in range(sector.size):
            if sector.id > -1:
                s += i * sector.id
            i += 1

    return s


def task(fs, alloc_fn):
    return checksum(alloc_fn(deepcopy(fs)))


if __name__ == '__main__':
    freeze_support()
    pool = Pool()

    fs = []  # type: list[Block]
    for i, c in enumerate(next(stdin).strip()):
        size = int(c)
        fs.append(Block(i // 2 if i % 2 == 0 else - 1, size))

    print(*pool.map(partial(task, fs), [realloc_1, realloc_2]), sep='\n')
