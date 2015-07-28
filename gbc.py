from sage import *
from itertools import product
import numpy as np
import networkx as nx
import igraph as ig

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

def gbc_from_quaternion(K):

def gbc_mat(M):
  lines = []
  lines.append((0,0,0))
  
  for p,q,r in product(M, repeat=3):
    
    flag = True
    for k in M:
      if k == 0:
        pass
      else:
        if (k*p,k*q,k*r) in lines:
          flag = False
          break
    if flag:
      p.set_immutable()
      q.set_immutable()
      r.set_immutable()
      lines.append((p,q,r))

  lines.remove((0,0,0))
  
  G = nx.DiGraph()
  G.add_nodes_from(lines)
  
  for i, l1 in enumerate(lines):
    for j, l2 in enumerate(lines):
      if i != j:
        if np.array(l1).dot(np.array(l2)) == 0:
          G.add_edge(l1, l2)

  return G


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


def nx_to_ig(G):
  int_G = nx.convert_node_labels_to_integers(G)
  ig_G = ig.Graph()
  
  ig_G.add_vertices(int_G)
  ig_G.add_edges(int_G.edges())
  
  return ig_G

def diameter(G):
  ig_G = nx_to_ig(G)
  return ig_G.diameter()

def attributes(G):
  ig_G = nx_to_ig(G)
  return len(G),tuple(set(G.degree().values())),diameter(G)


def show(G):
  print(attributes(G))