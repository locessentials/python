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

## Input / Entrada

The input starts with a line containing an integer n (3 ≤ n ≤ 200) specifying the number of vertices of the polygon. This is followed by n lines, each containing two integers x and y (|x|, |y| ≤ 10⁶
) that give the coordinates (x, y) of the vertices of the polygon in counter-clockwise order. The polygon is simple, i.e., its vertices are distinct and no two edges of the polygon intersect or touch, except that consecutive edges touch at their common vertex. In addition, no two consecutive edges are collinear.

## Output / Salida

Display the length of the longest straight line segment that fits inside the polygon, with an absolute or relative error of at most 10⁻⁶.

## Glosario

| ENG | ESP | Definición |
| --- | --- | ---------- |
| polygon | polígono | figura plana cerrada formada por segmentos de recta |
| vertex, vertices | vértice, vértices | punto donde se unen dos lados consecutivos |
| collinear | colineal(es) | que están sobre la misma recta |
| edge | lado | segmento que une dos vértices consecutivos |
| simple polygon | polígono simple | polígono cuyos lados no se cruzan ni se tocan, salvo en vértices consecutivos |
| counter-clockwise | sentido antihorario | contrario al giro de las manecillas del reloj |
| coordinates | coordenadas | par (x, y) que ubica un punto en el plano |
| intersect | intersecarse / cortarse | cruzarse en al menos un punto |
| absolute value (\|x\|) | valor absoluto | Distancia de un número al cero, sin importar su signo. Ej.: \|−5\| = 5 y \|5\| = 5. |
| convex | convexo | sin entrantes; todos sus vértices apuntan hacia afuera |
| not convex | no convexo | tiene al menos un entrante (un vértice que apunta hacia adentro) |

## Conceptos de la geometría




