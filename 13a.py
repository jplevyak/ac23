#!/usr/bin/python3
from sys import *
from functools import *
from re import *

S = [*stdin.readlines()]
m ={i+1j*j:(c=='.') for i,s in enumerate(S[:-2]) for j,c in enumerate(s.rstrip()) if c in '.#'}
g = {}
n = lambda x,d:[(x,-d*1j),(x-d*1j,d),(x+d*(1-1j),d*1j)][c(x,d)]
c = lambda x,d:len({x-d*1j,x-d*1j+d}&m.keys())
f = lambda x:(y:=c(*x)==2 and n(*x) or (z:=f(n(*x))) and (z[0]+c(*x) and z[1] or f(z[1])[1])) and g.update({x:(y[0],-y[1]),y:(x[0],-x[1])}) or (c(*y),n(*y))
f(next((x,d) for x in m for d in [1,-1,1j,-1j] if x+d not in m and x+d*(1+1j) in m))
j =lambda x,d:g.get((x,d),(x+d,d))
x = reduce(lambda x,p:(x[0],x[1]*1j*(1-2*(p=='R'))) if p in 'RL' else reduce(lambda y,_:j(*y) if m[j(*y)[0]] else y,range(int(p)),x),findall('\d+|R|L',S[-1]),(min(m,key=lambda x:(x.real,x.imag)),1j))
print(1000*x[0].real+4*x[0].imag+1004+[1j,1,-1j,-1].index(x[1]))
