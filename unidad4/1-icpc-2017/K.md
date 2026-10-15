---
layout: default
title: Problema K
grandparent: 4. Problemas
parent: ICPC 2017
nav_order: 11
---

# ICPC 2017 - Problema K: probabilidad de cadenas (autocorrelación)

Hay una secuencia escondida de **n** letras. Cada letra es R, P o S, elegida al azar. **La secuencia nunca se ve.** Solo se sabe cuántas letras tiene.

Se dan **s** patrones, todos del mismo largo, hechos con R, P y S.

Ordena los patrones de mayor a menor según la probabilidad de que aparezcan en algún lugar de la secuencia escondida, como letras seguidas. Si dos patrones empatan, se quedan en el orden de la entrada.

**Entrada:** primer renglón: **n** (el largo de la secuencia escondida) y **s** (cuántos patrones siguen). Luego **s** renglones, un patrón por renglón.

**Límites:** 1 ≤ n ≤ 1 000 000, 1 ≤ s ≤ 10, largo de cada patrón ≤ 100 000

**Ejemplos**

| Entrada 1 | Entrada 2 |
| --------- | --------- |
| n = 3, s = 4<br>PP, RR, PS, SS | n = 20, s = 3<br>PRSPS, SSSSS, PPSPP |
| **Salida:** PS, PP, RR, SS | **Salida:** PRSPS, PPSPP, SSSSS |

## Conceptos clave y por qué aplican

- **autocorrelación de cadenas**
  - qué es: la lista de pasos en los que un patrón coincide consigo mismo al moverlo, una posición a la vez, sobre una copia de sí mismo
  - por qué aplica: un patrón que se encima consigo mismo suele aparecer varias veces junto en la misma secuencia, así que aparece en menos secuencias distintas; por eso, entre menos se encime un patrón, más probable es que aparezca

- **Z-function**
  - qué es: un algoritmo que calcula, para cada posición de una cadena, cuántas letras coinciden con el inicio de la misma cadena
  - por qué aplica: calcula la autocorrelación del patrón; en cada posición compara las últimas letras del patrón con las primeras (cada vez una letra menos), y si todas coinciden, el patrón se encima consigo mismo en ese paso, aprovecha lo que ya calculó en posiciones anteriores, así que recorre el patrón una sola vez, aunque tenga 100 000 letras

```
pattern:  P P S P P
position: 0 1 2 3 4

position 1:  P S P P   vs  P P S P  → 1 letter matches, then stops
position 2:  S P P     vs  P P S    → 0 letters match
position 3:  P P       vs  P P      → 2 letters match, all the way to the end ✓
position 4:  P         vs  P        → 1 letter matches, all the way to the end ✓
```

- **ordenamiento estable** (*stable sort*)
  - qué es: un ordenamiento que deja en el mismo orden los elementos que tienen el mismo valor
  - por qué aplica: el problema pide que los patrones con la misma probabilidad queden en el orden de la entrada; `sorted()` de Python ya es estable: cuando dos elementos de la lista empatan, deja primero el que estaba primero en la entrada (no cambia las letras de cada patrón, solo el orden de los patrones en la lista)