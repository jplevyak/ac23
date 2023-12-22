#!/usr/bin/python3
import math
from copy import deepcopy


nn = {} # (op, connections, input#)
ss = {} # (inputs (, flipflop state)?)
ww = [] # (target, input#, value)

nn['output'] = (None, [], [])

for l in map(lambda x: x.strip(), open("20", "r").readlines()):
    n, d = l.split(">")
    n = n[:-2]
    dd = list(map(lambda x: x.strip(), d[1:].split(",")))
    if n == 'broadcaster':
        nn[n] = (None, dd, [])
    else:
        nn[n[1:]] = (n[0], dd, [])

for n in nn:
    ss[n] = [[]]
    if nn[n][0] == '%':
        ss[n].append(False)

missing = []
for (n,v) in nn.items():
    for d in v[1]:
        if not d in ss:
            missing.append(d)
for d in missing:
    nn[d] = (None, [], [])
    ss[d] = [[]]

for (n,v) in nn.items():
    for d in v[1]:
        v[2].append(len(ss[d][0]))
        ss[d][0].append(False)

iw = 0
done = {}
l = 0
h = 0
c = 0
ww.append(('broadcaster', 0, False, 'button'))
l += 1
fact = [0, 0, 0, 0]
while (iw < len(ww)):
    w = ww[iw]
    a = nn[w[0]]
    sa = ss[w[0]]
    #print('w', w, a, sa)
    if a[0] == None:
        for i, b in enumerate(a[1]):
            #print(None, b, i, (b, a[2][i], False))
            ww.append((b, a[2][i], False, w[0]))
            l += 1
    elif a[0] == '%':
        if not w[2]:
            #print('%1', sa[-1], not sa[-1])
            sa[-1] = not sa[-1]
            if sa[-1]:
                h += len(a[1])
            else:
                l += len(a[1])
            for i, b in enumerate(a[1]):
                #print('%', b, i, (b, a[2][i], sa[-1]))
                ww.append((b, a[2][i], sa[-1], w[0]))
    else: # &
        v = True
        sa[0][w[1]] = w[2]
        if w[0] == 'xn' and w[2]:
            print(w, c)
            fact[w[1]] = c + 1
            if math.prod(fact) > 0:
                break
        for s in sa[0]:
            #print('&1', v, s)
            v = v and s
        v = not v
        for i, b in enumerate(a[1]):
            #print('&', b, i, (b, a[2][i],  v))
            ww.append((b, a[2][i], v, w[0]))
            if v:
                h += 1
            else:
                l += 1

    iw += 1
    if iw >= len(ww):
        state = bytearray()
        for k, v in nn.items():
            if v[0] == '&':
                for x in ss[k][0]:
                    state.append(0 if x else 1)
            if v[0] == '%':
                state.append(0 if ss[k][-1] else 1)
        #print(state)
        state = state.decode("utf-8")
        #if c == 999:
        #    c = 1000
        #    break
        #if state in done:
        #    print(done)
        #    print(done[state])
        #    l -= done[state][0]
        #    h -= done[state][1]
        #    c = c - done[state][2]
        #    break
        done[state] = (l, h, c)
        ww.append(('broadcaster', 0, False, 'button'))
        l += 1
        c += 1

#for w in ww:
#    print(w[3], '-low->' if not w[2] else '-high->', w[0])
print(c, l, h)
print(math.lcm(*fact))
print("20a", l, h, c, 1000 // c, l * (1000 // c), h * (1000 // c), (l * (1000 // c)) * (h * (1000 // c)))
