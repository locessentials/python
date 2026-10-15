---
layout: default
title: Problema L
grandparent: 4. Problemas
parent: ICPC 2017
nav_order: 12
---

# ICPC 2017 - Problema L: Visual Python++ (línea de barrido)

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