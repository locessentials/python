# PASO 0: LEER LAS ENTRADAS

# d = número de valores distintos de rojo que aparecen en la imagen original
# k = número de valores distintos de rojo permitidos en la imagen posterizada

d, k = map(int, input().split())

# r = valor de intensidad del rojo
# p = número de píxeles que tienen la intensidad de rojo r

red_v = []          # valores de intensidad del rojo y su p
for _ in range(d):
    red_v.append(list(map(int, input().split())))

# PASO 1: DEFINIR UNA FUNCIÓN QUE CALCULA EL ERROR DE UN SOLO GRUPO

# Error si todas las intensidades desde una posición inicio hasta una posición fin
# de red_v (ambas incluidas) se cambian a un solo valor v, el mejor posible.
def group_error(start, end):
    total_pixels = 0
    weighted_sum = 0
    for position in range(start, end + 1):
        r, p = red_v[position]                      # red_v[posicion] = posicion en el indice
        total_pixels = total_pixels + p
        weighted_sum = weighted_sum + (p * r)

    # promedio ponderado: v = Σ(p × r) / Σp
    # // redondea hacia abajo (83.33 → 83); también probamos el entero de arriba (84)
    v_low = weighted_sum // total_pixels
    v_high = v_low + 1

    error_low = 0
    error_high = 0
    for position in range(start, end + 1):
        r, p = red_v[position]
        # error si usamos v_low: distancia entre r y v_low, al cuadrado,
        # multiplicada por los p píxeles que tienen la intensidad r
        error_low = error_low + p * (r - v_low) ** 2
        # lo mismo, pero si usamos v_high
        error_high = error_high + p * (r - v_high) ** 2

    return min(error_low, error_high)

# PASO 2: CREAR UNA TABLA CON EL ERROR DE CADA GRUPO POSIBLE

# Un grupo se define por dónde empieza (start) y dónde termina (end).
# error_table[start][end] guarda el error del grupo que va de start a end.
# start = en qué lista estamos, end = en qué posición de la lista estamos
# Calculamos cada error una sola vez para que el Paso 3 solo tenga que consultarlo.

error_table = []                                # tabla vacía; al final tendrá d renglones
for start in range(d):                          # para cada posición donde puede empezar un grupo
    row = [0] * d                               # crear un renglón de d espacios en 0
                                                # por ejemplo: [0, 0, 0, 0]
    for end in range(start, d):                 # para cada posición donde puede terminar el grupo,
                                                # desde start hasta la última
        row[end] = group_error(start, end)      # guardar el error de ese grupo en la columna end
    error_table.append(row)                     # agregar el renglón completo a la tabla

# PASO 3: PROGRAMACIÓN DINÁMICA

# num_groups = número de grupos en que dividimos las intensidades (de 1 a k)
# covered = cuántas intensidades de rojo incluimos en esta parte del problema
# contando desde la primera (de un universo de 1 a d)
# best_error[num_groups][covered] = el error mínimo para las primeras "covered"
# "cubiertas" intensidades usando exactamente num_groups grupos

INFINITY = 2 ** 63      # means "not possible yet"; a whole number, not a float
 
best_error = []                                     # tabla vacía; al final tendrá k + 1 listas
                                                    # p. ej., if k = 2, tenemos tres listas
for num_groups in range(k + 1):                     # una lista por cada número de grupos (de 0 a k)
    best_error.append([INFINITY] * (d + 1))         # cada lista tiene d + 1 espacios en INFINITY
                                                    # (INFINITY = todavía no se puede)

best_error[0][0] = 0                                # punto de partida: lista 1, posición 1 en la lista 
                                                    # 0 intensidades con 0 grupos no tienen error

for num_groups in range(1, k + 1):              # llenar la lista de 1 grupo, luego la de 2, hasta k
    for covered in range(num_groups, d + 1):    # cubrir las primeras intensidades: primero pocas, luego más
        for last_start in range(num_groups - 1, covered):  # probar cada lugar donde puede empezar el último grupo (dónde va el corte)
            error_before = best_error[num_groups - 1][last_start]   # mejor error antes del corte, con un grupo menos (ya guardado)
            error_last = error_table[last_start][covered - 1]       # error del último grupo (de la tabla de errores)
            if error_before + error_last < best_error[num_groups][covered]:   # si este corte da menos error total
                best_error[num_groups][covered] = error_before + error_last   # guardarlo como el mejor

print(best_error[k][d])                             # respuesta: todas las d intensidades con k grupos

# Get-Content fsample1.txt | python e.py > 66670000
# Get-Content fsample2.txt | python e.py > 0
# Get-Content fsample3.txt | python e.py > 37500000