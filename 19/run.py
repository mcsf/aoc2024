#!/usr/bin/env python3

from sys import stdin
from re import match
from functools import lru_cache

towel_patterns = next(stdin).strip().split(', ')
next(stdin)
towel_designs = [line.strip() for line in stdin]


# Part 1 (kept due to better performance)
pattern = '|'.join(towel_patterns)
pattern = f'^({pattern})+$'
print(sum(1 for design in towel_designs if match(pattern, design)))


# Part 2
@lru_cache
def parse(word):
    return 1 if not word else sum(parse(word[len(p):])
                                  for p in towel_patterns
                                  if word.startswith(p))


print(sum(parse(d) for d in towel_designs))
