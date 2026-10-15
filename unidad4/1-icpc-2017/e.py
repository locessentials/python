# LEER LA ENTRADA

# n = número de segmentos de su viaje
# t = tiempo total

n, t = map(int, input().split())

# lista de [[d, s], [d, s]]
# d = distancia
# s = lectura del velocímetro sin calibrar

segmentos = []
for _ in range(n):
    segmentos.append(list(map(int, input().split())))

# Inicialización de los límites de búsqueda

low_s = float("inf")        # Iniciar el límite para que en el primer paso
                            # s sea automáticamente más pequeño que low_s (infinito positivo)
for d, s in segmentos:
    if s < low_s:
        low_s = s
lo = -low_s                 # límite inferior: c más bajo posible

hi = 1001001                # límite superior: c suficientemente grande

# Función de evaluación

def T(c):                   # c = constante de velocidad que buscamos
                            # T = tiempo total del viaje si la constante fuera c
    running = 0             # total acumulado del tiempo de los segmentos
    for d, s in segmentos:
        segmento = d / (s + c)
        running += segmento
    return(running)

# Algoritmo de búsqueda binaria

for _ in range(100):
    mid = (lo + hi) / 2
    if T(mid) > t:
        lo = mid
    else:
        hi = mid

# Imprimir el resultado

print(f"{hi:.9f}")          # hi redondeado a 9 decimales
                            # f indica que se muestre como número decimal normal (punto fijo)

# Get-Content esample1.txt | python e.py > 3.000000000
# Get-Content esample2.txt | python e.py > -0.508653377