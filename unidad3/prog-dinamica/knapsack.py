# El problema de la mochila 0/1 - resuelto con fuerza bruta
# 0/1: por cada objeto eliges 0 (no tomarlo) o 1 (tomarlo)
# Lo tomas entero o lo dejas: sin fracciones ni copias repetidas

def cp(A):              # cp = conjunto potencia
    if len(A) == 0:     # conjunto vacío
        return [[]]     # Potencia del conjunto vacío P(∅) = {∅} = 1 elemento
    x = A[0]            # el primer elemento
    B = A[1:]           # el resto del conjunto sin x
    pB = cp(B)          # potencia de b
    gsx = pB                        # grupo sin x
    gcx = [s+[x] for s in pB]       # grupo con x
    return gsx + gcx                # los dos grupos

pesos = [2, 3, 4, 5]
valores = [3, 4, 5, 6]
w = 5
n = len(pesos)
A = range(n)                        # posiciones de los indices de cada elemento

peso = lambda s, p: sum([p[i] for i in s])          # pesos
valor = lambda s, v: sum([v[i] for i in s])         # valores
res = lambda S, p, W: [s for s in S if peso(s, p) <= W]     # resultado
mv = lambda S, v: max([ (valor(s, v), s) for s in S ])      # max valor

todos = cp(A)                          # 1. all 16 subsets
validos = res(todos, pesos, w)         # 2. only the ones that fit
mejor = mv(validos, valores)           # 3. the most valuable one
print(mejor)                           # (7, [1, 0])

## lambdas expandidas

"""
def peso(s, p):
    total = 0
    for i in s:            # each item index in the subset
        total = total + p[i]   # look up its weight and add it
    return total

def valor(s, v):
    total = 0
    for i in s:            # each item index in the subset
        total = total + v[i]   # look up its value and add it
    return total

def res(S, p, W):
    validos = []                 # subsets that fit
    for s in S:
        if peso(s, p) <= W:
            validos.append(s)
    return validos

def mv(S, v):
    mejor_valor = None
    mejor_subconjunto = None
    for s in S:
        val = valor(s, v)
        if mejor_valor is None or val > mejor_valor:
            mejor_valor = val
            mejor_subconjunto = s
    return (mejor_valor, mejor_subconjunto)
"""