# ===== Paso 1: leer la entrada =====
# Lee los vértices del polígono

# Collects the inputs
n = int(input())
vertices = []

for p in range(n):
    point = tuple(map(int, input().split())) 
    vertices.append(point)

# ===== Paso 2: funciones de geometría =====
# Producto cruz: su signo dice de qué lado de la recta AB está el punto P

def cross(A, B, P):
    x1, y1 = A
    x2, y2 = B
    x3, y3 = P
    return (x2-x1) * (y3-y1) - (y2-y1) * (x3-x1)

# Prueba de cruce: True si el lado CD cruza la recta AB (sus extremos quedan en lados opuestos)
def crosses(A, B, C, D):
    return cross(A, B, C) * cross(A, B, D) < 0

# Regresa t: dónde el lado CD choca con la recta AB (0 en A, 1 en B, >1 después de B, <0 antes de A)
def crossing_t(A, B, C, D):
    a = cross(C, D, A)
    b = cross(C, D, B)
    return a / (a - b)

# True si el punto P está sobre el lado CD (con un margen pequeño para errores de redondeo)
def on_wall(C, D, P):
    x1, y1 = C
    x2, y2 = D
    x, y = P
    length = ((x2 - x1)**2 + (y2 - y1)**2) ** 0.5
    if abs(cross(C, D, P)) > 1e-7 * length:   # no está sobre la recta del lado
        return False
    # está sobre la recta: ¿está entre C y D?
    return min(x1, x2) - 1e-7 <= x <= max(x1, x2) + 1e-7 and \
           min(y1, y2) - 1e-7 <= y <= max(y1, y2) + 1e-7

# Método del rayo: True si P está dentro del polígono o sobre su borde
def inside(P):
    x, y = P
    result = False
    for i in range(n):
        C = vertices[i]
        D = vertices[(i + 1) % n]          # % n regresa del último vértice al primero
        if on_wall(C, D, P):
            return True                    # estar sobre el borde cuenta como estar dentro
        x1, y1 = C
        x2, y2 = D
        if (y1 > y) != (y2 > y):           # el lado pasa por la altura de P
            x_hit = x1 + (y - y1) * (x2 - x1) / (y2 - y1)
            if x_hit > x:                  # el cruce está a la derecha de P
                result = not result        # cada cruce cambia de dentro a fuera, o de fuera a dentro
    return result

# Regresa el punto en la posición t de la recta AB
def point_at(A, B, t):
    x1, y1 = A
    x2, y2 = B
    return (x1 + t * (x2 - x1), y1 + t * (y2 - y1))

# Revisa si el pedazo de la recta AB entre t1 y t2 está dentro (prueba su punto medio)
def piece_inside(A, B, t1, t2):
    return inside(point_at(A, B, (t1 + t2) / 2))

# ===== Paso 3: probar cada recta que pasa por dos vértices =====
# La pista más larga siempre toca dos vértices, así que basta probar cada par A, B

best = 0.0

for i in range(n):
    for j in range(i + 1, n):
        A = vertices[i]
        B = vertices[j]
        dx = B[0] - A[0]
        dy = B[1] - A[1]
        ab_length = (dx**2 + dy**2) ** 0.5

        # 3.1 todos los t donde el borde toca la recta AB
        ts = []
        for V in vertices:                       # vértices que están sobre la recta
            if cross(A, B, V) == 0:
                ts.append(((V[0] - A[0]) * dx + (V[1] - A[1]) * dy) / (dx**2 + dy**2))
        for k in range(n):                       # lados que cruzan la recta
            C = vertices[k]
            D = vertices[(k + 1) % n]
            if crosses(A, B, C, D):
                ts.append(crossing_t(A, B, C, D))

        # 3.2 ordenar los t; cortan la recta en pedazos
        ts.sort()
        start = ts.index(0.0)                    # posición de A en la lista
        end = ts.index(1.0)                      # posición de B en la lista

        # 3.3 cada pedazo entre A y B debe estar dentro; si no, pasar al siguiente par
        ok = True
        for k in range(start, end):
            if not piece_inside(A, B, ts[k], ts[k + 1]):
                ok = False
                break
        if not ok:
            continue

        # 3.4 extender hacia atrás de A mientras los pedazos sigan dentro
        
        lo = start
        while lo > 0 and piece_inside(A, B, ts[lo - 1], ts[lo]):
            lo -= 1

        # y extender hacia adelante de B mientras los pedazos sigan dentro
        hi = end
        while hi < len(ts) - 1 and piece_inside(A, B, ts[hi], ts[hi + 1]):
            hi += 1

        # 3.5 longitud de la pista = (fracción de AB) × longitud de AB; guardar la mayor
        best = max(best, (ts[hi] - ts[lo]) * ab_length)

# ===== Paso 4: imprimir el resultado =====

print(f"{best:.9f}")

# Get-Content asample1.txt | python a.py > 76.157731059
# Get-Content asample2.txt | python a.py > 4510.149110617