---
layout: default
title: Grafos
parent: 2. Estructuras de datos
nav_order: 9
---

# Grafos

Un grafo representa entidades y las relaciones entre pares de ellas. Las entidades se llaman **nodos** (o vértices) y las relaciones se llaman **aristas**. Sirve para modelar muchas cosas: personas y amistades, computadoras y cables, ciudades y carreteras.

---

## Conceptos básicos de grafos

### Definición

Un grafo G = (V, E) tiene dos conjuntos:

- **V:** el conjunto de nodos
- **E:** el conjunto de aristas; cada arista une un par de nodos
- **n:** el número de nodos
- **m:** el número de aristas

Este es el grafo de ejemplo que se usa en toda la página. Tiene n = 8 nodos y m = 11 aristas:

```
         1     7
        / \   /|
       /   \ / |
      2-----3  |
     / \   / \ |
    /   \ /   \|
   4-----5     8
         |
         6
```

### Tipos de grafos

- **No dirigido:** la arista no tiene dirección; si 1 está unido con 2, también 2 está unido con 1
- **Dirigido:** la arista va en una sola dirección, de un nodo a otro
- **Con pesos:** cada arista tiene un número (costo, distancia, tiempo); se usa para buscar caminos más cortos
- **Simple:** no dirigido, sin aristas de un nodo a sí mismo y sin aristas repetidas
- **Multigrafo:** puede tener dos o más aristas entre el mismo par de nodos; por ejemplo, dos carreteras distintas entre las mismas dos ciudades

```
no dirigido        dirigido           con pesos         simple        multigrafo

  1-----2          1---->2          1----(5)----2       1-----2       1-----2
                                     \         /         \   /         \___/
                                     (2)     (1)          \ /
                                       \     /             3
                                        \   /
                                         \ /
                                          3
```

### Vocabulario

Estos son los términos que aparecen en las descripciones de los problemas:

- **vecinos:** nodos que están a una arista de distancia; el conjunto de vecinos de un nodo se llama su vecindario; en el ejemplo, los vecinos de 5 son 2, 3, 4 y 6
- **camino:** sucesión de nodos en la que cada nodo tiene una arista con el siguiente; su longitud es el número de aristas; por ejemplo, 4 → 5 → 3 → 7 tiene longitud 3
- **distancia:** longitud del camino más corto entre dos nodos, contada en aristas (saltos); en el ejemplo, la distancia de 4 a 7 es 3; si no hay camino, no hay distancia (se dice que es infinita)
- **ciclo:** camino de al menos tres nodos que empieza y termina en el mismo nodo, sin repetir ningún otro nodo; por ejemplo, 2 → 3 → 5 → 2
- **grafo conectado:** grafo en que hay un camino entre cada par de nodos
- **componente conectada:** grupo de nodos donde hay un camino entre cada par, y no hay ninguna arista entre un nodo del grupo y un nodo de fuera; un grafo puede tener desde una componente (si está conectado) hasta n componentes (si no tiene aristas)
- **árbol:** un grafo conectado y sin ciclos; un árbol de n nodos siempre tiene n − 1 aristas
- **denso / disperso:** un grafo denso tiene muchas aristas, cerca del máximo; uno disperso tiene pocas

Si al grafo de ejemplo se le agregan los nodos 9 y 10, unidos solo entre ellos, el grafo deja de estar conectado y queda con dos componentes:

```
         1     7
        / \   /|
       /   \ / |     9
      2-----3  |     |
     / \   / \ |     10
    /   \ /   \|
   4-----5     8
         |
         6

componente 1: nodos 1 a 8
componente 2: nodos 9 y 10
```

### Número de aristas

En un grafo simple de n nodos, el número de aristas va de 0 a n(n − 1)/2:

- **Mínimo, 0:** solo hay nodos, sin aristas; cada nodo es su propia componente
- **Máximo, n(n − 1)/2:** cada nodo está unido con todos los demás (grafo completo); cada uno de los n nodos tiene n − 1 vecinos, y se divide entre 2 porque la arista 1–2 es la misma que la 2–1; con 8 nodos, el máximo es 8 × 7 / 2 = 28

El grafo de ejemplo tiene 11 de 28 aristas posibles.

---

## Cómo guardar un grafo

Hay dos formas de guardar un grafo en memoria. Las dos guardan la misma información; cambian la memoria que usan y el tiempo que tardan las operaciones.

### Matriz de adyacencia

Una tabla de n × n. En el renglón i, columna j, hay un 1 si hay una arista entre i y j, y un 0 si no. Como el grafo no es dirigido, la tabla es simétrica: si el renglón 2, columna 4 tiene un 1, el renglón 4, columna 2 también. En un grafo simple, la diagonal siempre tiene ceros, porque ningún nodo tiene arista consigo mismo.

```
     1  2  3  4  5  6  7  8
 1   0  1  1  0  0  0  0  0
 2   1  0  1  1  1  0  0  0
 3   1  1  0  0  1  0  1  1
 4   0  1  0  0  1  0  0  0
 5   0  1  1  1  0  1  0  0
 6   0  0  0  0  1  0  0  0
 7   0  0  1  0  0  0  0  1
 8   0  0  1  0  0  0  1  0
```

