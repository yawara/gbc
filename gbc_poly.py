from sage.all import *
from itertools import product
import numpy as np
import networkx as nx
import igraph as ig

from common import nx_to_ig, diameter, attributes, show

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
    v = np.array([p,q,r])
    flag = True
    for k in iter_q(Q,star=True):
      if tuple(k*v) in lines:
        flag = False
        break
    if flag:
      lines.add((p,q,r))

  lines.remove((0,0,0))
  
  G = nx.Graph()
  
  for i, l1 in enumerate(lines):
    for j, l2 in enumerate(lines):
      if i < j:
        if np.array(l1).dot(np.array(l2)) == 0:
          G.add_edge(l1, l2)

  return G
