from sage.all import *
import networkx as nx
from gbc_poly import gbc_poly


def gbc_gauss(n):
    R = Zmod(n)
    x = var('x')
    P = PolynomialRing(R, x)
    f = x**2 + 1
    Q = P.quotient(f)
    G = gbc_poly(Q)

    return G


def show(G):
    ldegs = list(set(G.degree().values()))
    ldegs.sort()
    print len(G), tuple(ldegs), nx.diameter(G)

if __name__ == '__main__':
    for n in range(2, 10):
        show(gbc_gauss(n))
