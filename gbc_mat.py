from sage import *
from itertools import product
import numpy as np
import networkx as nx
import igraph as ig

from common import nx_to_ig, diameter, attributes, show

def gbc_mat(M):
  lines = []
  lines.append(((0,0,0),(0,0,0)))
  
  V = product(M, repeat=3)
  
  for (p,q,r), (s,t,u) in product(V, repeat=2):
    
    flag = True
    for k1, k2 in product(M, repeat=2):
      if k1 == 0 and k2 == 0:
        pass
      else:
        if ((k1*p,k1*q,k1*r),(s*k2,t*k2,u*k2)) in lines:
          flag = False
          break
    if flag:
      for x in [p,q,r,s,t,u]:
        x.set_immutable()
      lines.append(((p,q,r),(s,t,u)))

  lines.remove(((0,0,0),(0,0,0)))
  
  G = nx.DiGraph()
  G.add_nodes_from(lines)
  
  for i, (v1,v2) in enumerate(lines):
    for j, (w1,w2) in enumerate(lines):
      if i != j:
        if np.array(v1).dot(np.array(w2)) + np.array(w1).dot(np.array(v2)) == 0:
          G.add_edge((v1,v2),(w1,w2))

  return G

