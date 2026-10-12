# Leer la entrada
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
not_zero = 0
for row in rows:
    for a in row:
        if a > 0:
            not_zero += 1

# Emparejamiento: encontrar las pilas compartidas
match_col = [-1] * n    # n = número de columnas (de arriba)
                        # crea una lista con un lugar por columna, empezando en -1
                        # Por ejemplo: [-1] * 5   →   [-1, -1, -1, -1, -1]; luego
                        # match_col[j] == -1 significa que la columna j todavía no está emparejada con ningún renglón
                        # match_col[j] == i significa que la columna j está emparejada con el renglón i ("comparten" una pila).
 
# i = número de renglón
# j = número de columna

def try_match(i, seen):                     # Intenta encontrarle pareja al renglón i
                                            # seen = lista de las columnas que ya se probaron
                                            # durante la búsqueda de un renglón; evita que el programa se quede dando vueltas
    for j in range(n):                      # revisa cada columna, de izquierda a derecha
        can_share = (max_rows[i] == max_columns[j]) and rows[i][j] > 0
        # compara cada valor de max_columns con una posición de max_rows
        # para encontrar dónde son iguales y distintos de cero; regresa True o False
        if can_share == True and seen[j] == False:
            seen[j] = True                  # marca la columna j como ya revisada
            if match_col[j] == -1 or try_match(match_col[j], seen):
            # match_col[j] == -1     Es True cuando la columna j todavía no tiene renglón: está abierta
            # try_match(match_col[j], seen)     match_col[j] = el renglón que ya está en la columna j.
            #                                   Al llamar try_match con ese número de renglón se vuelve
            #                                   a ejecutar este mismo ciclo, ahora buscando para ESE renglón.
            #                                   seen[j] ya es True, así que el ciclo se salta la columna j.
            #                                   Si encuentra una columna libre, se acomoda ahí
            #                                   y regresa True → de vuelta aquí, el renglón i se queda con la columna j.
            #                                   Si no, regresa False → el renglón i sigue buscando.
                match_col[j] = i
                return True     # "este renglón encontró columna"
                                # El if que hizo la llamada recibe True:
                                #  - línea recursiva → el renglón anterior se movió, así que se ejecuta match_col[j] = i
                                #  - ciclo de abajo  → se suma el descuento de este renglón
    return False                # Solo se llega aquí después de revisar todas las columnas sin éxito.
                                # "este renglón no encontró nada." El if que hizo la llamada recibe False:
                                #  - línea recursiva → el renglón anterior no se puede mover, así que se salta
                                #                      match_col[j] = i y se prueba la siguiente j
                                #  - ciclo de abajo  → no hay descuento para este renglón
 
discount = 0                            # cajas que nos ahorramos al dejar que renglones y columnas compartan pilas
for i in range(m):                      # recorre todos los renglones, de arriba abajo
    if max_rows[i] > 0:                 # se salta los renglones que son puros ceros (no hay nada que emparejar)
        seen = [False] * n              # lista nueva para la búsqueda de este renglón: todavía no se prueba ninguna columna
        if try_match(i, seen):          # intenta emparejar el renglón i con una columna que tenga el mismo máximo
            discount += max_rows[i] - 1 # ¡emparejados! el renglón y la columna pueden usar UNA sola pila alta
                                        # en lugar de dos, así que nos ahorramos la altura de esa pila.
                                        # -1 porque 1 caja de esa pila ya está contada
                                        # en not_zero (cada posición distinta de cero conserva al menos 1)

# Cajas que quedan y cajas robadas
left = (not_zero
        + sum(h - 1 for h in max_rows if h > 0)
        + sum(h - 1 for h in max_columns if h > 0)
        - discount)

print(total - left)

# Get-Content csample1.txt | python c.py > 9
# Get-Content csample2.txt | python c.py > 30