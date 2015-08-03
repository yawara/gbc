from sage.all import *
from itertools import product
import networkx as nx

from common import nx_to_ig, diameter, attributes, show

def gbc(R):
  lines = []
  lines.append((0,0,0))
  
  for p,q,r in product(R, repeat=3):
    flag = True
    for k in R:
      if k == 0:
        pass
      else:
        if (k*p,k*q,k*r) in lines:
          flag = False
          break
    if flag:
      lines.append((p,q,r))

  lines.remove((0,0,0))
  
  G = nx.Graph()
  G.add_nodes_from(lines)
  
  for i, l1 in enumerate(lines):
    for j, l2 in enumerate(lines):
      if i < j:
        if l1[0]*l2[0]+l1[1]*l2[1]+l1[2]*l2[2] == 0:
          G.add_edge(l1, l2)

  return G
