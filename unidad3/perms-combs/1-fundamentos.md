---
layout: default
title: Generate a Permutation
parent: Permutaciones y combinaciones
grandparent: 3. Matemáticas y algoritmos
nav_order: 1
---

# Fundamentos de implementación

Aquí tienes la lista de problemas en español, manteniendo el formato de Tarea y Por qué.

---

## Problema 1: contar
**Tarea:** El programa recibe `n` (número de listas) y luego `n` listas, una por línea. Para cada lista, calcula el número de permutaciones posibles de sus elementos usando la fórmula `m!` (donde `m` es el número de elementos en una lista), de dos formas: a mano con un bucle y con la biblioteca estándar `math`, usando la función incorporada `math.factorial`. Imprime el conteo por cada lista.
- **Por qué:** Distingue entre calcular el tamaño de un problema y generar sus salidas. Muchas veces solo se necesita el conteo, como generar sería inviable (`20! ≈ 2.4 × 10¹⁸`). Además, construir el factorial a mano muestra el mecanismo, mientras que usar la biblioteca muestra cómo resolver el problema con una sola línea de código.

[Ver el código en Github](https://github.com/locessentials/python/blob/main/unidad3/perms-combs/prob1-1.py.py)

## Problema 2: La forma integrada
- **Tarea:** Dada una lista como `[1, 2, 3]`, usa `itertools.permutations()` de Python para imprimir los 6 arreglos. Luego, verifica que la longitud de la salida sea igual a 3! (que es 6).
- **Por qué:** Introduce la herramienta de biblioteca estándar y optimizada. Es lo que usarías en un entorno de producción real en lugar de escribirlo desde cero.

## Problema 3: La forma recursiva
- **Tarea:** Escribe una función `get_permutations(lst)` que genere todas las permutaciones *sin* usar `itertools`. Usa recursión. Toma un elemento de la lista, encuentra recursivamente las permutaciones de los elementos restantes, y luego pega el elemento elegido al frente de cada resultado.
- **Por qué:** Es una pregunta clásica de entrevista. Te obliga a entender la lógica interna de cómo se construyen las permutaciones y sirve como el "motor" detrás de las matemáticas.

## Problema 4: Método de inserción
- **Tarea:** Escribe una función `ins(lst, x)` que inserte un elemento `x` en cada posición posible de una lista `lst`. Luego úsala para escribir `insm(lst)` que genere permutaciones recursivamente insertando el primer elemento en cada posición de las permutaciones de los elementos restantes.
- **Por qué:** Refuerza la idea de que generar permutaciones consiste en tomar una solución más pequeña y expandirla.

## Problema 5: Aplicar una permutación
- **Tarea:** Escribe una función `apply_permutation(perm, lst)` que tome una regla de permutación (como `[2, 3, 1]`) y la aplique a una lista de datos (como `['A', 'B', 'C']`). La función debe devolver la lista reordenada.
- **Por qué:** Traduce la notación de dos líneas de la pizarra en una herramienta práctica. Pasa de "generar" permutaciones a "usarlas" para transformar datos.

## Problema 6: Composición de permutaciones
- **Tarea:** Escribe una función `compose(p1, p2)` que tome dos permutaciones y devuelva la permutación compuesta resultante. Ejecútala con dos permutaciones diferentes y demuestra que `compose(p1, p2)` no es igual a `compose(p2, p1)`.
- **Por qué:** Demuestra directamente la propiedad de no conmutatividad (`σ ∘ τ ≠ τ ∘ σ`). Muestra que el orden importa al transformar datos.

## Problema 7: Paridad e inversiones
- **Tarea:** Escribe una función `is_even(perm)` que devuelva `True` si una permutación es par y `False` si es impar. Hazlo contando las "inversiones" (cuántos pares de números están fuera de orden) y verificando si esa cuenta es par o impar.
- **Por qué:** Conecta el código con la teoría de grupos más profunda. Es la forma algorítmica de determinar la paridad (signo) de una permutación sin tener que rastrear físicamente los intercambios.