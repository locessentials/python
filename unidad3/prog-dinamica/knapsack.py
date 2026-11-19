def cp(a):              # conjunto potencia
    if len(a) == 0:     # conjunto vacío
        return [[]]     # Potencia del conjunto vacío P(∅) = {∅} = 1 elemento
    x = a[0]
    b = a[1:]
    pb = cp(b)
    gsx = pb
    gcx = [s+[x] for s in pb]
    return gsx + gcx

pesos = [2, 3, 4, 5]
valores = [3, 4, 5, 6]
w = 5

n = len(pesos)
a = range(n)

peso = lambda s, p: sum([p[i] for i in s])          # pesos
valor = lambda s, v: sum([v[i] for i in s])         # valores
res = lambda S, p, W: [s for s in S if peso(s, p) <= W]
mv = lambda S, v: max([ (valor(s, v), s) for s in S ])   # max valor