from sage.all import *
from itertools import product
from collections import defaultdict
import networkx as nx

from common import nx_to_ig, diameter, attributes, show

def BooleanRing(n, p=2):
  P = PolynomialRing(GF(p),n,'x')
  ps = []
  for i, g in enumerate(P.gens()):
    ps.append(g**2+g)
    for j, h in enumerate(P.gens()):
      if i < j:
        ps.append(g*h)
  B = P.quotient(ps)
  return B

def iter_b(B, star=False):
  gens = B.gens()
  
  n = len(gens) + 1
  basis = [1] + list(gens)
  
  for x in product(B.base_ring(),repeat=n):
    tmp = 0
    for i in range(n):
      tmp += x[i]*basis[i]
    if tmp == 0:
      if not star:
        yield 0
    else:
      yield tmp

def gbc_boolean(B):
  lines = []
  check_table = defaultdict(bool)
  
  for p,q,r in product(iter_b(B), repeat=3):
    if p == 0 and q == 0 and r == 0:
      pass
    else:
      flag = True
      if not check_table[(p,q,r)]:
        for k in iter_b(B, star=True):
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
