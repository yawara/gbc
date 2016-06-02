import pyprimes

from gbc_without_sage import pair_int

rtv = []

for n in range(2, 1000):
    rtv.append((pair_int(n), n))

for p in pyprimes.primes_below(100):
    for k in range(2, 10):
        q = p**k
        rtv.append(((q**2 + q + 1, q + 1), (p, k)))

rtv.sort()

for pair in rtv:
    print(pair)
