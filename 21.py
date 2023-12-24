#!/usr/bin/python3
import math
from copy import deepcopy

mm = list(map(lambda x: x.strip(), open("21", "r").readlines()))
X = len(mm[0])
Y = len(mm)
zz = [[False for _ in range(X)] for _ in range(Y)]
ss = deepcopy(zz)
pp = deepcopy(ss)

for y in range(Y):
    for x in range(X):
        if mm[y][x] == 'S':
            ss[y][x] = True

D = [(-1, 0), (0, 1), (1, 0), (0, -1)]
N = 64 + 1
for i in range(N):
    for y in range(Y):
        for x in range(X):
            if pp[y][x]:
                for d in D:
                    yy = y + d[0]
                    xx = x + d[1]
                    if yy >= 0 and yy < Y and xx >= 0 and xx < X and mm[yy][xx] != '#':
                        ss[yy][xx] = True
    pp = deepcopy(ss)
    ss = deepcopy(zz)

t = 0
for y in range(Y):
    for x in range(X):
        if pp[y][x]:
            t += 1
print("21a", t)
