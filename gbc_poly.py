from sage.all import *
from itertools import product
from collections import defaultdict
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
  lines = []
  check_table = defaultdict(bool)
  
  for p,q,r in product(iter_q(Q), repeat=3):
    if p == 0 and q == 0 and r == 0:
      pass
    else:
      flag = True
      if not check_table[(p,q,r)]:
        for k in iter_q(Q, star=True):
          kp, kq, kr = k*p, k*q, k*r 
          if kp == 0 and kq == 0 and kr == 0:
            flag = False
          else:
            check_table[(kp,kq,kr)] = True
        if flag:
          lines.append((p,q,r))  
  
  G = nx.Graph()
  G.add_nodes_from(lines)
  
  for i, l1 in enumerate(lines):
    for j, l2 in enumerate(lines):
      if i < j:
        if l1[0]*l2[0]+l1[1]*l2[1]+l1[2]*l2[2] == 0:
          G.add_edge(l1, l2)

  return G

if __name__ == '__main__':
  R = GF(3)
  P = PolynomialRing(R, 'x')
  f = x**2+2
  Q = P.quotient(f)
  G = gbc_poly(Q)
  show(G)