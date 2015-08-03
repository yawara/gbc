from itertools import product
import networkx as nx
import igraph as ig
import pyprimes

from common import nx_to_ig, diameter, attributes, show


def gbc(n):
  lines = []
  lines.append((0,0,0))
  
  for p,q,r in product(range(n), repeat=3):
    flag = True
    for k in range(n):
      if k == 0:
        pass
      else:
        if ((k*p)%n,(k*q)%n,(k*r)%n) in lines:
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
        if (l1[0]*l2[0]+l1[1]*l2[1]+l1[2]*l2[2])%n == 0:
          G.add_edge(l1, l2)

  return G

def gbc_with_loop(n):
  lines = []
  lines.append((0,0,0))
  
  for p,q,r in product(range(n), repeat=3):
    flag = True
    for k in range(n):
      if k == 0:
        pass
      else:
        if ((k*p)%n,(k*q)%n,(k*r)%n) in lines:
          flag = False
          break
    if flag:
      lines.append((p,q,r))

  lines.remove((0,0,0))
  
  G = nx.Graph()
  G.add_nodes_from(lines)
  
  for i, l1 in enumerate(lines):
    for j, l2 in enumerate(lines):
      if i <= j:
        if (l1[0]*l2[0]+l1[1]*l2[1]+l1[2]*l2[2])%n == 0:
          G.add_edge(l1, l2)

  return G


def order(n):
  rtv = n**2
  for (p,_) in pyprimes.factorise(n):
    rtv *= 1 + 1/p + 1/p**2
  return round(rtv)

def degree(n):
  rtv = n
  for (p,_) in pyprimes.factorise(n):
    rtv *=  1 + 1/p 
  return round(rtv)

def pair(n):
  return order(n),degree(n)
