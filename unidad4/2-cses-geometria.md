---
layout: default
title: CSES Geometría
parent: 4. Problemas
nav_order: 2
has_children: true
---

# CSES Problem Set - Geometría

[CSES Problem Set](https://cses.fi/problemset/)

## Objetivo

En esta sección resuelvo los problemas de geometría del CSES Problem Set. Todas las soluciones están implementadas en **Python**. Los problemas básicos usan las herramientas de la página Geometría de la Unidad 3. Para cada problema, además del código, explico **cómo se resuelve** según los siguientes ejes:

- **Construcción del algoritmo:** los pasos de la solución, en orden.
- **Variables y tipos de datos:** qué variables se necesitan y de qué tipo (`int`, `float`, `bool`, `str`), y por qué.
- **Estructuras de datos:** qué estructuras se usan y qué ventaja tiene cada opción: listas, tuplas, diccionarios, conjuntos, colas (*queues*), montículos (*heaps*), grafos, matriz o lista de adyacencia (*adjacency matrix or list*, para representar un grafo). Por qué la elegida conviene para este problema, es decir, para qué sirve cada una en la solución.
- **Paradigma algorítmico:** la estrategia para resolver el problema (fuerza bruta, voraz, divide y vencerás, programación dinámica, búsqueda en grafos, etc.) y por qué esa estrategia sirve aquí.
- **Estilo de programación:** cómo se organiza el código (imperativo/procedural, orientado a objetos, funcional) y por qué conviene ese estilo.
- **Iterativo o recursivo:** cuál se usa y por qué (lo recursivo suele ser más fácil para grafos y árboles; lo iterativo usa menos memoria cuando hay muchos datos).
- **Complejidad:** complejidad temporal y espacial, y qué operación la determina.

## Problemas básicos

| # | Problema | Nombre | Herramienta | Explicación | Código |
| - | -------- | ------ | ----------- | ----------- | ------ |
| 1 | [Point Location Test](https://cses.fi/problemset/task/2189) | Ubicación de un punto | producto cruz (orientación) | | |
| 2 | [Line Segment Intersection](https://cses.fi/problemset/task/2190) | Cruce de segmentos | prueba de cruce | | |
| 3 | [Polygon Area](https://cses.fi/problemset/task/2191) | Área de un polígono | fórmula de la lazada | | |
| 4 | [Point in Polygon](https://cses.fi/problemset/task/2192) | Punto en un polígono | método del rayo | | |
| 5 | [Polygon Lattice Points](https://cses.fi/problemset/task/2193) | Puntos enteros de un polígono | fórmula de la lazada y MCD | | |
| 6 | [Minimum Euclidean Distance](https://cses.fi/problemset/task/2194) | Distancia mínima | pareja de puntos más cercanos | | |
| 7 | [Convex Hull](https://cses.fi/problemset/task/2195) | Envolvente convexa | orientación | | |

## Problemas avanzados

| # | Problema | Nombre | Explicación | Código |
| - | -------- | ------ | ----------- | ------ |
| 8 | [Maximum Manhattan Distances](https://cses.fi/problemset/task/3410) | Distancias Manhattan máximas | | |
| 9 | [All Manhattan Distances](https://cses.fi/problemset/task/3411) | Suma de todas las distancias Manhattan | | |
| 10 | [Intersection Points](https://cses.fi/problemset/task/1740) | Puntos de intersección | | |
| 11 | [Line Segments Trace I](https://cses.fi/problemset/task/3427) | Trazo de segmentos I | | |
| 12 | [Line Segments Trace II](https://cses.fi/problemset/task/3428) | Trazo de segmentos II | | |
| 13 | [Lines and Queries I](https://cses.fi/problemset/task/3429) | Rectas y consultas I | | |
| 14 | [Lines and Queries II](https://cses.fi/problemset/task/3430) | Rectas y consultas II | | |
| 15 | [Area of Rectangles](https://cses.fi/problemset/task/1741) | Área de rectángulos | | |
| 16 | [Robot Path](https://cses.fi/problemset/task/1742) | Camino de un robot | | |
