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
  - por qué aplica: un patrón que se encima consigo mismo suele aparecer varias veces junto en la misma secuencia, así que aparece en menos secuencias distintas; para comparar dos patrones, se busca el primer paso donde son distintos, y el que se encima en ese paso es menos probable

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

## Panorama del código

### Z-function (`z_function`)

- `match_lengths` guarda, para cada posición, cuántas letras seguidas coinciden entre el original, leído desde esa posición, y la copia, que siempre empieza en la primera letra del patrón
- la ventana (de `window_start` a `window_end`) son las letras del original que un turno anterior ya comparó con la copia y coincidieron, así que no hace falta volver a compararlas
- al principio la ventana está vacía; cada coincidencia nueva crea una ventana que sirve para las posiciones que siguen
- si la posición todavía no está en la ventana, match_length empieza en 0 y se comparan las letras una por una
- si la posición está dentro de la ventana, se copia el valor de la posición que le corresponde en el inicio (`position - window_start`), sin pasar del final de la ventana, y luego se sigue comparando
- si esta coincidencia termina después del final de la ventana, se vuelve la nueva ventana
- gracias a la ventana, una letra que ya coincidió no se vuelve a comparar, así que el trabajo total crece igual que el largo del patrón

```
patrón:    P P S P P
posición:  0 1 2 3 4

posición 1  (todavía no está en la ventana: match_length empieza en 0)
original: P P S P P
copia:      P P S P P
comparar:   ✓ ✗                 match_lengths[1] = 1, ventana = posición 1

posición 2  (todavía no está en la ventana: match_length empieza en 0)
original: P P S P P
copia:        P P S P P
comparar:     ✗                 match_lengths[2] = 0

posición 3  (todavía no está en la ventana: match_length empieza en 0)
original: P P S P P
copia:          P P S P P
comparar:       ✓ ✓             match_lengths[3] = 2, ventana = posiciones 3–4

posición 4  (en la ventana: match_length empieza en 1 y se aprovecha lo que ya sabemos)
posición:  0 1 2 3 4
patrón:    P P S P P
                [P P]           ventana = posiciones 3–4
          [P P]                 inicio  = posiciones 0–1

la posición 4 en la ventana = la posición 1 en el inicio
match_lengths[1] = 1, letras que quedan en la ventana = 1  →  empezar en min(1, 1) = 1
original: P P S P P
copia:            P P S P P
comparar:         ✓             (ya se sabe, no hace falta comparar)
                                fin del patrón  →  match_lengths[4] = 1

resultado:
posición:       0 1 2 3 4
match_lengths:  0 1 0 2 1       (el 0 de la posición 0 solo ocupa el lugar; no se usa)
```

Las posiciones 3 y 4 llegan al final del patrón (3 + 2 = 5 y 4 + 1 = 5), así que PPSPP se encima consigo mismo en los pasos 3 y 4.

### Banderas de encimamiento (`overlap_flags`)

- llama a `z_function` y revisa cada paso (`shift`), empezando en 1
- el patrón se encima en un paso si la coincidencia llega hasta el final del patrón: `shift + match_lengths[shift] == pattern_length`
- guarda un 1 en `flags` si la coincidencia llega hasta el final del patrón, y un 0 si no, aunque coincidan algunas letras
- se detiene cuando las dos copias ya no caben en la secuencia escondida (`pattern_length + shift > sequence_length`), porque los pasos siguientes tampoco caben
- si el patrón es más largo que la secuencia escondida, flags queda vacía, así que todos los patrones empatan y se imprimen en el orden de la entrada

```
shift:            1  2  3  4
match_lengths:    1  0  2  1
shift + match:    2  2  5  5        (donde terminó la coincidencia)
flags:            0  0  1  1
```

```
secuencia escondida (n = 6):  _ _ _ _ _ _

shift 1:  P P S P P
            P P S P P         6 letras → cabe

shift 3:  P P S P P
              P P S P P       8 letters → no cabe
```

### Ordenamiento (`sort_patterns` y `get_flags`)

- `sort_patterns` calcula las `flags` de cada patrón una sola vez y las guarda junto al patrón
- `get_flags` hace que `sorted()` compare solo las `flags`, y no el texto del patrón
- `sorted()` compara las `flags` de izquierda a derecha y se detiene en el primer paso donde son distintas; el patrón con 0 en ese paso queda antes, porque es más probable
- `sorted()` es estable, así que los patrones que empatan quedan en el orden de la entrada

```
SSSSS se encima en el paso 1:
S S S S S
  S S S S S
          ↑          1 letra al azar debe ser S              → 1/3

PPSPP se encima en el paso 4:
P P S P P
        P P S P P
          ↑ ↑ ↑ ↑    4 letras al azar deben ser P S P P      → 1/81
```

## Análisis del código

- **Construcción del algoritmo:** (1) leer n, s y los patrones; (2) para cada patrón, calcular `match_lengths` con la Z-function; (3) con `match_lengths`, guardar en `flags` un 1 en cada paso donde el patrón se encima consigo mismo y un 0 donde no, solo mientras las dos copias quepan en la secuencia escondida; (4) ordenar los patrones por sus `flags` con un ordenamiento estable; (5) imprimir los patrones en ese orden

- **Variables y tipos de datos:** `sequence_length`, `position`, `shift`, `match_length`, `window_start` y `window_end` son `int`, porque son largos y posiciones; cada patrón es un `str`; `match_lengths` y `flags` son listas de `int`; no se usa `float`, porque nunca se calcula una probabilidad, solo se comparan las `flags`, así que no hay errores de redondeo

- **Estructuras de datos:** listas: `patterns` guarda los patrones en el orden de la entrada (necesario para los empates), `match_lengths` usa la posición como índice, y `flags` se compara de izquierda a derecha con `sorted()`; tuplas: cada par (`flags`, patrón) une un patrón con sus `flags` para ordenarlos juntos; no hacen falta diccionarios, conjuntos, colas, montículos ni grafos, porque solo se recorre cada patrón en orden y se ordenan como mucho 10 patrones

- **Paradigma algorítmico:** algoritmo de cadenas (Z-function) que aprovecha resultados anteriores (la ventana) en vez de volver a comparar letras; además, en lugar de calcular probabilidades con fuerza bruta (revisar las 3 elevado a n secuencias posibles, imposible con n = 1 000 000), se usa una propiedad: en el primer paso donde dos patrones son distintos, el que se encima es menos probable

- **Estilo de programación:** imperativo/procedural, con una función para cada paso (`read_input`, `z_function`, `overlap_flags`, `sort_patterns`), así cada parte se puede explicar y probar por separado

- **Iterativo o recursivo:** iterativo; los patrones pueden tener 100 000 letras, y una versión recursiva pasaría el límite de recursión de Python

- **Complejidad:** temporal O(s × L), donde L es el largo del patrón: la Z-function y `overlap_flags` recorren cada patrón una vez; el ordenamiento compara pocas parejas de `flags` (s ≤ 10), cada una de largo L como mucho; espacial O(s × L), por las listas `match_lengths` y `flags` de cada patrón; la operación que determina la complejidad es la comparación de letras dentro de la Z-function