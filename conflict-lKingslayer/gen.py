#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import random
import string

n = int(sys.argv[1])
m = int(sys.argv[2])
print(n, m)


def gen_info():
    a = random.choice(('必修', '限选', '任选'))
    b = random.randint(10000000, 89999999)
    c = ''.join(random.choices(string.ascii_uppercase +\
        string.digits, k = 6))
    d = random.randint(0,100)
    e = []
    e1 = random.randint(1,3)
    for _ in range(e1):
        day = random.randint(1, 7)
        hour = random.randint(1, 6)
        li = random.randint(1, 15)
        ri = random.randint(li+1, 16)
        week = random.choice(('全周','前八周','后八周',
            f'{li}-{ri}'))
        e.append(f'{day}-{hour}({week})')
    e = ','.join(e)
    f = ''.join(random.choices(string.ascii_uppercase +\
        string.digits, k = 3))
    g = random.randint(0,5)
    h = random.choice(('是', '否'))
    i = random.randint(1, 300)
    j = random.randint(1, 300)
    k = random.choice(('空', '非空'))
    l = random.choice(('空', '非空'))
    o = random.choice(('某院系', '非某院系'))
    p = random.choice(('是', '否'))
    return a, b, c, d, e, f, g, h, i, j, k, l, o, p

for _ in range(n):
    a, b, c, d, e, f, g, h, i, j, k, l, o, p = gen_info()
    print('{} {} {} {} {} {} {} {}'.format(a, b, c, d,
        e, f, g, h))

for _ in range(m):
    a, b, c, d, e, f, g, h, i, j, k, l, o, p = gen_info()
    print('{} {} {} {} {} {} {} {} {} {} {}'.format(b, d, c,
        i, j, e, f, k, l, o, p))

