#!/usr/bin/env sage

from sage.all import *
from sage_poly import *

def search(n,m):
  R = Zmod(n)
  print(R)
  print("")
  
  x = var('x')
  P = PolynomialRing(R, x)

  for p in P.polynomials(m):
    if R.is_field() and p in P.irreducible_element(m):
      pass
    else:
      if p in P.monics(m):
        print(p)
        Q = P.quotient(p)
        G = get(Q)
        show(G)
        print("")

if __name__ == "__main__":
  import sys
  n = int(sys.argv[1])
  m = int(sys.argv[2])
  search(n,m)
