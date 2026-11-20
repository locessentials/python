# El problema de la mochila 0/1 - resuelto con recursividad

def mochila(p, v, W, n):        # W: capacidad restante de la mochila
                                # n: número de objetos que quedan por considerar
    if n == 0 or W == 0:
        return 0
    if p[n-1] > W:                      # no cabe, saltamos el objeto
        return mochila(p, v, W, n-1)    # ahora resuelve el problema para n-1
    # cabe: probamos las dos opciones
    nto = mochila(p, v, W, n-1)                     # nto = no tomar objeto
                                                    # los demás subconjuntos quizás valen más
    to = v[n-1] + mochila(p, v, W - p[n-1], n-1)    # to = tomar objeto
                                                    # v[n-1] - sumamos su valor
                                                    # W - p[n-1]: queda menos capacidad
    return max(nto, to)                             # encuentra la mejor de las dos

p = [2, 3, 4, 5]
v = [3, 4, 5, 6]
W = 5
n = len(p)

print(f"Valor maximo: {mochila(p, v, W, n)}")   # Valor maximo: 7