#!/usr/bin/env python3

from sys import stdin
from re import findall


def main():
    ns = list(map(int, findall(r'\d+', stdin.read())))
    reg, prog = ns[:3], ns[3:]

    reg_copy = reg.copy()
    print(*run(reg_copy, prog), sep=',')

    print(find(prog))


def run(reg, prog):
    #       0    1    2    3    4    5    6    7
    OPS = [adv, bxl, bst, jnz, bxc, out, bdv, cdv]

    ip = 0   # Instruction pointer
    ob = []  # Output buffer

    while 0 <= ip < len(prog) - 1:
        ins = OPS[prog[ip]]
        opd = prog[ip + 1]
        res = ins(reg, opd, ob)
        if res is None:
            ip += 2
        else:
            ip = res

    return ob


def combo(opd, reg):
    assert opd < 7
    if opd <= 3:
        return opd
    return reg[opd - 4]


def adv(reg, opd, ob):
    reg[0] >>= combo(opd, reg)


def bxl(reg, opd, ob):
    reg[1] ^= opd


def bst(reg, opd, ob):
    reg[1] = combo(opd, reg) % 8


def jnz(reg, opd, ob):
    if reg[0] != 0:
        return opd


def bxc(reg, opd, ob):
    reg[1] ^= reg[2]


def out(reg, opd, ob):
    ob.append(combo(opd, reg) % 8)


def bdv(reg, opd, ob):
    reg[1] = reg[0] >> combo(opd, reg)


def cdv(reg, opd, ob):
    reg[2] = reg[0] >> combo(opd, reg)


def explain(prog):

    def aux_combo(opd):
        if opd <= 3:
            return opd
        return chr(ord('A') + opd - 4)

    table = []
    for ip in range(0, len(prog), 2):
        ins, opd = prog[ip], prog[ip + 1]
        if ins == 0:
            table.append(('adv', f'A >>= {aux_combo(opd)}'))
        elif ins == 1:
            table.append(('bxl', f'B ^= {opd}'))
        elif ins == 2:
            table.append(('bst', f'B = {aux_combo(opd)} % 8'))
        elif ins == 3:
            table.append(('jnz', 'A != 0    ', 'JMP'))
        elif ins == 4:
            table.append(('bxc', 'B ^= C'))
        elif ins == 5:
            table.append(('out', f'-> {aux_combo(opd)} % 8   ', 'OUT'))
        elif ins == 6:
            table.append(('bdv', f'B = A >> {aux_combo(opd)}'))
        elif ins == 7:
            table.append(('cdv', f'C = A >> {aux_combo(opd)}'))

    for row in table:
        print(*row, sep='\t')


# bst	B = A % 8
# bxl	B ^= 2
# cdv	C = A >> B
# bxc	B ^= C
# adv	A >>= 3
# bxl	B ^= 7
# out	-> B % 8   	OUT
# jnz	A != 0    	JMP
def find(prog, prev=0):
    if not prog:
        return prev
    for seed in range(8):
        a = prev << 3
        a += seed
        b = a % 8
        b ^= 2
        c = a >> b
        b ^= c
        b ^= 7
        if b % 8 == prog[-1]:
            rest = find(prog[:-1], a)
            if rest is None:
                continue
            return rest


main()
