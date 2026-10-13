# d = number of distinct red values that occur in the original image
# k = number of distinct red values allowed in the posterized image

d, k = map(int, input().split())

# r = red intensity value
# p = number of pixels having red intensity r

red_v = []          # red intensity values
for _ in range(d):
    red_v.append(list(map(int, input().split())))

# Paso 1: costo de un grupo

# Error si todas las intensidades desde una posición inicio hasta una posición fin
# de red_v (ambas incluidas) se cambian a un solo valor v, el mejor posible.
def costo_grupo(inicio, fin):
    total_pixeles = 0
    suma_ponderada = 0
    for posicion in range(inicio, fin + 1):
        r, p = red_v[posicion]
        total_pixeles = total_pixeles + p
        suma_ponderada = suma_ponderada + p * r
 
    # promedio ponderado: v = Σ(p × r) / Σp
    # // redondea hacia abajo (83.33 → 83); también probamos el entero de arriba (84)
    v_abajo = suma_ponderada // total_pixeles
    v_arriba = v_abajo + 1
 
    error_abajo = 0
    error_arriba = 0
    for posicion in range(inicio, fin + 1):
        r, p = red_v[posicion]
        error_abajo = error_abajo + p * (r - v_abajo) ** 2
        error_arriba = error_arriba + p * (r - v_arriba) ** 2
 
    return min(error_abajo, error_arriba)
 
 
# Paso 2: tabla de costos de todos los grupos posibles
# costo[inicio][fin] = costo_grupo(inicio, fin), calculado una sola vez
costo = []
for inicio in range(d):
    fila = [0] * d
    for fin in range(inicio, d):
        fila[fin] = costo_grupo(inicio, fin)
    costo.append(fila)
 
 
# Paso 3: programación dinámica
# mejor_error[grupos][cubiertas] = error mínimo para cubrir las primeras
# "cubiertas" intensidades usando exactamente "grupos" grupos
INFINITO = 2 ** 63      # "todavía no se puede"; entero, para no usar float
 
mejor_error = []
for grupos in range(k + 1):
    mejor_error.append([INFINITO] * (d + 1))
 
mejor_error[0][0] = 0   # 0 intensidades con 0 grupos: error 0
 
for grupos in range(1, k + 1):
    for cubiertas in range(grupos, d + 1):
        # ¿dónde empieza el último grupo? Probamos cada posición posible
        for inicio_ultimo in range(grupos - 1, cubiertas):
            antes = mejor_error[grupos - 1][inicio_ultimo]
            ultimo = costo[inicio_ultimo][cubiertas - 1]
            if antes + ultimo < mejor_error[grupos][cubiertas]:
                mejor_error[grupos][cubiertas] = antes + ultimo
 
print(mejor_error[k][d])









# Get-Content fsample1.txt | python e.py > 66670000
# Get-Content fsample2.txt | python e.py > 0
# Get-Content fsample3.txt | python e.py > 37500000