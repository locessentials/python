# Quick sort with fixed pivot

def qsf(a):
    if len(a) <= 1:
        return a
    piv = a[-1]
    men = [x for x in a if x < piv]
    igual = [x for x in a if x == piv]
    may = [x for x in a if x > piv]

    return qsf(men) + igual + qsf(may)

a = [8, 3, 1, 7, 0, 10, 2, 5]

print(qsf(a))

# Quick sort with random pivot

import random

def qsr(a):
    if len(a) <= 1:
        return a
    piv = random.choice(a)
    print(f"Pivot point: {piv}")
    men = [x for x in a if x < piv]
    igual = [x for x in a if x == piv]
    may = [x for x in a if x > piv]

    return qsr(men) + igual + qsr(may)

a = [8, 3, 1, 7, 0, 10, 2, 5]

print(qsr(a))