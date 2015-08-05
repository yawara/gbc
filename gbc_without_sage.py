from itertools import product
from collections import defaultdict
import networkx as nx
import pyprimes

from common import nx_to_ig, diameter, attributes, show


def gbc(n):
  lines = []
  check_table = defaultdict(bool)

  for p,q,r in product(range(n), repeat=3):
    if p == 0 and q == 0 and r == 0:
      pass
    else:
      flag = True
      if not check_table[(p,q,r)]:
        for k in range(1,n):
          kp, kq, kr = (k*p)%n, (k*q)%n, (k*r)%n 
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


if __name__ == "__main__":
  def show_n(n):
    G = gbc(n)
    show(G)
  
  for i in range(2,10):
    show_n(i)
