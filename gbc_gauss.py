from itertools import combinations, product
from collections import defaultdict

import matplotlib.pyplot as plt
import networkx as nx
import numpy as np


def GZmod(n):
    a, b = int(n.real), int(n.imag)
    range_GZmod = range(int((- abs(a) - abs(b)) / 2), int((abs(a) + abs(b)) / 2) + 1)

    for i in range_GZmod:
        for j in range_GZmod:
            if a * (2 * i - a) + b * (2 * j - b) <= 0 and (-b) * (2 * i + b) + a * (2 * j - a) <= 0 and a * (2 * i + a) + b * (2 * j + b) > 0 and (-b) * (2 * i - b) + a * (2 * j + a) > 0:
                yield complex(i, j)


def show_GZmod(n):
    a, b = int(n.real), int(n.imag)

    plt.grid()
    plt.xlim(-abs(a) - abs(b), abs(a) + abs(b))
    plt.ylim(-abs(a) - abs(b), abs(a) + abs(b))

    plt.plot([a, -b, -a, b], [b, a, -b, -a], 'or')

    # plt.plot([(a - b) / 2, (-a - b) / 2, (-a + b) / 2, (a + b) / 2],
    #         [(a + b) / 2, (a - b) / 2, (-a - b) / 2, (-a + b) / 2], 'or')

    X, Y = [], []
    for c in GZmod(n):
        i, j = int(c.real), int(c.imag)
        X.append(i)
        Y.append(j)
    plt.plot(X, Y, 'ob')

    plt.plot([(a - b) / 2, (-a - b) / 2], [(a + b) / 2, (a - b) / 2], '--k')
    plt.plot([(-a - b) / 2, (-a + b) / 2], [(a - b) / 2, (-a - b) / 2], '--k')
    plt.plot([(-a + b) / 2, (a + b) / 2], [(-a - b) / 2, (-a + b) / 2], '--k')
    plt.plot([(a + b) / 2, (a - b) / 2], [(-a + b) / 2, (a + b) / 2], '--k')

    plt.show()


def remainder(n, N):
    fq = n / N
    q = complex(round(fq.real), round(fq.imag))

    r = n - q * N

    if r in GZmod(N):
        return r
    else:
        a, b = N.real, N.imag
        i, j = r.real, r.imag
        if a * (2 * i + a) + b * (2 * j + b) == 0 and (-b) * (2 * i - b) + a * (2 * j + a) == 0:
            return r + (1 + 1j) * N
        elif a * (2 * i + a) + b * (2 * j + b) == 0:
            return r + N
        elif (-b) * (2 * i - b) + a * (2 * j + a) == 0:
            return r + 1j * N
        else:
            raise Exception


def nodes(n):
    rtv = []
    check_table = defaultdict(bool)

    for p, q, r in product(GZmod(n), repeat=3):
        if p == 0 and q == 0 and r == 0:
            continue
        flag = True
        if not check_table[(p, q, r)]:
            for k in GZmod(n):
                if k == 0:
                    continue
                kp, kq, kr = remainder(k * p, n), remainder(k * q, n), remainder(k * r, n)
                if kp == 0 and kq == 0 and kr == 0:
                    flag = False
                else:
                    check_table[(kp, kq, kr)] = True
            if flag:
                rtv.append((p, q, r))

    return rtv


def is_orthogonal(x, y, N):
    tmp = 0
    for xi, yi in zip(x, y):
        tmp += xi * yi
    return remainder(tmp, N) == 0


def gbc(n):
    G = nx.Graph()
    ns = nodes(n)
    for x, y in combinations(ns, 2):
        if is_orthogonal(x, y, n):
            G.add_edge(x, y)
    return G


def show_graph(n):
    G = gbc(n)
    ldegs = list(set(G.degree().values()))
    ldegs.sort()
    print(len(G), tuple(ldegs), nx.diameter(G))
