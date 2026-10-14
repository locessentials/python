---
layout: default
title: Problema H
grandparent: 4. Problemas
parent: ICPC 2017
nav_order: 8
---

# ICPC 2017 - Problema H: planificación con plazos

Hay **n** tareas. Cada tarea tarda exactamente **t** unidades de tiempo. Para cada tarea se dan dos números:

- **a**: lo más temprano que se puede empezar la tarea
- **b**: el momento en que la tarea ya tiene que estar terminada

Solo se puede hacer una tarea a la vez, y una tarea no se puede interrumpir: una vez que empieza, dura **t** unidades seguidas.

¿Es posible acomodar todas las tareas de modo que cada una **empiece en a o después** y **termine en b o antes**?

**Salida:** `yes` si se puede, `no` si no se puede.

**Límites:** 1 ≤ n ≤ 10 000, 1 ≤ t ≤ 100 000, a + t ≤ b ≤ 1 000 000 000

## Ejemplos

| Entrada 1 | Entrada 2 | Entrada 3 |
| --------- | --------- | --------- |
| n = 2, t = 10<br>tarea 1: a = 0, b = 15<br>tarea 2: a = 5, b = 20 | n = 2, t = 10<br>tarea 1: a = 1, b = 15<br>tarea 2: a = 0, b = 20 | n = 2, t = 10<br>tarea 1: a = 5, b = 30<br>tarea 2: a = 10, b = 20 |
| **Salida:** yes | **Salida:** no | **Salida:** yes |