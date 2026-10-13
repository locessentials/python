# Leer la entrada

# m = número de productores
# n = número de compradores

m, n = map(int, input().split())

# p = precio
# d = día en que el primer producto sería listo

prod = []
for _ in range(m):
    prod.append(list(map(int, input().split())))

# c = costo
# z = fin, día en que el vendedor parará de comprar producto

comp = []
for _ in range(n):
    comp.append(list(map(int, input().split())))

# Establecer funciones para reordenar los datos

def ord_prod(productor):            # Ordenar por día inicial de menor a mayor
    precio = productor[0]
    dia = productor[1]
    return (dia, precio)

def ord_comp(comprador):            # Ordenar por día final de mayor a menor
    precio = comprador[0]
    dia = comprador[1]
    return (-dia, -precio)

# 1. Poda

# Productores: conservar solo si es más barato que todos los anteriores
prod.sort(key=ord_prod)             # Ordenar por día inicial de menor a mayor
prod_c = []                         # prod_c = productores competitivos
min_precio = float('inf')           # float('inf') means infinity
                                    # First producer: any price is < infinity, so it's kept.
for p, d in prod:
    if p < min_precio:
        prod_c.append((p, d))
        min_precio = p

# Compradores: conservar solo si paga más que todos los que terminan después
comp.sort(key=ord_comp)             # Ordenar por día final de mayor a menor
comp_c = []                         # comp_c = compradores competitivos
max_costo = 0
for c, z in comp:
    if c > max_costo:
        comp_c.append((c, z))
        max_costo = c
comp_c.reverse()                    # Dejar los compradores de menor a mayor día

# 2. Divide y vencerás
# (c − p) × (z − d)

# Ganancia de un par productor–comprador
def ganancia(productor, comprador):
    p = productor[0]
    d = productor[1]
    c = comprador[0]
    z = comprador[1]
    if c < p and z < d:             # Los dos negativos darían una ganancia falsa
        return float('-inf')
    return (c - p) * (z - d)
 
mejor_total = 0
mejor_par = None
 
def buscar(p_ini, p_fin, c_ini, c_fin):     # ini - inicio de la lista de productores / compradores
                                            # fin - fin de la lista de productores / compradores
    global mejor_total, mejor_par   # De variables afuera de la función
    if p_ini > p_fin:               # No quedan productores en este tramo
        return
    mitad = (p_ini + p_fin) // 2
    mejor = float('-inf')
    mejor_c = c_ini
    for pos_c in range(c_ini, c_fin + 1):          # Buscar mejor comprador para el productor del medio
        g = ganancia(prod_c[mitad], comp_c[pos_c])
        if g > mejor:
            mejor = g
            mejor_c = pos_c
    if mejor > mejor_total:
        mejor_total = mejor
        mejor_par = (prod_c[mitad], comp_c[mejor_c])
    buscar(p_ini, mitad - 1, c_ini, mejor_c)   # Productores anteriores: compradores hasta mejor_c
    buscar(mitad + 1, p_fin, mejor_c, c_fin)   # Productores posteriores: compradores desde mejor_c
 
buscar(0, len(prod_c) - 1, 0, len(comp_c) - 1)
print(mejor_total)
print(mejor_par)                    # (precio, día, posición) del productor y del comprador

# Get-Content dsample1.txt | python d.py > 5
# Get-Content dsample2.txt | python d.py > 0
 