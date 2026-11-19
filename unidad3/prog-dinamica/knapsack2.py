# 0/1 knapsack problem
# 0/1: por cada objeto eliges 0 (no tomarlo) o 1 (tomarlo)
# Lo tomas entero o lo dejas: sin fracciones ni copias repetidas

def mochila(p, v, W, n):           # W: The remaining weight capacity of your backpack.
                                # n: The number of items currently available to choose from 
                                # (it looks at the first n items in the list)
    if n == 0 or W == 0:
        return 0
    if (p[n-1] > W):
        return mochila(p, v, W, n-1)
    nto = mochila(p, v, W, n-1)                    # nto = no tomar objeto
    to = v[n-1] + mochila(p, v, W - p[n-1], n-1)   # to = tomar objeto
    return max(nto, to)

def cp(A):
    if len(A)==0:
        return [[]]
    x=A[0]
    B=A[1:]
    pB=cp(B)
    gsx=pB
    gcx=[sc+[x] for sc in pB]
    return gsx+gcx

peso = lambda s, p: sum(p[i] for i in s)

valor = lambda s, v: sum(v[i] for i in s)

res = lambda S, p, W: [s for s in S if peso(s, p) <= W]

mv = lambda S, v: max([(valor(s, v), s) for s in S])

p = [2, 3, 4, 5]
v = [3, 4, 5, 6]
W = 5
n = len(p)
A = range(n)

print(f"Valor maximo: {mochila(p, v, W, n)}")