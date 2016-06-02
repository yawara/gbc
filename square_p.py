import networkx as nx

from gbc import *

p = 5

a = matrix(Zmod(p), [[0, 1], [0, 0]])
b = matrix.identity(2)

a.set_immutable()
b.set_immutable()

R = [i * a + j * b for i in range(p) for j in range(p)]

for m in R:
    m.set_immutable()

G = gbc(R)
