from sage.all import *
from itertools import product
import networkx as nx

from common import nx_to_ig, diameter, attributes, show

n = 3
R = Zmod(n)
P = PolynomialRing(R,'x')
x = P.gen()
f = x**2 + 1
Q = P.quotient(f)

def iter_q(Q,star=False):
  if not star:
    yield 0
  a = Q.gen()
  mod = Q.modulus()
  d = mod.degree()
  P = Q.base()
  for i in range(1,d+1):
    for p in P.polynomials(d-i):
      yield p.subs(a)

      
def gbc_poly(Q):
  lines = set()
  lines.add((0,0,0))
  
  for p,q,r in product(iter_q(Q), repeat=3):
    flag = True
    for k in iter_q(Q,star=True):
      if (k*p, k*q, k*r) in lines:
        flag = False
        break
    if flag:
      lines.add((p,q,r))

  lines.remove((0,0,0))
  
  G = nx.Graph()
  
  for i, l1 in enumerate(lines):
    for j, l2 in enumerate(lines):
      if i < j:
        if l1[0]*l2[0]+l1[1]*l2[1]+l1[2]*l2[2] == 0:
          G.add_edge(l1, l2)

  return G
