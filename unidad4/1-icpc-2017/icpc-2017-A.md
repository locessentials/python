---
layout: default
title: Problem A
grandparent: 4. Problemas
parent: ICPC 2017
nav_order: 1
---

# ICPC 2017 - Problem A

## Resumen del problema

Dado un **polígono simple** de *n* vértices, en sentido antihorario, calcular la longitud del **segmento de recta más largo** que cabe dentro de él.

- El segmento **no puede salir** del polígono.
- El segmento **sí puede tocar** el borde o **correr a lo largo** de un lado.
- El polígono puede ser **no convexo**.

### Input / Entrada

The input starts with a line containing an integer n (3 ≤ n ≤ 200) specifying the number of vertices of the polygon. This is followed by n lines, each containing two integers x and y (|x|, |y| ≤ 10⁶
) that give the coordinates (x, y) of the vertices of the polygon in counter-clockwise order. The polygon is simple, i.e., its vertices are distinct and no two edges of the polygon intersect or touch, except that consecutive edges touch at their common vertex. In addition, no two consecutive edges are collinear.

### Output / Salida

Display the length of the longest straight line segment that fits inside the polygon, with an absolute or relative error of at most 10⁻⁶.

## Fórmulas y métodos para la resolución del problema

| ENG | ESP | Definición |
| --- | --- | ---------- |
| cross product | producto cruz | dados A = (x₁, y₁), B = (x₂, y₂) y P = (x₃, y₃): (x₂ − x₁)(y₃ − y₁) − (y₂ − y₁)(x₃ − x₁); positivo: de A a B y luego a P se gira en sentido antihorario; negativo: en sentido horario; cero: colineales |
| distance formula | fórmula de la distancia | distancia entre (x₁, y₁) y (x₂, y₂): d = √((x₂ − x₁)² + (y₂ − y₁)²) |
| parametric form | forma paramétrica | dados A = (x₁, y₁) y B = (x₂, y₂), cada punto de la recta es (x₁ + t(x₂ − x₁), y₁ + t(y₂ − y₁)); t = 0 en A, t = 1 en B |
| ray casting | método del rayo (regla par-impar) | para saber si un punto está dentro de un polígono, se traza un rayo desde él y se cuentan los lados que cruza; impar: dentro, par: fuera |

## Vocabulario adicional

| ENG | ESP | Definición |
| --- | --- | ---------- |
| absolute value (\|x\|) | valor absoluto | Distancia de un número al cero, sin importar su signo. Ej.: \|−5\| = 5 y \|5\| = 5. |
| collinear | colineal(es) | que están sobre la misma recta |
| coordinates | coordenadas | par (x, y) que ubica un punto en el plano |
| convex | convexo | sin entrantes; todos sus vértices apuntan hacia afuera |
| not convex | no convexo | tiene al menos un entrante (un vértice que apunta hacia adentro) |
| counter-clockwise | sentido antihorario | contrario al giro de las manecillas del reloj |
| edge | lado | segmento que une dos vértices consecutivos |
| intersect | intersecarse / cortarse | cruzarse en al menos un punto |
| polygon | polígono | figura plana cerrada formada por segmentos de recta |
| simple polygon | polígono simple | polígono cuyos lados no se cruzan ni se tocan, salvo en vértices consecutivos |
| vertex, vertices | vértice, vértices | punto donde se unen dos lados consecutivos |