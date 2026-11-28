---
layout: default
title: Cambio de monedas
parent: 4. Problemas
nav_order: 3
has_children: true
---

# Cambio de monedas

## Objetivo

Esta sección reúne problemas de **cambio de monedas** (de *coin change* en inglés) para practicar programación dinámica. Cada problema se aborda con dos enfoques: **memoización** (recursión con caché, de arriba hacia abajo) y **tabulación** (iteración con tabla, de abajo hacia arriba), junto con su análisis y explicación.

## Problemas

| # | Problema | Variante / Enfoque | Memoización | Tabulación | Explicación |
| - | -------- | ------------------ | :---------: | :--------: | :---------: |
| 1 | Mínimo número de monedas | Minimizar cantidad de monedas (suministro ilimitado) | | | |
| 2 | The Coin Change Problem (HackerRank) | Número de formas / combinaciones (suministro ilimitado, sin importar el orden) | | | |
| 3 | DP: Coin Change (HackerRank) | Número de formas / combinaciones (práctica extra con ejemplo detallado) | | | |
| 4 | Número de permutaciones (formas ordenadas) | Contar secuencias donde el orden sí importa (1 + 2 ≠ 2 + 1) | | | |
| 5 | Monedas limitadas | Cantidad limitada por moneda (o uso restringido) | | | |
| 6 | Reconstruir las monedas usadas | Recuperar qué monedas forman la solución (camino / elección) | | | |

---

## Conceptos claves: repaso

### Recursión y programación dinámica

- **Recursión:** es una técnica de programación en la que una función se llama a sí misma para resolver instancias más pequeñas del problema. Se puede usar recursión sin programación dinámica (por ejemplo, recursión pura sin guardar resultados) y se puede hacer programación dinámica sin recursión (mediante ciclos y arreglos).
- **Programación dinámica:** es una estrategia de diseño de algoritmos para problemas que tienen **subproblemas superpuestos** y **subestructura óptima**. Su idea central es evitar recalcular el mismo subproblema una y otra vez.

Cuando una solución recursiva repite los mismos estados muchas veces, el número de llamadas puede crecer de forma exponencial. Ahí es donde entra la programación dinámica: guarda los resultados de los subproblemas para reutilizarlos y así disminuye la complejidad.

### Memoización (enfoque descendente / *top-down*)

La **memoización** suele aplicarse como un enfoque descendente (top-down) basado en recursión para evitar volver a calcular los mismos subproblemas. Al resolver un estado, se reutiliza su resultado si ya fue calculado (por ejemplo, mediante una estructura propia como una lista o diccionario, o una caché del lenguaje), en vez de repetir las mismas llamadas una y otra vez.

- Si la función vuelve a necesitar ese mismo estado, **lee el valor guardado** en lugar de volver a ramificarse.
- Suele sentirse más cercana al enunciado recursivo del problema.
- Hay que cuidar la profundidad de la pila de llamadas (*call stack*) y el tamaño del caché en entradas grandes.

### Tabulación (enfoque ascendente / *bottom-up*)

La **tabulación** resuelve el problema de forma iterativa (usando ciclos `for` o `while`) llenando una tabla (`dp`) desde los **casos base** hacia el estado objetivo.

- En lugar de "preguntar" hacia abajo con llamadas recursivas, se construyen primero las respuestas pequeñas (por ejemplo, monto `0`) y se avanza paso a paso hasta el monto deseado.
- Evita la sobrecarga de llamadas recursivas y suele facilitar el control de memoria (incluyendo optimizaciones de espacio cuando solo se necesita una fila o un arreglo 1D).