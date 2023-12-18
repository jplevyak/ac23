#!/usr/bin/python3
from collections import defaultdict

mm = list(map(lambda x: list(map(int, list(x.strip()))), open("17", "r").readlines()))
dd = [(0, 1), (1, 0), (0, -1), (-1, 0)]  
M = 1000000000
lowest = M
p = set([(0, 0, 0), (0, 1, 0), (0, 2, 0), (0, 3, 0), (0, 4, 0), (0, 5, 0), (0, 6, 0), (0, 7, 0), (0, 8, 0),
         (1, 8, 1), (2, 8, 1), (3, 8, 1), (4, 8, 1),
         (4, 9, 0), (4, 10, 0), (4, 11, 0), (4, 12, 0),
         (5, 12, 1), (6, 12, 1), (7, 12, 1), (8, 12, 1), (9, 12, 1), (10, 12, 1), (11, 12, 1), (12, 12, 1)])

def f(y, x, d, r, v, yy, xx, dd, rr, w, vv, rmax):
    global lowest
    if yy >= 0 and yy < len(mm) and xx >= 0 and xx < len(mm[0]) and rr <= rmax:
        o = vv[(yy, xx, dd, rr)]
        n = min(v + mm[yy][xx], o)
        #if (y, x, d) in p:
        #    print('X', y, x, d, r, v, yy, xx, dd, rr, o, n)
        if o != n and n < (9 * (len(mm) + len(mm[0]))) and n < lowest:
            if xx == len(mm[0]) - 1 and yy == len(mm) - 1:
                lowest = min(lowest, n)
            #if (yy, xx, dd) in p:
            #    print(yy, xx, dd, rr, y, x, v, rr, o, n)
            vv[(yy, xx, dd, rr)] = n
            w.add((yy, xx, dd, rr))

def g(rmin, rmax):
    vv = defaultdict(lambda: M)
    w = set()
    vv[(0, 0, 1, 0)] = 0
    w.add((0, 0, 1, 0))
    vv[(0, 0, 0, 0)] = 0
    w.add((0, 0, 0, 0))
    while len(w) > 0:
        (y, x, d, r) = w.pop()
        v = vv[(y, x, d, r)]
        f(y, x, d, r, v, y + dd[d][0], x + dd[d][1], d, r + 1, w, vv, rmax)
        #if y == 4 and x == 8 and d == 1:
        #    print('X', r, rmin)
        if r >= rmin:
            ddd = (d + 1) % 4
            f(y, x, d, r, v, y + dd[ddd][0], x + dd[ddd][1], ddd, 1, w, vv, rmax)
            ddd = (d + 3) % 4
            f(y, x, d, r, v, y + dd[ddd][0], x + dd[ddd][1], ddd, 1, w, vv, rmax)
    t = M
    for v in vv:
        if v[0] == len(mm) - 1 and v[1] == len(mm[0]) - 1:
            t = min(t, vv[v])
            if vv[v] == t:
                vvv = v
    return t
    while vvv[0] != 0 or vvv[1] != 0:
        #print(vvv, vv[vvv])
        if vvv[3] > 1:   
            vvv = (vvv[0] - dd[vvv[2]][0], vvv[1] - dd[vvv[2]][1], vvv[2], vvv[3] - 1)
            #print(vvv, (vvv[0] - dd[vvv[2]][0],  vvv[1] - dd[vvv[2]][1], dd[vvv[2]][0], dd[vvv[2]][1]))
        else:
            found = None
            for v in vv:
                if found is not None:
                    break
                for d in dd:
                    if v[0] + d[0] == vvv[0] and v[1] + d[1] == vvv[1] and vv[vvv] - mm[vvv[0]][vvv[1]] == vv[v]:
                        found = v
                        break
            if not found:
                print('not found', vvv)
            vvv = found

    pp = [(0, 8, 1, 8)]
    for p in pp:
        print(p, vv[p])
    return t

#print("17a", g(0, 3))
print("17b", g(4, 10))
