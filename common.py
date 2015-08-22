import matplotlib.pyplot as plt
import networkx as nx
import igraph as ig

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
  ldegs = list(set(G.degree().values()))
  ldegs.sort()
  return len(G),tuple(ldegs),diameter(G)

def show(G):
  print(attributes(G))
  
def remove_nodes_deg(g, d):
  degs = g.degree().copy()
  ns = g.nodes().copy()
  
  for v in ns:
    if degs[v] == d:
      g.remove_node(v)
      
def draw(g):
  nx.draw(g)
  plt.show()