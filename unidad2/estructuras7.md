---
layout: default
title: Montículos
parent: 2. Estructuras de datos
nav_order: 8
---

# Montículos (*heaps*)

Un montículo (*heap*) es una estructura de datos que siempre da primero el elemento más pequeño o el más grande, sin importar el orden en que se agregaron. Hay dos tipos: el montículo de mínimos da primero el más pequeño, y el montículo de máximos da primero el más grande. Se usa para hacer una cola de prioridad. 

## Cómo está ordenado

Un montículo de mínimos sigue un orden parcial: si se dibuja la lista como un árbol, cada elemento es más pequeño que sus hijos (o igual). 

La lista guarda el árbol por niveles, de izquierda a derecha: primero la raíz, luego sus dos hijos, luego los hijos de esos hijos, y así. Como cada elemento tiene dos hijos, los hijos llenan la lista de dos en dos, en el mismo orden que sus padres, y por eso, los hijos de la posición 0 están en las posiciones 1 y 2, y los de la posición 1, en 3 y 4. Cada padre tiene dos lugares para sus hijos, así que para encontrarlos se multiplica la posición del padre (no su valor) por 2. Como la raíz está en la posición 0, los hijos empiezan a contarse desde la 1, y por eso se suma 1 para el primer hijo o 2 para el segundo. Es decir, los hijos del elemento en la posición k están en las posiciones 2k + 1 y 2k + 2. 

No hay ninguna regla para el orden de los elementos de un mismo nivel. En el ejemplo de abajo, 8 va antes que 5 aunque es más grande. Por eso la lista no está ordenada, pero el más pequeño siempre está en la posición 0, y el resto sigue la regla del árbol, en la que cada padre es más pequeño que sus hijos.

```
lista:      [ 3,  8,  5, 24, 10, 20 ]
posición:     0   1   2   3   4   5

la misma lista como árbol:

               3
             /   \
           8       5
          / \     /
        24   10  20
```

## En Python

En Python el montículo no es un tipo aparte. Al contrario, es una lista normal, y el módulo `heapq` solo hace montículos de mínimos, con el elemento más pequeño en la posición 0.

- `heapq`: "heap queue", nombre del módulo de Python que tiene las funciones de montículos
- `heapq.heappush(heap, item)`: agrega el elemento `item` a la lista `heap` y deja el más pequeño en la posición 0
- `heapq.heappop(heap)`: saca de la lista `heap` el elemento más pequeño, lo devuelve y deja el siguiente más pequeño en la posición 0
- los elementos del montículo pueden ser números o tuplas; con tuplas, `heappush` y `heappop` comparan el primer número para decidir cuál es el más pequeño

### Qué hacen `heappop` y `heappush` paso a paso

Cada vez que se agrega o se saca un elemento del montículo, la lista deja de cumplir la regla del árbol por un momento. `heappush` y `heappop` reacomodan la lista moviendo un solo elemento hacia arriba o hacia abajo por una rama del árbol, sin reordenar toda la lista.

En el caso de `heappop`, el elemento que se mueve es el último de la lista, que pasa al frente y baja por el árbol hasta que se vuelve a cumplir la regla. Estos son los pasos con el ejemplo de arriba, después de sacar 3.

1. Pasa el último elemento, 20, al frente, para que la lista no quede con un hueco.
2. 20 es más grande que sus hijos, 8 y 5, así que cambia de lugar con el más pequeño de los dos, 5.
3. 20 queda en el lugar que tenía 5 y ya no tiene hijos, así que se detiene.

```
lista:      [ 5,  8, 20, 24, 10 ]

               5
             /   \
           8       20
          / \
        24   10
```

En el caso de `heappush`, el elemento que se mueve es el nuevo. Se agrega al final de la lista y sube por el árbol, cambiando de lugar con su padre mientras sea más pequeño que él. Estos son los pasos con la lista que quedó después de `heappop`, al agregar 4.

1. Agrega 4 al final de la lista, en la posición 5, así que su padre es 20.
2. 4 es más pequeño que 20, así que cambian de lugar.
3. Ahora el padre de 4 es 5, y como 4 también es más pequeño, cambian de lugar otra vez.
4. 4 llega a la posición 0 y ya no tiene padre, así que se detiene.

```
lista:      [ 4,  8,  5, 24, 10, 20 ]

               4
             /   \
           8       5
          / \     /
        24   10  20
```