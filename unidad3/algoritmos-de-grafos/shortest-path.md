---
layout: default
title: Ruta más corta
parent: Algoritmos de grafos
grandparent: 3. Matemáticas y algoritmos
nav_order: 4
---

# Ruta más corta desde un origen, con pesos no negativos (algoritmo de Dijkstra)

Los algoritmos de la ruta más corta (*shortest path*) encuentran en un grafo con pesos la ruta de menor costo entre dos nodos o desde un nodo de inicio hasta todos los demás. El costo de una ruta es la suma de los pesos de sus aristas, y esos pesos pueden representar distancia, tiempo, dinero o cualquier otra cantidad que se quiera minimizar. Algunos ejemplos de su uso son las aplicaciones de mapas que buscan la ruta más rápida, el enrutamiento de datos por los routers en internet y la búsqueda de los vuelos más baratos, aunque tengan más escalas.

## Concepto clave: relajar aristas (Edge Relaxation)

En el algoritmo de Dijkstra, mantenemos una lista con el **costo acumulado mínimo conocido** para ir desde el nodo de origen hasta cada uno de los demás nodos. Al inicio, como no conocemos ninguna ruta, estos costos se consideran infinitos, y para encontrar la ruta más corta, evaluamos constantemente las aristas entre nodos. 

**Relajar una arista** entre un nodo A y un nodo B consiste en hacer una comparación muy simple:

1. Calculamos cuánto costaría llegar a B desde el origen pasando por A:

`new_cost = costs[A] + weight(A, B)`

2. **Comparación**: Si este `new_cost` es menor que el **costo mínimo conocido hasta ahora para llegar a B desde el origen** (que está guardado en `costs[B]`), actualizamos `costs[B]` con este nuevo valor más bajo. Es decir, sustituimos la mejor ruta conocida hacia B por una ruta mejor que pasa por A.

En resumen: relajar una arista es simplemente **actualizar la distancia a un nodo destino si encontramos una ruta más corta a través de un nodo vecino**.

## Explicación del programa

Esta sección sigue un programa que calcula las rutas más cortas paso a paso con un ejemplo, para mostrar cómo cambian `heap`, `costs` y `previous` hasta encontrar la ruta más corta a cada nodo. Usaremos este grafo, con el **nodo 1** como **nodo de inicio**.

```markdown
   (1)--24---(2)
    |  \     |
 20 |   \ 3  | 5
    |    \   |
   (4)----\--(3)
       12      
```

La entrada de prueba del programa describe el mismo grafo. El primer renglón da el número de nodos y el número de aristas, cada renglón siguiente da una arista con sus dos nodos y su peso, y el último renglón da el nodo de inicio.

```markdown
4 5
1 2 24
1 4 20
3 1 3
4 3 12
2 3 5
1
```

### Organización de los datos de entrada

El programa importa `heapq`, la implementación de montículos de la biblioteca estándar de Python. La usaremos más adelante para extraer siempre el nodo con el menor costo acumulado; si quieres repasar cómo funcionan los montículos, consulta Estructuras de datos > Montículos.

Los datos se guardan en un diccionario llamado `graph`, que representa el grafo como una **lista de adyacencia**: cada nodo es una clave, y su valor es la lista de sus vecinos junto con el peso de la arista que los une. Las aristas se agregan **en ambos sentidos**, porque el grafo no es dirigido: si el nodo 1 se conecta con el 2, el 3 y el 4, entonces el 4 también se conecta con el 1, y lo mismo el 3 y el 2.

Para el grafo de ejemplo, el diccionario resultante es:

{
    1: [(2, 24), (4, 20), (3, 3)],
    2: [(1, 24), (3, 5)],
    3: [(1, 3), (4, 12), (2, 5)],
    4: [(1, 20), (3, 12)],
}

Cada tupla es `(vecino, peso)`. Por ejemplo, `graph[1]` contiene `(2, 24)` porque hay una arista de 1 a 2 con peso 24, y `graph[2]` contiene `(1, 24)` por esa misma arista vista desde el otro lado.

Como se mencionó, esta sección explica un programa que calcula las rutas más cortas desde un nodo de inicio. el código que acompaña a la explicación está disponible aquí:

