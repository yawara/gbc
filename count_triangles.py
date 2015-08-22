from gbc_without_sage import gbc, show
import matplotlib.pyplot as plt
import numpy as np
import networkx as nx

def count_triangles(n):
  g = gbc(n)
  m = nx.to_numpy_matrix(g)
  m3 = m.dot(m).dot(m)
  return np.diag(m3)//2

def show_diag(n):
  diag = count_triangles(n)
  print(diag)
  
def common_neighbor(g):
  flag = True
  for i, v in enumerate(g):
    for j, w in enumerate(g):
      if i < j:  
        vn = set(g.neighbors(v))
        if w in vn:
          wn = set(g.neighbors(w))
          print(v, w)
          int_vn_wn = vn.intersection(wn)
          if len(int_vn_wn) > 1:
            flag = False
          print(int_vn_wn)
          print()
  if not flag:
    print("For some vertices v and w, they are adjacent and included by more than two triangles")