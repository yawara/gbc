import pyprimes


def is_new_record(order, degree):
    k = 1
    while True:
        pks = list(pyprimes.factorise(degree - k))
        if len(pks) == 1:
            break
        k += 1
    p, k = pks[0]
    q = p**k
    o, d = q**2 + q + 1, q + 1
    return order > o + (degree - d)


if __name__ == '__main__':
    for p in pyprimes.primes_below(1000):
        for k in range(2, 10):
            for d in range(1, k):
                assert k > d
                N, M = p**k, p**d
                if is_new_record(N**2 + N * M + M**2, N + M):
                    print("p: %d, k: %d, d: %d" % (p, k, d))
