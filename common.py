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
  return len(G),tuple(set(G.degree().values())),diameter(G)

def show(G):
  print(attributes(G))