### Lista de adyacencia

Cada nodo tiene una lista de sus vecinos. Cada arista aparece dos veces, una en la lista de cada uno de sus nodos.

```
 1: 2, 3
 2: 1, 3, 4, 5
 3: 1, 2, 5, 7, 8
 4: 2, 5
 5: 2, 3, 4, 6
 6: 5
 7: 3, 8
 8: 3, 7
```

### Comparación

- **Memoria:** la matriz usa O(n²), aunque el grafo tenga pocas aristas; la lista usa O(n + m): crece con lo que sea más grande, los nodos o las aristas
- **¿Hay arista entre a y b?:** en la matriz es O(1), porque se lee una casilla; en la lista es O(n) en el peor caso, porque se recorren los vecinos de a, y un nodo puede tener hasta n − 1
- **Recorrer los vecinos de un nodo:** en la matriz es O(n), porque se revisa todo el renglón; en la lista es O(número de vecinos)

---

![Logo de Python en amarillo y rojo]({{ '/imagenes/python-logo.png' | relative_url }}){: .tip-circle }

En casi todos los problemas se usa la lista de adyacencia: los grafos de los problemas suelen ser dispersos, y los algoritmos como BFS y DFS recorren los vecinos de cada nodo. La matriz conviene cuando n es pequeño (unos cientos de nodos) y se pregunta muchas veces si existe una arista.

<span class="clear"></span>

---

## En Python

### Leer un grafo desde la entrada

En los problemas, el grafo casi siempre llega así: una línea con n y m, y después m líneas, cada una con los dos nodos de una arista. La lista de adyacencia se guarda en un diccionario: cada clave es un nodo y su valor es la lista de sus vecinos.

```python
# entrada:
# 8 11
# 1 2
# 1 3
# 2 3
# 2 4
# 2 5
# 3 5
# 3 7
# 3 8
# 4 5
# 5 6
# 7 8

n, m = map(int, input().split())

graph = {}                              # lista de adyacencia: nodo -> lista de vecinos
for node in range(1, n + 1):            # los nodos van del 1 al n
    graph[node] = []

for edge_number in range(m):
    node_a, node_b = map(int, input().split())
    graph[node_a].append(node_b)        # la arista se guarda en las dos direcciones,
    graph[node_b].append(node_a)        # porque el grafo no es dirigido

print(graph)
# {1: [2, 3], 2: [1, 3, 4, 5], 3: [1, 2, 5, 7, 8], 4: [2, 5],
#  5: [2, 3, 4, 6], 6: [5], 7: [3, 8], 8: [3, 7]}
```

Primero se crea una lista vacía para cada nodo, para que también aparezcan los nodos que no tienen ninguna arista.

En un grafo dirigido, cada arista se guarda en una sola dirección: solo `graph[node_a].append(node_b)`.

### Grafo con pesos

Si cada línea de aristas trae un tercer número, el peso, cada vecino se guarda como una tupla (vecino, peso):

```python
# una línea de aristas: 1 2 5   (arista entre 1 y 2 con peso 5)
node_a, node_b, weight = map(int, input().split())
graph[node_a].append((node_b, weight))
graph[node_b].append((node_a, weight))
```

### Matriz de adyacencia en Python

La matriz se guarda como una lista de listas. Se crean n + 1 renglones y n + 1 columnas para que los nodos 1 a n coincidan con sus índices; el renglón 0 y la columna 0 no se usan.

```python
matrix = []
for row_number in range(n + 1):
    matrix.append([0] * (n + 1))        # cada renglón es una lista nueva

for edge_number in range(m):
    node_a, node_b = map(int, input().split())
    matrix[node_a][node_b] = 1
    matrix[node_b][node_a] = 1
```

---

![Logo de Python en amarillo y rojo]({{ '/imagenes/python-logo.png' | relative_url }}){: .tip-circle }

No se puede crear la matriz con `[[0] * (n + 1)] * (n + 1)`: eso repite la misma lista en todos los renglones, y un cambio en un renglón aparece en todos. Es el mismo problema de `b = a` en "Copiar una lista" (Cheat Sheet 4: listas).

<span class="clear"></span>

---

### Operaciones comunes

```python
for neighbor in graph[5]:               # recorrer los vecinos del nodo 5
    print(neighbor)                     # 2 \n3 \n4 \n6

len(graph[5])                           # 4  (cuántos vecinos tiene el nodo 5)

3 in graph[5]                           # True  (¿hay arista entre 5 y 3?); O(número de vecinos)
matrix[5][3] == 1                       # True  (la misma pregunta con la matriz); O(1)
```

---

## Algoritmos

Los algoritmos que recorren un grafo (búsqueda por amplitud o BFS, búsqueda en profundidad o DFS, caminos más cortos) están en Algoritmos de grafos.

## Para leer más

- Luis E. Vargas Azcona, [*Problemas y Algoritmos*](https://omegaup.com/docs/assets/libroluisvargas.pdf), parte sobre grafos (libro de la Olimpiada Mexicana de Informática)