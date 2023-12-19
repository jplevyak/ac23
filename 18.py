#!/usr/bin/python3
from collections import defaultdict

mm = list(map(lambda x: x.strip().split(' '), open("18", "r").readlines()))
dd = {'R': (0, 1), 'D': (1, 0), 'L': (0, -1), 'U': (-1, 0)}  

def f(mm):
    p = []
    x = 0
    y = 0
    for m in mm:
        (d, l) = m
        if d == 'D':
            p.append((y, x, 'D'))
            p.append((y + l, x, 'U'))
        elif d == 'U': 
            p.append((y, x, 'U'))
            p.append((y - l, x, 'D'))
        y = y + (dd[d][0] * l)
        x = x + (dd[d][1] * l)
    p.sort(key=(lambda x: (1000 if x[2] == 'U' else 0) + x[0] * 1000000 + x[1]))

    l = []
    q = 0
    t = 0
    while q < len(p):
        ny = p[q][0]
        i = 0
        while i < len(l):
            if ny > y + 1 and l[i+1] > l[i]:
                t += ((l[i+1] - l[i])+ 1) * (ny - y - 1)
            i += 2
        y = ny
        a = l.copy()
        while q < len(p) and p[q][0] == ny:
            if p[q][2] == 'D':
                l.append(p[q][1])
            else:
                l.remove(p[q][1])
            q += 1
        l.sort()
        b = l.copy()
        i = j = 0
        tt = t
        while (i < len(a) or j < len(b)):
            if i < len(a) and j < len(b):
                if a[i] > b[j+1]:
                    t += ((b[j+1] - b[j]) + 1)
                    j += 2
                elif b[j] > a[i+1]:
                    t += ((a[i+1] - a[i]) + 1)
                    i += 2
                elif a[i+1] > b[j+1]:
                    a[i] = min(a[i], b[j])
                    j += 2
                else:
                    b[j] = min(a[i], b[j])
                    i += 2
            elif i < len(a):
                t += ((a[i+1] - a[i]) + 1)
                i += 2
            else:
                t += ((b[j+1] - b[j]) + 1)
                j += 2
    return t

print("18a", f(list([(m[0], int(m[1])) for m in mm])))
DD = { 0: 'R', 1: 'D', 2: 'L', 3: 'U' }
print("18b", f(list([(DD[int(m[2][7])], int(m[2][2:7], 16)) for m in mm])))
