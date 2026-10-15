---
layout: default
title: Problema L
grandparent: 4. Problemas
parent: ICPC 2017
nav_order: 12
---

# ICPC 2017 - Problema L: línea de barrido

Hay **n** rectángulos en una cuadrícula, pero solo se ven sus esquinas: **n** esquinas de arriba a la izquierda y **n** esquinas de abajo a la derecha. No se sabe qué esquina va con cuál.

Empareja cada esquina de arriba a la izquierda con una de abajo a la derecha para que los rectángulos queden bien acomodados: cada dos rectángulos están uno dentro del otro o separados, y sus bordes nunca se enciman ni se cruzan. Si hay varias respuestas, cualquiera vale. Si no se puede, imprime `syntax error`.

**Entrada:** primer renglón: **n**. Luego **n** renglones con el renglón y la columna de cada esquina de arriba a la izquierda, y después **n** renglones con las esquinas de abajo a la derecha.

**Salida:** **n** renglones, uno por cada esquina de arriba a la izquierda, en orden. Cada renglón dice en qué lugar de la lista de esquinas de abajo a la derecha está su pareja (empezando en 1). Si no se puede, un solo renglón: `syntax error`.

**Límites:** 1 ≤ n ≤ 100 000, renglones y columnas entre 1 y 1 000 000 000, todas las esquinas en lugares distintos

**Ejemplos**

| Entrada 1 | Entrada 2 | Entrada 3 | Entrada 4 |
| --------- | --------- | --------- | --------- |
| arriba-izq:<br>1. (4, 7)<br>2. (9, 8)<br>abajo-der:<br>1. (14, 17)<br>2. (19, 18) | arriba-izq:<br>1. (4, 7)<br>2. (14, 17)<br>abajo-der:<br>1. (9, 8)<br>2. (19, 18) | arriba-izq:<br>1. (4, 8)<br>2. (9, 7)<br>abajo-der:<br>1. (14, 18)<br>2.(19, 17) | arriba-izq:<br>1. (1, 1)<br>2. (4, 8)<br>3. (8, 4)<br>abajo-der:<br>1. (10, 6)<br>2. (6, 10)<br>3. (10, 10) |
| **Salida:** 2, 1 (uno dentro del otro) | **Salida:** 1, 2 (separados) | **Salida:** syntax error | **Salida:** syntax error |
{: .columnas-iguales }

```
Ejemplo 1                   Ejemplo 2            Ejemplo 3             Ejemplo 4
uno dentro del otro         separados            se cruzan             bordes encimados

┌──────────┐                ┌──┐                  ┌───────┐            ┌──────────────────┐
│ ┌──────┐ │                └──┘                  │       │            │                  │
│ │      │ │                                     ┌┼─────┐ │            │            ┌─────┤
│ └──────┘ │                    ┌──┐             ││     │ │            │            │  B  │
└──────────┘                    └──┘             │└─────┼─┘            │            └─────┤
                                                 └──────┘              │        A         │
                                                                       │      ┌────┐      │
                                                                       │      │ C  │      │
                                                                       └──────┴────┴──────┘
```

---

## Conceptos clave: línea de barrido (*sweep line*) y búsqueda binaria (*binary search*)

La **línea de barrido** es una línea imaginaria que baja por la cuadrícula, de arriba hacia abajo. Ordenamos las esquinas por renglón y las revisamos una por una, en el orden en que la línea las toca, y en cada momento guardamos solo los rectángulos que ya se abrieron y todavía no se cierran. La usamos porque una esquina de abajo a la derecha solo puede cerrar un rectángulo que se abrió arriba de ella, así que basta con revisar cada esquina una vez en orden. Ordenar cuesta *n log n*, mientras que comparar todas las parejas posibles cuesta *n²*, y con n = 100 000 eso tardaría demasiado.

La **búsqueda binaria** encuentra un valor en una lista ordenada partiendo la lista a la mitad en cada paso: compara con el elemento del centro y sigue buscando solo en la mitad donde puede estar el valor. Así cada búsqueda cuesta *log n* en lugar de *n*. La usamos para encontrar la pareja de cada esquina y para contar los lados verticales que tocan cada borde.

Por ejemplo, para encontrar dónde va la columna 7:

```
lista:   2   5   9   12   15   20   25

paso 1:  mira el centro (12). 7 es menor  →  sigue solo en la mitad izquierda: 2  5  9
paso 2:  mira el centro (5).  7 es mayor  →  sigue solo en la mitad derecha:   9
paso 3:  mira el 9.           7 es menor  →  el 7 va justo antes del 9
```

---

## Panorama del código

Construimos el código como una línea de barrido, que funciona como una ventana que baja por la cuadrícula y solo ve lo que está abierto en ese momento. Por eso es rápida: en cada paso, el programa solo revisa lo que está dentro de esa ventana, no todos los rectángulos. 

El código hace dos barridos: el primero empareja las esquinas y el segundo verifica que los bordes no se crucen ni se encimen.

### Emparejar las esquinas (`match_corners`)

- Juntamos todas las esquinas en la lista `events` y la ordenamos por renglón. En el mismo renglón van primero las esquinas de abajo a la derecha, para no formar un rectángulo sin altura.
- Recorremos `events` de arriba hacia abajo: esta es la línea de barrido.
- Cada esquina de arriba a la izquierda abre un rectángulo: con `insort` la guardamos en `open_corners`, ordenada por columna (`column`, `corner_number`).
- Cada esquina de abajo a la derecha cierra un rectángulo. Con `bisect_left` encontramos dónde iría su columna en `open_corners`. La esquina justo antes de ese lugar es la esquina abierta más cercana a su izquierda. Buscamos `(column, -1)` en lugar de solo `column` para que una esquina en la misma columna quede a la derecha del lugar encontrado, y no la elijamos.