[https://github.com/locessentials/python/blob/main/unidad3/algoritmos-de-grafo/shortest-path.py](https://github.com/locessentials/python/blob/main/unidad3/algoritmos-de-grafo/shortest-path.py)

### Cálculo de los costos

El programa no calcula todos los costos de golpe: va descubriendo rutas y mejorándolas. Para eso usa tres estructuras:

- `costs`: el mejor costo conocido hasta ahora para llegar a cada nodo desde el origen.
- `heap`: los pares `(costo, nodo)` que todavía hay que revisar, ordenados por costo.
- `previous`: de qué nodo venimos en la mejor ruta conocida a cada nodo.

**Estado inicial.** Todos los nodos empiezan en infinito porque aún no conocemos ninguna ruta. El nodo de inicio cuesta 0 llegar a sí mismo, y es lo único que hay en el heap:

```python
costs = {1: 0, 2: inf, 3: inf, 4: inf}
heap = [(0, 1)]
previous = {}
```

**Primera vuelta del `while`.** Se extrae `(0, 1)` de `heap` (que solo contiene `(0, 1)`): costo actual 0, nodo actual 1. Como `0` no es mayor que `costs[1]` (que es 0), seguimos al `for`. c

Con el vecino 2: `new_cost = 0 + 24 = 24`. Como `24 < inf`, se actualiza `costs[2] = 24`, `previous[2] = 1`, y se mete `(24, 2)` al heap.

Con el vecino 4: `new_cost = 0 + 20 = 20`. Como `20 < inf`, se actualiza `costs[4] = 20`, `previous[4] = 1`, y se mete `(20, 4)` al heap.

Con el vecino 3: `new_cost = 0 + 3 = 3`. Como `3 < inf`, se actualiza `costs[3] = 3`, `previous[3] = 1`, y se mete `(3, 3)` al heap.

Al terminar el `for`:

```python
costs = {1: 0, 2: 24, 3: 3, 4: 20}
heap = [(3, 3), (20, 4), (24, 2)]
previous = {2: 1, 3: 1, 4: 1}
```

**Segunda vuelta.** Se extrae `(3, 3)`. Los vecinos de 3 son `(1, 3)`, `(4, 12)` y `(2, 5)`.

Con el vecino 1: `new_cost = 3 + 3 = 6`. Como `6 < 0` es falso, no se hace nada.

Con el vecino 4: `new_cost = 3 + 12 = 15`. Como `15 < 20`, se actualiza `costs[4] = 15`, `previous[4] = 3`, y se mete `(15, 4)` al heap.

Con el vecino 2: `new_cost = 3 + 5 = 8`. Como `8 < 24`, se actualiza `costs[2] = 8`, `previous[2] = 3`, y se mete `(8, 2)` al heap.

```python
costs = {1: 0, 2: 8, 3: 3, 4: 15}
heap = [(8, 2), (15, 4), (20, 4), (24, 2)]
previous = {2: 3, 3: 1, 4: 3}
```

Fíjate que `heap` ahora tiene pares viejos: `(20, 4)` y `(24, 2)`, que ya no representan la mejor ruta conocida. Esos se descartan más adelante con la condición `current_cost > costs[current_node]`.

**Tercera vuelta.** Se extrae `(8, 2)`. Los vecinos de 2 son `(1, 24)` y `(3, 5)`.

Con el vecino 1: `new_cost = 8 + 24 = 32`. Como `32 < 0` es falso, no se hace nada.

Con el vecino 3: `new_cost = 8 + 5 = 13`. Como `13 < 3` es falso, no se hace nada.

```python
costs = {1: 0, 2: 8, 3: 3, 4: 15}
heap = [(15, 4), (20, 4), (24, 2)]
previous = {2: 3, 3: 1, 4: 3}
```

**Cuarta vuelta.** Se extrae `(15, 4)`. Los vecinos de 4 son `(1, 20)` y `(3, 12)`.

Con el vecino 1: `new_cost = 15 + 20 = 35`. Como `35 < 0` es falso, no se hace nada.

Con el vecino 3: `new_cost = 15 + 12 = 27`. Como `27 < 3` es falso, no se hace nada.

```python
costs = {1: 0, 2: 8, 3: 3, 4: 15}
heap = [(20, 4), (24, 2)]
previous = {2: 3, 3: 1, 4: 3}
```

**Quinta vuelta.** Se extrae `(20, 4)`. Pero `costs[4]` es 15, y `20 > 15`, así que el par es viejo y se descarta con `continue`. No se toca nada más.

```python
heap = [(24, 2)]
```

**Sexta vuelta.** Se extrae `(24, 2)`. `costs[2]` es 8, y `24 > 8`, así que también se descarta.

```python
heap = []
```

El `while` termina porque el heap está vacío. Los costos finales son `{1: 0, 2: 8, 3: 3, 4: 15}`.

### Impresión de los resultados

Terminado el `while`, `costs` ya tiene el menor costo desde el inicio hasta cada nodo, y `previous` dice de qué nodo se llegó en cada caso. Falta reconstruir e imprimir las rutas.

El programa recorre cada nodo con un `for`. Si el costo guardado para ese nodo sigue en infinito, significa que no hay ruta desde el inicio, así que se imprime "No path".

En caso contrario, se empieza a construir la ruta. `path` arranca como una lista con el nodo destino, y `current_node` se copia también como ese nodo, pero como un cursor que se va a mover hacia atrás. Mientras `current_node` no sea el nodo de inicio, se busca en `previous` el nodo del que se llegó a `current_node` y se agrega a `path`. El `while` repite esto hasta llegar al inicio, y ahí se detiene: el inicio ya quedó en `path` en la última vuelta, así que no se agrega dos veces.

Como la ruta se armó de atrás hacia adelante, se invierte con `reverse()` para que vaya del inicio al destino, y se imprime el destino, su costo y la ruta.

Para el grafo de ejemplo, la salida es:

```python
Destination: 1 Cost: 0 Path: [1]
Destination: 2 Cost: 8 Path: [1, 3, 2]
Destination: 3 Cost: 3 Path: [1, 3]
Destination: 4 Cost: 15 Path: [1, 3, 4]
```

Nota que la ruta al nodo 2 es `[1, 3, 2]`, no la arista directa 1–2 de peso 24, sino la de 1–3–2 de peso 8, que es la más barata que encontró el cálculo de costos.

## Análisis del código

- **Construcción del algoritmo:**
  1. Leer los nodos, las aristas y el nodo de inicio, y guardar el grafo como una lista de adyacencia.
  2. Calcular el menor costo desde el inicio hasta cada nodo con el algoritmo de Dijkstra, usando un montículo para extraer siempre el nodo de menor costo acumulado.
  3. Reconstruir e imprimir la ruta más corta a cada nodo siguiendo el diccionario `previous`.

- **Variables y tipos de datos:**
  - `int`: los nodos, los pesos de las aristas y las posiciones en listas. Los pesos son enteros, así que las sumas de costos son exactas.
  - `float`: solo `float("inf")`, que se usa como costo inicial para los nodos que aún no tienen ruta conocida.
  - `bool`: no se usa explícitamente, pero las comparaciones como `new_cost < costs[neighbor]` producen valores booleanos que controlan el flujo.

- **Estructuras de datos:**
  - Diccionario `graph`: lista de adyacencia; cada nodo es una clave y su valor es la lista de tuplas `(vecino, peso)`.
  - Diccionario `costs`: el mejor costo conocido hasta ahora para llegar a cada nodo desde el origen.
  - Diccionario `previous`: de qué nodo se llegó a cada nodo en la mejor ruta conocida.
  - Montículo `heap`: pares `(costo, nodo)` ordenados por costo; permite extraer siempre el más barato con `heappop` e insertar con `heappush`.
  - Lista `path`: la ruta reconstruida, que se arma al revés y se invierte al final.

- **Paradigma algorítmico:** algoritmo de Dijkstra, un método voraz. En cada paso se extrae del montículo el nodo con el menor costo acumulado y se relajan sus aristas, es decir, se actualiza el costo de un vecino si se encuentra una ruta más barata a través del nodo actual. Funciona con pesos no negativos.

- **Estilo de programación:** imperativo/procedural, con un ciclo principal `while` y un `for` interno. No se usan funciones propias; todo el cálculo vive en el ciclo.

- **Iterativo o recursivo:** iterativo. Todo se hace con `while` y `for`. No hay llamadas recursivas, y lo iterativo usa menos memoria.

- **Complejidad:**
  - Temporal: cada arista se relaja a lo más una vez por cada vez que su nodo de origen sale del montículo con el costo óptimo, y cada operación del montículo cuesta O(log V). En total, O((V + E) log V), donde V es el número de nodos y E el de aristas.
  - Espacial: O(V + E). Se guardan `graph` (E entradas repartidas en V listas), `costs` y `previous` (V entradas cada uno) y `heap` (hasta O(E) pares).

[Ver el código en GitHub](https://github.com/locessentials/python/blob/main/unidad3/algoritmos-de-grafo/shortest-path.py)