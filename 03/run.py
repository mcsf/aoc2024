#!/usr/bin/env python3

import fileinput
import re

RE = r'(mul\((\d{1,3}),(\d{1,3})\))|(do\(\))|(don\'t\(\))'

sum1 = sum2 = 0
on = True

for line in fileinput.input():
    for match in re.findall(RE, line.strip()):
        _, a, b, do, dont = match
        if do or dont:
            on = do
            continue
        sum1 += int(a) * int(b)
        if on:
            sum2 += int(a) * int(b)

print(sum1)
print(sum2)
