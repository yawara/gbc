from itertools import product
from collections import defaultdict
import networkx as nx
import pyprimes

from common import nx_to_ig, diameter, attributes, show, remove_nodes_deg, draw


def coprime(k, n):
    return set(pyprimes.factors(k)).intersection(set(pyprimes.factors(n))) == set()


def lines(n):
    lines = []
    check_table = defaultdict(bool)

    for p, q, r in product(range(n), repeat=3):
        if p == 0 and q == 0 and r == 0:
            pass
        else:
            if not check_table[(p, q, r)]:
                for k in range(1, n):
                    if coprime(k, n):
                        kp, kq, kr = (k * p) % n, (k * q) % n, (k * r) % n
                        check_table[(kp, kq, kr)] = True
                lines.append((p, q, r))

    return lines


def nondegenerate_lines(n):
    lines = []
    check_table = defaultdict(bool)

    for p, q, r in product(range(n), repeat=3):
        if p == 0 and q == 0 and r == 0:
            pass
        else:
            if not check_table[(p, q, r)]:
                for k in range(1, n):
                    if coprime(k, n):
                        kp, kq, kr = (k * p) % n, (k * q) % n, (k * r) % n
                        check_table[(kp, kq, kr)] = True
                if (p**2 + q**2 + r**2) % n != 0:
                    lines.append((p, q, r))

    return lines


def nodes(n):
    rtv = []
    check_table = defaultdict(bool)

    for p, q, r in product(range(n), repeat=3):
        if p == 0 and q == 0 and r == 0:
            pass
        else:
            flag = True
            if not check_table[(p, q, r)]:
                for k in range(1, n):
                    kp, kq, kr = (k * p) % n, (k * q) % n, (k * r) % n
                    if kp == 0 and kq == 0 and kr == 0:
                        flag = False
                    else:
                        check_table[(kp, kq, kr)] = True
                if flag:
                    rtv.append((p, q, r))

    return rtv


def nondegenerate_nodes(n):
    rtv = []
    check_table = defaultdict(bool)

    for p, q, r in product(range(n), repeat=3):
        if p == 0 and q == 0 and r == 0:
            pass
        else:
            flag = True
            if not check_table[(p, q, r)]:
                for k in range(1, n):
                    kp, kq, kr = (k * p) % n, (k * q) % n, (k * r) % n
                    if kp == 0 and kq == 0 and kr == 0:
                        flag = False
                    else:
                        check_table[(kp, kq, kr)] = True
                if flag and (p**2 + q**2 + r**2) % n != 0:
                    rtv.append((p, q, r))

    return rtv


def check_orthogonal(n1, n2, n):
    return (n1[0] * n2[0] + n1[1] * n2[1] + n1[2] * n2[2]) % n == 0


def check_ang(n1, n2, n, m):
    i_product = n1[0] * n2[0] + n1[1] * n2[1] + n1[2] * n2[2]
    norm1 = n1[0] * n1[0] + n1[1] * n1[1] + n1[2] * n1[2]
    norm2 = n2[0] * n2[0] + n2[1] * n2[1] + n2[2] * n2[2]
    return (m * i_product**2 - norm1 * norm2) % n == 0


def check_60(n1, n2, n):
    return check_ang(n1, n2, n, 4)


def gbc(n, nodes=nodes, check_edge=check_orthogonal):
    ns = nodes(n)

    G = nx.Graph()
    G.add_nodes_from(ns)

    for i, n1 in enumerate(ns):
        for j, n2 in enumerate(ns):
            if i < j:
                if check_edge(n1, n2, n):
                    G.add_edge(n1, n2)

    return G


def order(n):
    rtv = n**2
    for (p, _) in pyprimes.factorise(n):
        rtv *= 1 + 1 / p + 1 / p**2
    return round(rtv)


def order_int(n):
    rtv = 1
    for p, k in pyprimes.factorise(n):
        rtv *= p ** (k * 2) + p ** (k * 2 - 1) + p ** (k * 2 - 2)
    return rtv


def degree(n):
    rtv = n
    for (p, _) in pyprimes.factorise(n):
        rtv *= 1 + 1 / p
    return round(rtv)


def degree_int(n):
    rtv = 1
    for p, k in pyprimes.factorise(n):
        rtv *= p ** k + p ** (k - 1)
    return rtv


def pair(n):
    return order(n), degree(n)


def pair_int(n):
    return order_int(n), degree_int(n)

if __name__ == "__main__":
    def show_n(n, gbc):
        G = gbc(n)
        show(G)

    for i in range(2, 20):
        show(gbc(i))
    '''
  for p in pyprimes.primes_below(50):
    print(p)
    show_n(p, lambda n: gbc(n, nondegenerate_nodes))
    for m in range(1,6):
      print(m)
      show_n(p, lambda n: gbc60(n, nondegenerate_nodes, m))
    print()
  '''
    '''
  for n in range(2,40):
    print(n)
    show_n(n, lambda n: gbc(n, nodes))
    show_n(n, lambda n: gbc(n, nondegenerate_nodes))
    #show_n(n, gbc60)
    print()
  '''
