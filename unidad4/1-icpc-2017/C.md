---
layout: default
title: Problema C
grandparent: 4. Problemas
parent: ICPC 2017
nav_order: 3
---

# ICPC 2017 - Problema C: emparejamiento bipartito

Tenemos una **cuadrícula** (*grid*) de r renglones y c columnas, y en cada posición hay una pila de cajas de cierta altura (puede ser 0). Desde el frente se ve la altura máxima de cada columna, desde el lado se ve la altura máxima de cada renglón y desde arriba se ve qué posiciones tienen cajas y cuáles están vacías.

Dadas las dimensiones de la cuadrícula y la altura de cada posición, hay que encontrar el mayor número de cajas que se pueden quitar sin que cambie ninguna de las tres vistas: cada renglón y cada columna deben conservar su altura máxima, las posiciones vacías deben seguir vacías y las que tienen cajas deben seguir teniendo al menos una.

## Ilustración de la entrada de ejemplo 1

|       | col0 | col1 | col2 | col3 | col4 | lado |
|-------|------|------|------|------|------|------|
| row 0 |  1   |  4   |  0   |  5   |  2   |  5   |
| row 1 |  2   |  1   |  2   |  0   |  1   |  2   |
| row 2 |  0   |  2   |  3   |  4   |  4   |  4   |
| row 3 |  0   |  3   |  0   |  3   |  1   |  3   |
| row 4 |  1   |  2   |  2   |  1   |  1   |  2   |
| frente |  2   |  4   |  3   |  5   |  4   |      |

frente = cámara frontal; lee la altura máxima de cada columna  
lado = cámara lateral; lee la altura máxima de cada renglón

**Cámara superior**

|       | col0 | col1 | col2 | col3 | col4 | lado |
|-------|------|------|------|------|------|------|
| row 0 |  1   |  1   |  0   |  1   |  1   |  5   |
| row 1 |  1   |  1   |  1   |  0   |  1   |  2   |
| row 2 |  0   |  1   |  1   |  1   |  1   |  4   |
| row 3 |  0   |  1   |  0   |  1   |  1   |  3   |
| row 4 |  1   |  1   |  1   |  1   |  1   |  2   |
| frente |  2   |  4   |  3   |  5   |  4   |      |

## Conceptos claves
Hay que dejar 1 caja en cada posición distinta de 0, una posición con el máximo en cada renglón y una posición con el máximo en cada columna. Si un renglón y una columna tienen el mismo máximo h y la posición donde se cruzan es distinta de 0, una sola posición sirve para los dos, y se ahorran h − 1 cajas.

