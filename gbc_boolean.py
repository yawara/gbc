from sage.all import *
from itertools import product
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
  
  n = len(gens)
  
  for x in product(B.base_ring(),repeat=n):
    tmp = 0
    for i in range(n):
      tmp += x[i]*gens[i]
    if tmp == 0:
      if not star:
        yield 0
    else:
      yield tmp

def gbc_boolean(B):
  lines = []
  lines.append((0,0,0))
  
  for p,q,r in product(iter_b(B), repeat=3):
    flag = True
    for k in iter_b(B,star=True):
      if (k*p, k*q, k*r) in lines:
        flag = False
        break
    if flag:
      lines.append((p,q,r))

  lines.remove((0,0,0))
  
  G = nx.Graph()
  
  for i, l1 in enumerate(lines):
    for j, l2 in enumerate(lines):
      if i <= j:
        if l1[0]*l2[0]+l1[1]*l2[1]+l1[2]*l2[2] == 0:
          G.add_edge(l1, l2)

  return G
