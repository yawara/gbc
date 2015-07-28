from sage.all import *
from itertools import product
import numpy as np
import networkx as nx
import igraph as ig

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
        if np.array(l1).dot(np.array(l2)) == 0:
          G.add_edge(l1, l2)

  return G
