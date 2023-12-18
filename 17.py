#!/usr/bin/python3
from collections import defaultdict

mm = list(map(lambda x: list(map(int, list(x.strip()))), open("17", "r").readlines()))
dd = [(0, 1), (1, 0), (0, -1), (-1, 0)]  
M = 1000000000
lowest = M

def f(y, x, v, yy, xx, dd, rr, w, vv, rmax):
    global lowest
    if yy >= 0 and yy < len(mm) and xx >= 0 and xx < len(mm[0]) and rr <= rmax:
        o = vv[(yy, xx, dd, rr)]
        n = min(v + mm[yy][xx], o)
        if o != n and n < (9 * (len(mm) + len(mm[0]))) and n < lowest:
            if xx == len(mm[0]) - 1 and yy == len(mm) - 1:
                lowest = min(lowest, n)
            vv[(yy, xx, dd, rr)] = n
            w.add((yy, xx, dd, rr))

def g(rmin, rmax):
    global lowest
    lowest = M
    vv = defaultdict(lambda: M)
    w = set()
    vv[(0, 0, 1, 0)] = 0
    w.add((0, 0, 1, 0))
    vv[(0, 0, 0, 0)] = 0
    w.add((0, 0, 0, 0))
    while len(w) > 0:
        (y, x, d, r) = w.pop()
        v = vv[(y, x, d, r)]
        f(y, x, v, y + dd[d][0], x + dd[d][1], d, r + 1, w, vv, rmax)
        if r >= rmin:
            ddd = (d + 1) % 4
            f(y, x, v, y + dd[ddd][0], x + dd[ddd][1], ddd, 1, w, vv, rmax)
            ddd = (d + 3) % 4
            f(y, x, v, y + dd[ddd][0], x + dd[ddd][1], ddd, 1, w, vv, rmax)
    t = M
    for v in vv:
        if v[0] == len(mm) - 1 and v[1] == len(mm[0]) - 1:
            t = min(t, vv[v])
            if vv[v] == t:
                vvv = v
    return t

print("17a", g(0, 3))
print("17b", g(4, 10))
