#!/usr/bin/env sage

from sage.all import *
from sage_poly import *

def search(n):
  R = Zmod(n)
  x = var('x')
  P = PolynomialRing(R, x)
  p = x**2+1
  if is_prime(n):
    pass
  else:
    Q = P.quotient(p)
    G = get(Q)
    print(Q)
    show(G)
    print("")

if __name__ == "__main__":
  for n in range(2,100):
    search(n)
