#!/usr/bin/python3
import math
from copy import deepcopy

r = {}

ll = list(map(lambda x: x.strip(), open("19", "r").readlines()))
ill = 0
I = {'x': '0', 'm': '1', 'a': '2', 's': '3'}
a = []

def _A():
    a.append(x)

def _R():
    pass

while len(ll[ill]) > 0:
    (name, v) = ll[ill].split("{")
    vv = v[:-1].split(",")
    d = "def _" + name + "():\n"
    for i, v in enumerate(vv):
        o = "<" if "<" in v else (">" if ">" in v else None)
        if o is not None:
            (n, b) = v.split(o)
            c, f = b.split(":")
            d += " " + ("if" if i == 0 else ("elif" if i != len(vv) - 1 else "else"))
            d += " x[" + I[n] + "] " + o + " " + c + ":\n"
        else:
            d += " else:\n"
            f = v
        d += "  _" + f + "()\n"
    #print(d)
    exec(d)
    ill += 1

ill += 1
while ill < len(ll):
    vv = ll[ill][1:-1].split(",")
    x = [int(v.split("=")[1]) for v in vv]
    exec("_in()")
    ill += 1

print("19a", sum(map(sum, a)))

F = {}
ill = 0
while len(ll[ill]) > 0:
    (name, v) = ll[ill].split("{")
    vv = v[:-1].split(",")
    F[name] = []
    for i, v in enumerate(vv):
        o = "<" if "<" in v else (">" if ">" in v else None)
        if o is not None:
            (n, b) = v.split(o)
            c, f = b.split(":")
            #if f == 'A':
            #    print(v, b, f)
            F[name].append((f, int(I[n]), int(c) if o == ">" else None, int(c) if o == "<" else None))
        else:
            F[name].append((v, None, None, None))
    ill += 1

M = 4001
S = [[0,  M], [0,  M], [0,  M], [0,  M]]

def g(x, n):
    #print(n, x)
    if n == "A":
        #print(x, math.prod([x[i][1] - x[i][0] - 1 for i in range(4)]))
        return math.prod([x[i][1] - x[i][0] - 1 for i in range(4)])
    if n == "R":
        return 0
    f = F[n]
    t = 0
    for (n, v, l, h) in f:
        #print(n, v, l, h)
        if v == None:
            t += g(deepcopy(x), n)
        elif l != None:
            y = deepcopy(x)
            y[v][0] = max(y[v][0], l)
            t += g(y, n)
            x[v][1] = min(x[v][1], l + 1)
        else:
            y = deepcopy(x)
            y[v][1] = min(y[v][1], h)
            t += g(y, n)
            x[v][0] = max(x[v][0], h - 1)
    return t

print("19a", g(S, "in"))
