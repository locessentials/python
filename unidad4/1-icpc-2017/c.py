# PREPARACIÓN: LEER Y ORGANIZAR LAS ENTRADAS

# Tamaño de la cuadricula

# m = número de renglones
# n = número de columnas

m, n = map(int, input().split())
rows = []
for _ in range(m):
    rows.append(list(map(int, input().split())))

# Total de cajas
total = 0
for row in rows:
    total += sum(row)

# Máximo para renglones y columnas
columns = list(zip(*rows))      # *rows desempaca la lista exterior,
                                # así que zip recibe los 5 renglones como argumentos separados.
                                # zip toma el primer elemento de cada renglón y los agrupa,
                                # luego el segundo de cada uno, y así sucesivamente.

max_rows = []
max_columns = []

for row in rows:
    max_rows.append(max(row))

for column in columns:
    max_columns.append(max(column))

# Posiciones distintas de cero
not_zero = 0            # guarda cuántas posiciones tienen al menos una caja (no son 0)
                        # que se quedan con mínimo 1 caja para que la cámara de arriba vea lo mismo
for row in rows:
    for a in row:
        if a > 0:
            not_zero += 1

# EMPAREJAMIENTO: ENCONTRAR LAS POSICIONES MÁXIMAS COMPARTIDAS

match_col = [-1] * n    # n = número de columnas (de arriba)
                        # crea una lista con un lugar por columna, empezando en -1
                        # Por ejemplo: [-1] * 5   →   [-1, -1, -1, -1, -1]; luego
                        # match_col[j] == -1 significa que la columna j todavía no está emparejada con ningún renglón
                        # match_col[j] == i significa que la columna j está emparejada con el renglón i ("comparten" una pila)
 
# i = número de renglón
# j = número de columna

def try_match(i, seen):                     # Intenta encontrarle pareja al renglón i
                                            # seen = lista de las columnas que ya se probaron
                                            # durante la búsqueda de un renglón; evita que el programa se quede dando vueltas
    for j in range(n):                      # para cada columna en el número total de columnas
        can_share = (max_rows[i] == max_columns[j]) and rows[i][j] > 0
        # compara el máximo del renglón i con el máximo de cada columna
        # max_rows[i] == max_columns[j] – ¿tienen el mismo máximo? V o F
        # rows[i][j] > 0 – ¿hay por lo menos una caja en esta posición? V o F
        # can_share = V solamente si las dos partes son V, si no lo son, es F
        if can_share == True and seen[j] == False:
            seen[j] = True                  # marca la columna j como ya revisada en esta búsqueda
            if match_col[j] == -1 or try_match(match_col[j], seen):
            # match_col es como una hoja de registro: dice qué renglón usa cada columna
            # match_col[j] == -1 – V cuando la columna j está libre
            # try_match(match_col[j], seen) – si la columna j está ocupada, match_col[j] es
            #     el número del renglón que la usa. Le pregunta a ese renglón si se puede
            #     cambiar a otra columna: V si se cambió, F si no pudo
            # si las dos partes son F, no se escribe nada y se prueba la siguiente columna
                match_col[j] = i            # el renglón i se queda con la columna j
                return True                 # sí encontró columna; 
                                            # regresa V a la línea que llamó a try_match
    return False                            # revisó todas las columnas y ninguna funcionó;
                                            # regresa F a la línea que llamó a try_match

counted_twice = 0                       # Cajas de las posiciones compartidas que se cuentan dos veces
for i in range(m):                      # para cada renglón en el número total de renglones
    if max_rows[i] > 0:                 # el máximo del renglón tiene que ser mayor que 0
                                        # (si el máximo es 0, todos los elementos también son 0
                                        # y no hay nada que emparejar)
        seen = [False] * n              # inicializa una lista con un F por columna
                                        # (por ejemplo, si n = 3: [F, F, F])
                                        # donde ninguna columna ha sido revisada todavía
        if try_match(i, seen):          # revisa cada columna y empareja el renglón i con una
                                        # que tenga el mismo máximo (y una posición distinta de 0)
            counted_twice += max_rows[i] - 1  # emparejados: una sola posición sirve para los dos máximos
                                              # -1 porque 1 caja ya está contada en not_zero

# CÁLCULO FINAL

# Cajas que quedan
row_crates = 0                          
for row_max in max_rows:                # Añade las cajas que necesita cada row_max...
    if row_max > 0:
        row_crates += row_max - 1       # ... menos la caja ya contada en not_zero

column_crates = 0
for column_max in max_columns:          # Añade las cajas que necesita cada column_max...
    if column_max > 0:
        column_crates += column_max - 1 # ... menos la caja ya contada en not_zero

left = not_zero + row_crates + column_crates - counted_twice

# Cajas robadas
print(total - left)

# Get-Content csample1.txt | python c.py > 9
# Get-Content csample2.txt | python c.py > 30

# EXTENSIÓN: MAPA DE CAJAS QUE QUEDAN EN CADA POSICIÓN

# Paso 1: la cámara de arriba
# cada posición que no es 0 se queda con 1 caja; las posiciones vacías siguen en 0
crate_map = []
for row in rows:
    new_row = []
    for a in row:
        if a > 0:
            new_row.append(1)
        else:
            new_row.append(0)
    crate_map.append(new_row)

# Paso 2: posiciones compartidas
# match_col dice qué renglón usa cada columna; ahí va una sola pila
# que cuenta como la máxima del renglón y de la columna a la vez
row_done = [False] * m          # V cuando el renglón ya tiene su pila máxima en el mapa
column_done = [False] * n       # V cuando la columna ya tiene su pila máxima en el mapa

for j in range(n):
    if match_col[j] != -1:
        i = match_col[j]
        crate_map[i][j] = max_columns[j]
        row_done[i] = True
        column_done[j] = True

# Paso 3: renglones sin pareja
# su pila máxima va en la posición donde estaba su máximo original
# (esa posición no es 0 y no supera el máximo de su columna)
for i in range(m):
    if max_rows[i] > 0 and row_done[i] == False:
        j = rows[i].index(max_rows[i])      # .index() da la primera columna con ese valor
        crate_map[i][j] = max_rows[i]

# Paso 4: columnas sin pareja
# igual que el paso 3, pero buscando dentro de la columna
for j in range(n):
    if max_columns[j] > 0 and column_done[j] == False:
        i = columns[j].index(max_columns[j])  # .index() da el primer renglón con ese valor
        crate_map[i][j] = max_columns[j]

# Imprimir el mapa, un renglón por línea
for row in crate_map:
    line = ""
    for number in row:
        line = line + str(number) + " "
    print(line.strip())                 # .strip() quita el espacio extra del final