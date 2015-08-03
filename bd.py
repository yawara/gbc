import networkx as nx
from networkx.algorithms import bipartite
from gbc_without_sage import gbc_with_loop as gbc

G = gbc(2)

def check_dup(G):
  for i, v in enumerate(G):
    for j, w in enumerate(G):
      if i < j:
        if set(G.neighbors(v)) == set(G.neighbors(w)):
          raise Exception("Found duplicated nodes")

def check_neighbors(G):
  check_dup(G)
  rtv = set()
  for i, v in enumerate(G):
    for j, w in enumerate(G):
      if i < j:
        l = len(set(G.neighbors(v)).intersection(G.neighbors(w)))
        print(l)
        rtv.add(l)
  print(rtv)
  
def to_hg(G):
  check_dup(G)
  
  H = nx.Graph()
  
  for v in G:
    H.add_node(v, bipartite=0)
    h_edge = tuple(G.neighbors(v))
    H.add_node(h_edge , bipartite=1)
    
    for w in h_edge:
      H.add_edge(w, h_edge)
  
  return H

def bd(n):
  G = gbc(n)
  H = to_hg(G)
  
  return H

H = to_hg(G)

def params_bd(H):
  V, B = bipartite.sets(H)
  
  k = H.degree(list(B)[0])
  r = H.degree(list(V)[0])
  l = len(set(H.neighbors(list(V)[0])).intersection(set(H.neighbors(list(V)[1]))))
  
  dl =  len(set(H.neighbors(list(B)[0])).intersection(set(H.neighbors(list(B)[1]))))
  
  for b in B:
    if k != H.degree(b):
      raise Exception("Failed: REGULARITY")
  for v in V:
    if r != H.degree(v):
      raise Exception("Failed: 1-BALANCE")
  rtv = set([l])
  cnt = 0
  for i, v1 in enumerate(V):
    for j, v2 in enumerate(V):
      if i < j:
        common_neighbors = set(H.neighbors(v1)).intersection(set(H.neighbors(v2)))
        la = len(common_neighbors)
        print(v1,v2)
        print(common_neighbors)
        print(la)
        if l != la:
          print("Failed: 2-BALANCE")
          cnt += 1
          rtv.add(la)
        print("")
  print(rtv)
  print(cnt)
  
  for i, b1 in enumerate(B):
    for j, b2 in enumerate(B):
      if i < j:
        inter_block = set(H.neighbors(b1)).intersection(set(H.neighbors(b2)))
        dla = len(inter_block)
        if dl != dla:
          raise Exception("Failed: DUAL 2-BALANCE")
  
  return k, r, l, dl
