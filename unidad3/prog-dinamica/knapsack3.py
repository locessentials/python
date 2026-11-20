# El problema de la mochila 0/1 - resuelto con recursividad

def mochila_dp(p, v, W):
    
    # Crear un arreglo vacío de (n+1) renglones × (W+1) columnas
    A = []                            
    for renglon in range(n + 1):      # un renglón para 0, 1, 2, 3, 4 objetos permitidos
        nuevo_renglon = []            # empezar un renglón vacío
        for c in range(W + 1):        # una posición para cada capacidad: 0, 1, 2, 3, 4, 5
            nuevo_renglon.append(0)   # poner un 0 en esa posición
        A.append(nuevo_renglon)       # agregar el renglón al arreglo

    # A = [[0] * (W + 1) for _ in range(n + 1)]   # Versión abreviada

    # Llenar el arreglo, un renglón a la vez
    for i in range(1, n + 1):          # renglones 1 a 4 (el renglón 0 se queda en ceros)
        for c in range(W + 1):         # capacidades 0 a 5
            peso = p[i-1]              # peso del objeto que agrega este renglón
            val = v[i-1]               # valor del objeto que agrega este renglón

            if peso > c:                            # no cabe
                A[i][c] = A[i-1][c]                 # copiar el valor del renglón de arriba
            else:
                nto = A[i-1][c]                     # no tomar objeto: renglón de arriba, misma columna
                to = val + A[i-1][c - peso]         # tomar objeto: el valor de este objeto
                                                    # + el mayor valor que los objetos anteriores pueden agregar
                                                    # en el espacio que queda después de meter este objeto
                A[i][c] = max(nto, to)              # seleccionar la mejor de las dos opciones
    return A

def reconstruir(A, p, v, W):
    S = []          # los objetos que vamos encontrando (empieza vacío)
    c = W           # espacio en la mochila: empieza con la mochila completa (5 kg)

    for i in range(n, 0, -1):          # empezar en n, parar ANTES de 0, bajar de 1 en 1
        peso = p[i-1]                  # peso del objeto que agrega este renglón
        val = v[i-1]                   # valor del objeto que agrega este renglón

        if peso <= c:                              # el objeto cabe en el espacio que queda
            to = val + A[i-1][c - peso]            # tomar - total si se agrega el objeto
            nto = A[i-1][c]                        # no tomar - total si no se lo agrega
            if to >= nto:                          # si tomarlo fue la mejor opción (en empate, se toma)
                S.append(i-1)                      # anotar el número del objeto
                c = c - peso                       # ueda menos espacio

    return S

p = [2, 3, 4, 5]
v = [3, 4, 5, 6]
W = 5
n = len(p)

A = mochila_dp(p, v, W)
print("Valor máximo:", A[n][W])                      # 7
print("Subconjunto:", reconstruir(A, p, v, W))           # [1, 0]