```
posición:     0     1     2
columna:      2     5     9
                       ↑
              el 7 iría aquí (posición 2)
```

- Esa es su pareja, porque el rectángulo abierto más cercano tiene que ser el de más adentro. La quitamos de `open_corners` y la guardamos en `partner_of`.
- Si no hay ninguna esquina abierta a su izquierda, el rectángulo no se puede cerrar y la respuesta es `syntax error`.

### Verificar los resultados (`check_rectangles`)

- El emparejamiento encuentra la única pareja posible para cada esquina, pero los bordes todavía se pueden cruzar o encimar, como en los ejemplos 3 y 4. Por eso hacemos una segunda línea de barrido.
- Para cada rectángulo creamos cuatro eventos: en el renglón de arriba abrimos sus dos lados verticales (`ADD`) y revisamos el borde de arriba (`CHECK`); en el renglón de abajo revisamos el borde de abajo (`CHECK`) y cerramos los lados (`REMOVE`).

```
columna:     7                    18
renglón 4:   ┌────────────────────┐    ADD: entran 7 y 18
             │                    │
             │   lados activos    │    active_columns = [7, 18]
             │                    │
renglón 19:  └────────────────────┘    REMOVE: salen 7 y 18
```

- Ordenamos los eventos por renglón. En el mismo renglón: primero abrir, luego revisar, al final cerrar. Así los lados del propio rectángulo siempre se cuentan.
- En `active_columns` guardamos, en orden, las columnas de los lados verticales abiertos.
- Para cada borde horizontal, contamos con `bisect_left` y `bisect_right` cuántos lados verticales abiertos hay entre su columna izquierda y su columna derecha.
- Deben ser exactamente 2: los lados de su propio rectángulo. Si hay más, algún borde se cruza o se encima con otro, y la respuesta es `syntax error`.

```
posición:          0    1    2    3
active_columns:  [ 7,   8,  17,  18 ]
                      ↑         ↑
         bisect_left(8) = 1   bisect_right(17) = 3

3 − 1 = 2  →  solo 8 y 17, sus propios lados  →  bien
```

```
posición:          0    1    2    3
active_columns:  [ 7,   8,  17,  18 ]
                 ↑              ↑
    bisect_left(7) = 0   bisect_right(17) = 3

3 − 0 = 3  →  7, 8 y 17  →  el 8 es de otro rectángulo  →  syntax error
```

```
columna:  7  8         17  18
             |               |      rectángulo A
          ┌──┼──────────┐    |      renglón 9: CHECK del borde de arriba de B
          |  |          |    |

active_columns = [7, 8, 17, 18]
borde de B: de la columna 7 a la 17  →  tocan 7, 8 y 17  →  3, no 2  →  syntax error
```

- Basta con revisar los bordes horizontales: si dos rectángulos se tocan en cualquier punto, siempre hay un borde horizontal de uno que toca un lado vertical del otro.

---

## Análisis del código

Library
Inputting corners with their position number in the list so as to be able to answe the problem

## Análisis

- **Construcción del algoritmo:**
  1. Leemos la entrada y guardamos cada esquina con su índice en la lista (empezando en 0), porque la salida pide la posición de cada pareja. Al imprimir sumamos 1, porque la salida empieza a contar en 1.
  2. Emparejamos con una primera línea de barrido. Lo que está abierto son esquinas de arriba a la izquierda, y cada esquina de abajo a la derecha toma la esquina abierta más cercana a su izquierda. Puede haber varias abiertas a la vez, y el rectángulo de más adentro (el que se abrió después) suele cerrarse primero.
  3. Verificamos con una segunda línea de barrido. Lo que está abierto son lados verticales, y en cada borde horizontal contamos cuántos lo tocan: deben ser 2, el lado izquierdo y el lado derecho de su propio rectángulo.
  4. Imprimimos `partner_of`, sumando 1 a cada número.

  **Nota:** En los dos barridos usamos `bisect`, de la biblioteca estándar de Python, para hacer búsqueda binaria en las listas ordenadas.

- **Variables y tipos de datos:** todo es `int`: n, renglones, columnas y números de esquina. No usamos `float` porque las coordenadas son enteras y las comparaciones deben ser exactas. `check_rectangles` regresa un `bool`, y la salida es `str`.

- **Estructuras de datos:**
  - Tuplas para las esquinas y los eventos: son datos fijos, y Python las ordena comparando elemento por elemento (primero el renglón, luego el tipo).
  - Listas ordenadas para `open_corners` y `active_columns`: permiten búsqueda binaria. Un diccionario no guarda orden, y un montículo solo da el mínimo, no el más cercano a la izquierda.
  - `partner_of` es una lista donde la posición es la esquina de arriba y el valor es su pareja.

- **Paradigma algorítmico:** línea de barrido con una estrategia voraz: cada esquina de abajo a la derecha toma la esquina abierta más cercana, y esa elección siempre es correcta porque el rectángulo abierto más cercano tiene que ser el de más adentro.

- **Estilo de programación:** procedural, con una función por paso (`read_input`, `match_corners`, `check_rectangles`, `print_results`) y `main` que las llama en orden.

- **Iterativo o recursivo:** iterativo. Recorremos los eventos con un ciclo; con hasta 400 000 eventos, la recursión pasaría el límite de Python.

- **Complejidad:**
  - Tiempo: ordenar cuesta *n log n* y cada búsqueda binaria cuesta *log n*. `insort` y `pop` mueven elementos de la lista, así que en el peor caso cuestan *n²* en total, pero en la práctica son rápidos. Con un árbol balanceado sería *n log n*.
  - Espacio: *n*, por las listas de esquinas y eventos.