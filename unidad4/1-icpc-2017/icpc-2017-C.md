---
layout: default
title: Problem C
grandparent: 4. Problemas
parent: ICPC 2017
nav_order: 3
---

# ICPC 2017 - Problem C: emparejamiento bipartito

Tenemos una **cuadrícula** (grid) de r renglones y c columnas, y en cada posición hay una pila de cajas de cierta altura (puede ser 0). Desde el frente se ve la altura máxima de cada columna, desde el lado se ve la altura máxima de cada renglón y desde arriba se ve qué posiciones tienen cajas y cuáles están vacías. 

Dadas las dimensiones de la cuadrícula y la altura de cada posición, hay que encontrar el mayor número de cajas que se pueden quitar sin que cambie ninguna de las tres vistas: cada renglón y cada columna deben conservar su altura máxima, las posiciones vacías deben seguir vacías y las que tienen cajas deben seguir teniendo al menos una.

## Pasos a seguir

1. Sumar todas las cajas (el total original).
2. Encontrar la altura máxima de cada renglón y de cada columna.
3. Contar las posiciones distintas de cero. Cada una conserva al menos 1 caja; los ceros se quedan en 0.
4. Optimización (emparejamiento bipartito): buscar los cruces donde un renglón y una columna necesitan la misma altura máxima y la celda no es 0. Emparejar la mayor cantidad posible, usando cada renglón y cada columna una sola vez. Cada pareja comparte una sola pila alta, así que nos ahorramos una pila (altura − 1 cajas).
5. Cálculo final: darle a cada renglón y a cada columna su propia pila a su altura máxima (altura − 1, porque la caja de abajo ya se contó en el paso 3) y restar el ahorro de las parejas del paso 4. Lo que queda son las cajas mínimas necesarias.
6. Restar las cajas mínimas del total original.

robadas = total − (cajas mínimas para que las tres vistas se vean igual)

## Emparejamiento bipartito

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

*Cámara superior*

|       | col0 | col1 | col2 | col3 | col4 | lado |
|-------|------|------|------|------|------|------|
| row 0 |  1   |  1   |  0   |  1   |  1   |  5   |
| row 1 |  1   |  1   |  1   |  0   |  1   |  2   |
| row 2 |  0   |  1   |  1   |  1   |  1   |  4   |
| row 3 |  0   |  1   |  0   |  1   |  1   |  3   |
| row 4 |  1   |  1   |  1   |  1   |  1   |  2   |
| frente |  2   |  4   |  3   |  5   |  4   |      |






