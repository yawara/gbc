import math

from gbc_without_sage import pair_int
import pyprimes

MAX_P = 1000000
MAX_K = int(math.log(MAX_P, 2))
pks = []
for p in pyprimes.primes_below(MAX_P):
    for k in range(1, MAX_K):
        pks.append(p**k)
pks.sort()

MAX_VALID_DEGREE = MAX_P + 1
print(MAX_VALID_DEGREE)


def is_new_record(order, degree):
    if degree > MAX_VALID_DEGREE:
        raise Exception
    for pk in pks:
        if pk + 1 > degree:
            break
        else:
            q = pk

    h = degree - (q + 1)

    return order > q**2 + q + 1 + h

if __name__ == '__main__':
    for p in pyprimes.primes_below(MAX_P):
        for k in range(2, MAX_K):
            q = p ** k
            if q + 1 > MAX_VALID_DEGREE:
                break
            for n in range(2, 1000):
                print("check p:%d k:%d n:%d" % (p, k, n))
                o, d = pair_int(n)
                if p == 2:
                    new_o = (q ** 2 + q + 2) * o
                else:
                    new_o = (q ** 2 + q + 1) * o
                new_d = (q + 1) * d
                if new_d < MAX_VALID_DEGREE and is_new_record(new_o, new_d):
                    print(p, k, n)
