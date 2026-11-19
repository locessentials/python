---
layout: default
title: Permutaciones como funciones
parent: Permutaciones y combinaciones
grandparent: 3. Matemáticas y algoritmos
nav_order: 2
---

# Permutaciones como funciones

Una permutación de `n` elementos se representa como una lista `p` donde `p[i]` indica a dónde se envía la posición `i` (empezando en 0). Vista así, una permutación es una función: se puede aplicar, componer con otras, descomponer en intercambios y asignarle un signo.

## Problema 1: Identidad y transposiciones
- **Tarea:** Escribe `identidad(n)`, que devuelva la permutación que no mueve nada (`[0, 1, ..., n-1]`), y `tr(i, j, I)`, que tome la identidad e intercambie las posiciones `i` y `j`. Por ejemplo, `tr(1, 3, I)` con `n = 5` da `[0, 3, 2, 1, 4]`.
- **Por qué:** Las transposiciones son las permutaciones más simples: solo intercambian dos elementos. Todas las demás se construyen a partir de ellas.

[Ver el código en Github](https://github.com/locessentials/python/blob/main/unidad3/perms-combs/prob2-1.py)

## Problema 2: Aplicar una permutación
- **Tarea:** Escribe una función `apply_permutation(perm, lst)` que tome una regla de permutación (como `[2, 3, 1]`) y la aplique a una lista de datos (como `['A', 'B', 'C']`). La función debe devolver la lista reordenada.
- **Por qué:** Traduce la notación de dos líneas de la pizarra en una herramienta práctica. Pasa de "generar" permutaciones a "usarlas" para transformar datos.

## Problema 3: Composición
- **Tarea:** Escribe `compose(a, b)`, que devuelva la lista con `b[a[i]]` en cada posición `i`: primero se aplica `a` y luego `b`. Escríbela de dos formas: en una línea con `lambda` y en versión larga con un bucle que nombre cada paso.
- **Por qué:** Componer es aplicar una permutación después de otra. La versión larga hace visible lo que la versión con `lambda` resume en una línea.

[Ver el código en Github](https://github.com/locessentials/python/blob/main/unidad3/perms-combs/prob2-3.py)

## Problema 4: El orden importa
- **Tarea:** Escribe una función `compose(p1, p2)` que tome dos permutaciones y devuelva la permutación compuesta resultante. Ejecútala con dos permutaciones diferentes y demuestra que `compose(p1, p2)` no es igual a `compose(p2, p1)`.
- **Por qué:** Demuestra directamente la propiedad de no conmutatividad (`σ ∘ τ ≠ τ ∘ σ`). Muestra que el orden importa al transformar datos.

## Problema 5: Descomposición en transposiciones
- **Tarea:** Escribe `trl(b)`, que ordene la lista intercambiando elementos vecinos que estén fuera de orden. Cada intercambio se guarda como una transposición `tr(i, i+1, I)`, y la función devuelve la lista de todas ellas.
- **Por qué:** Muestra que toda permutación se puede escribir como una sucesión de transposiciones de elementos vecinos.

[Ver el código en Github](https://github.com/locessentials/python/blob/main/unidad3/perms-combs/prob2-5.py)

## Problema 6: Signo de una permutación
- **Tarea:** Escribe `sgn(b)`, que ordene la lista con intercambios vecinos y cuente cuántos hizo (`c`). Debe devolver `(-1)**(c % 2)`: `1` si la cuenta es par y `-1` si es impar.
- **Por qué:** `sgn(σ) = (-1)^k`, donde `k` es el número de transposiciones. La descomposición no es única, pero la paridad de `k` sí lo es, por eso el signo está bien definido.

[Ver el código en Github](https://github.com/locessentials/python/blob/main/unidad3/perms-combs/prob2-6.py)

## Problema 7: Paridad e inversiones
- **Tarea:** Escribe una función `is_even(perm)` que devuelva `True` si una permutación es par y `False` si es impar. Hazlo contando las "inversiones" (cuántos pares de números están fuera de orden) y verificando si esa cuenta es par o impar.
- **Por qué:** Conecta el código con la teoría de grupos más profunda. Es la forma algorítmica de determinar la paridad (signo) de una permutación sin tener que rastrear físicamente los intercambios. Debe coincidir con el signo del Problema 6.

## Problema 8: El determinante
- **Tarea:** Escribe `det(A)`, que calcule el determinante con la fórmula de Leibniz: genera todas las permutaciones con `per` (recursión con inserción, usando `insm`) y suma `sgn(σ) · A[0, σ(0)] · A[1, σ(1)] · ... · A[n-1, σ(n-1)]` para cada una. Compara el resultado con `np.linalg.det`. Requiere NumPy.
- **Por qué:** Une todo lo anterior: generar permutaciones, calcular su signo y usarlas como funciones. Cuesta O(n · n!), por eso NumPy usa otro método.

[Ver el código en Github](https://github.com/locessentials/python/blob/main/unidad3/perms-combs/prob2-8.py)