**Definiciones**
- **[grafo bipartito](https://es.wikipedia.org/wiki/Grafo_bipartito) (*bipartite graph*):** grafo cuyos vértices (o nodos) se dividen en dos conjuntos disjuntos, de modo que cada arista (*edge*) une un vértice de un conjunto con un vértice del otro
- **emparejamiento (*matching*):** conjunto de aristas que no comparten vértices; es decir, cada vértice queda con una sola pareja o sin pareja
- **emparejamiento máximo:** emparejamiento con el mayor número posible de aristas

**Aplicación al problema**
- Vértices: los renglones (un conjunto) y las columnas (el otro)
- Arista entre el renglón i y la columna j: si tienen el mismo máximo y `rows[i][j] > 0`
- Cada arista del emparejamiento es una posición compartida:

|       | col0 | col1 | col2 | col3 | col4 | lado |
|-------|------|------|------|------|------|------|
| row 0 |  1   |  1   |  0   |  1   |  1   |  5   |
| row 1 |  1   |  1   |  1   |  0   |  1   |  2   |
| row 2 |  0   |  **4**   |  1   |  1   |  1   |  4   |
| row 3 |  0   |  1   |  0   |  1   |  1   |  3   |
| row 4 |  1   |  1   |  1   |  1   |  1   |  2   |
| frente |  2   |  4   |  3   |  5   |  4   |      |


La celda **[4]** es una posición compartida. El renglón 2 y la columna 1 tienen máximo 4, así que una sola pila de 4 en esa celda cuenta como la más alta de las dos a la vez.

## Implementación

### 1. Preparación: organizar las entradas
- `rows`: la cuadrícula, una lista de listas
- `total`: la suma de todas las cajas
- `max_rows` y `max_columns`: el máximo de cada renglón y de cada columna
- `not_zero`: cuántas posiciones son distintas de 0; cada una se queda con mínimo 1 caja

### 2. Emparejamiento: encontrar las posiciones máximas compartidas
- `match_col`: una hoja de registro con un lugar por columna, que guarda qué renglón usa esa columna; -1 quiere decir que está libre
- `try_match(i, seen)`: busca pareja para el renglón `i`, revisando cada columna:
  1. `can_share` es `True` si el renglón y la columna tienen el mismo máximo **y** la posición donde se cruzan es distinta de 0
  2. Si la columna está libre, el renglón la toma y regresa `True`
  3. Si está ocupada, la **llamada recursiva** `try_match(match_col[j], seen)` le pregunta al renglón que la usa si se puede cambiar a otra columna. Si se cambia, regresa `True` y el renglón `i` toma la columna. Si no, se prueba la siguiente columna
  4. Si ninguna columna funciona, regresa `False`
- `seen`: marca las columnas ya revisadas en la búsqueda de un renglón, para que dos renglones no se pidan intercambiar hasta infinito
- `counted_twice`: un ciclo llama a `try_match` una vez por renglón; si encuentra pareja, suma `máximo − 1` cajas

**¿Por qué se necesita la llamada recursiva?** Con la entrada `2 7 4 / 7 0 1`, row 0 puede usar col 0 o col 1, y row 1 solo col 0. Si row 0 toma col 0 primero, row 1 se queda sin pareja. La llamada recursiva le pide a row 0 que se cambie a col 1, y así los dos tienen pareja.

|       | col 0 | col 1 | col 2 |
|-------|-------|-------|-------|
| row 0 | 2     | 7     | 4     |
| row 1 | 7     | 0     | 1     |


```
max_rows    = [7, 7]
max_columns = [7, 7, 4]
match_col   = [-1, -1, -1] (empty)

# Row 0 (i = 0)
seen = [False, False, False]
call try_match(0, seen)
  j = 0
  can_share = (7 == 7) and (2 > 0) = True
  seen[0] = True
  match_col[0] == -1?        yes
  match_col[0] = 0           column 0 is used by row 0
                             match_col is now [0, -1, -1]
  return True
```

El renglón 0 tomó la columna 0 solo porque fue la primera que funcionó. Pero el renglón 0 también podría usar la columna 1, y el renglón 1 solo puede usar la columna 0 (su posición en la columna 1 es 0).

```
# Row 1 (i = 1)
seen = [False, False, False]
call try_match(1, seen)
  j = 0
  can_share = (7 == 7) and (7 > 0) = True
  seen[0] = True             seen is now [True, False, False]
  match_col[0] == -1?        no, row 0 is using it
  so ask row 0 to move: try_match(0, seen)

      --- new call, for row 0 ---
      j = 0
      seen[0] is True, so skip column 0
      j = 1
      can_share = (7 == 7) and (7 > 0) = True
      seen[1] = True
      match_col[1] == -1?    yes
      match_col[1] = 0       column 1 is used by row 0
                             match_col is now [0, 0, -1]
      return True
      --- back to row 1's call ---

  row 0 moved, so the "or" is True
  match_col[0] = 1           column 0 is used by row 1
                             match_col is now [1, 0, -1]
  return True
```

### 3. Cálculo final
- `row_crates` y `column_crates`: las cajas que necesita la posición con el máximo de cada renglón y de cada columna, menos la caja ya contada en `not_zero`
- `left = not_zero + row_crates + column_crates − counted_twice`: las cajas que quedan
- `total − left`: las cajas robadas (9 en el ejemplo 1, 30 en el ejemplo 2)

## Análisis
- **Variables y tipos de datos:** todo es `int` (alturas, conteos, números de renglón y columna), porque se cuentan cajas enteras; `can_share` y los valores de `seen` son `bool`
- **Estructuras de datos:** una lista de listas para la cuadrícula; listas para los máximos; la lista `match_col` como hoja de registro; la lista `seen` de `bool`. El grafo bipartito no se guarda: las conexiones se revisan con `can_share` cuando hacen falta
- **Paradigma algorítmico:** búsqueda en grafos: emparejamiento bipartito máximo con el **algoritmo de Kuhn**, que busca pareja para cada renglón con búsqueda en profundidad (*DFS*). La cadena de cambios que hace la llamada recursiva se llama **camino de aumento**, una cadena de cambios donde cada fila ocupada se mueve a otra columna para dejar espacio; al final, una fila que no tenía pareja consigue una, y hay una pareja más que antes
- **Estilo de programación:** procedural, con una función `try_match`. Iterativo en la preparación y el cálculo final; recursivo en el emparejamiento, porque cada cambio puede provocar otro y no se sabe de antemano cuántos. La recursión termina porque regresa `True` al encontrar una columna libre o `False` al revisar todas, y `seen` evita revisar la misma columna dos veces

## Extensión del problema

Este problema deja algo por resolver. Encontramos cuántas cajas se pueden quitar, pero nunca cuántas hay que dejar en cada posición. Sin esa información, no podemos crear la cuadrícula resultante.

Para extender el problema, el programa puede imprimir también un mapa con el número exacto de cajas que se necesitan en cada posición de la cuadrícula.

En el código de solución, hay una sección al final que imprime este mapa.

[Ver el código completo en GitHub](https://github.com/locessentials/python/blob/main/unidad4/1-icpc-2017/c.py)