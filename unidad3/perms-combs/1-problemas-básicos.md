---
layout: default
title: Problemas básicos
parent: Permutaciones y combinaciones
grandparent: 3. Matemáticas y algoritmos
nav_order: 1
---

# Problemas básicos

## Problema 1: contar
- **Tarea:** El programa recibe `n` (número de listas) y luego `n` listas, una por línea. Para cada lista, calcula el número de permutaciones posibles de sus elementos usando la fórmula `m!` (donde `m` es el número de elementos en una lista), de dos formas: a mano con un bucle y con la biblioteca estándar `math`, usando la función incorporada `math.factorial`. Imprime el conteo por cada lista.
- **Por qué:** Distingue entre calcular el tamaño de un problema y generar sus salidas. Muchas veces solo se necesita el conteo, como generar sería inviable (`20! ≈ 2.4 × 10¹⁸`). Además, construir el factorial a mano muestra el mecanismo, mientras que usar la biblioteca muestra cómo resolver el problema con una sola línea de código.

[Ver el código en Github](https://github.com/locessentials/python/blob/main/unidad3/perms-combs/prob1-1.py)

## Problema 2: La forma integrada
- **Tarea:** Dada una lista como `[1, 2, 3]`, usa `itertools.permutations()` de Python para imprimir los 6 arreglos. Luego, verifica que la longitud de la salida sea igual a 3! (que es 6).
- **Por qué:** Introduce la herramienta de biblioteca estándar y optimizada. Es lo que usarías en un entorno de producción real en lugar de escribirlo desde cero.

## Problema 3: La forma recursiva
- **Tarea:** Escribe una función `get_permutations(lst)` que genere todas las permutaciones *sin* usar `itertools`. Usa recursión. Toma un elemento de la lista, encuentra recursivamente las permutaciones de los elementos restantes, y luego pega el elemento elegido al frente de cada resultado.
- **Por qué:** Es una pregunta clásica de entrevista. Te obliga a entender la lógica interna de cómo se construyen las permutaciones y sirve como el "motor" detrás de las matemáticas.

## Problema 4: Método de inserción
- **Tarea:** Escribe una función `ins(lst, x)` que inserte un elemento `x` en cada posición posible de una lista `lst`. Luego úsala para escribir `insm(lst)` que genere permutaciones recursivamente insertando el primer elemento en cada posición de las permutaciones de los elementos restantes.
- **Por qué:** Refuerza la idea de que generar permutaciones consiste en tomar una solución más pequeña y expandirla.