---
layout: default
title: Problema H
grandparent: 4. Problemas
parent: ICPC 2017
nav_order: 8
---

# ICPC 2017 - Problema H: planificación con plazos

Hay **n** tareas. Cada tarea tarda exactamente **t** unidades de tiempo (en el código: `task_duration`). Para cada tarea se dan dos números:

- **a** (en el código: `earliest_start`): lo más temprano que se puede empezar la tarea
- **b** (en el código: `deadline`): el momento en que la tarea ya tiene que estar terminada

Solo se puede hacer una tarea a la vez, y una tarea no se puede interrumpir: una vez que empieza, dura **t** unidades seguidas.

¿Es posible acomodar todas las tareas de modo que cada una **empiece en a o después** y **termine en b o antes**?

**Salida:** `yes` si se puede, `no` si no se puede.

**Límites:** 1 ≤ n ≤ 10 000, 1 ≤ t ≤ 100 000, a + t ≤ b ≤ 1 000 000 000

**Ejemplos**

| Entrada 1 | Entrada 2 | Entrada 3 |
| --------- | --------- | --------- |
| n = 2, t = 10<br>tarea 1: a = 0, b = 15<br>tarea 2: a = 5, b = 20 | n = 2, t = 10<br>tarea 1: a = 1, b = 15<br>tarea 2: a = 0, b = 20 | n = 2, t = 10<br>tarea 1: a = 5, b = 30<br>tarea 2: a = 10, b = 20 |
| **Salida:** yes | **Salida:** no | **Salida:** yes |

## Conceptos claves

- **regiones prohibidas** (*forbidden regions*) - intervalos de tiempo en los que no se puede empezar ninguna tarea, si una tarea empezara ahí, todavía estaría en curso cuando otro grupo de tareas necesita el tiempo para terminar antes de su **b**; se calculan del `earliest_start` más tardío al más temprano, antes de armar el horario (preprocesamiento), pero por sí solas no arman el horario: solo dicen dónde no empezar

- **primero el plazo más próximo** (*earliest deadline first*, EDF) - regla voraz (*greedy*): avanza del tiempo más temprano al más tardío y, cada vez que se puede empezar una tarea, elige, entre las que ya están disponibles, la que tiene el **b** más pequeño; por sí solo falla en este problema: puede empezar una tarea demasiado pronto, cuando lo correcto era esperar

- **usados juntos** - las regiones prohibidas miran hacia atrás desde el final y marcan el tiempo que las tareas tardías van a necesitar; EDF avanza hacia adelante y solo ve las tareas que ya están disponibles, así que las regiones prohibidas son lo que le avisa que hay tareas más adelante y que tiene que esperar; juntos dan la respuesta correcta: primero se calculan las regiones prohibidas y después se aplica EDF saltando esas regiones

**Ejemplo** (Entrada 3, `task_duration = 10`): tarea 1 (`earliest_start = 5`, `deadline = 30`), tarea 2 (`earliest_start = 10`, `deadline = 20`)

**EDF solo:** en 5 solo está disponible la tarea 1, así que la empieza; la tarea 2 termina en 25, después de su `deadline` de 20; la respuesta sale `no`

```
tiempo: 0    5    10   15   20   25   30
             [ tarea 1][ tarea 2]
```

**EDF con la región prohibida (0, 10):** 5 está dentro de la región, así que EDF espera hasta 10; en 10 están disponibles las dos tareas y elige la tarea 2 porque su `deadline` es más próximo; las dos terminan a tiempo y la respuesta es `yes`

```
tiempo: 0    5    10   15   20   25   30
                  [ tarea 2][ tarea 1]
```

**Nota:** la combinación de regiones prohibidas con EDF viene del artículo de Garey, Johnson, Simons y Tarjan (1981, *SIAM Journal on Computing*, "Scheduling Unit-Time Tasks with Arbitrary Release Times and Deadlines").

## Resumen del código

### Regiones prohibidas

- `find_forbidden_regions`: usa un conjunto (*set*) para tener cada `earliest_start` una sola vez; recorre esos valores del más tardío al más temprano y, con cada uno como `window_start`, llama a `pack_backwards`; si entre `window_start` y el inicio del grupo hay menos de `task_duration`, agrega la región prohibida `(inicio del grupo - task_duration, window_start)`; devuelve la lista de regiones, o `None` si algún grupo no cabe.

```
tasks = [(0, 15), (5, 20), (5, 30)]
distinct_starts = {0, 5}                # el 5 aparece una sola vez
sorted(distinct_starts, reverse=True)   # [5, 0]
```

**Ejemplo** (Entrada 3, `task_duration = 10`): `distinct_starts` = [10, 5]

1. `window_start = 10`: grupo = tarea 2; `pack_backwards` devuelve 10; 10 < 10 + 10, se agrega la región (0, 10)

```
tiempo: 0    5    10   15   20   25   30
        (xxxxxxxx)[ tarea 2]
                  ^ window_start = 10
```

2. `window_start = 5`: grupo = tarea 1 y tarea 2; `pack_backwards` devuelve 10; 10 < 5 + 10, se agrega la región (0, 5)

```
tiempo: 0    5    10   15   20   25   30
        (xxx)     [ tarea 2][ tarea 1]
             ^ window_start = 5
```

Resultado: `[(0, 10), (0, 5)]`

- `pack_backwards`: `find_forbidden_regions` la llama una vez por cada `window_start`, del más tardío al más temprano; toma todas las tareas con `earliest_start >= window_start` y las acomoda hacia atrás: la de mayor `deadline` va en la última posición y las demás van antes; devuelve el momento más tardío en que el grupo puede empezar sin que ninguna tarea termine después de su `deadline` (`int`).

- `move_out_of_forbidden_regions`: si un inicio cae dentro de una región prohibida, lo mueve al borde izquierdo de esa región y repite hasta que quede fuera de todas.

### EDF

- `schedule_with_edf`: avanza en el tiempo y, entre las tareas disponibles, siempre empieza la de `deadline` más próximo, que saca de un montículo (*heap*) en O(log n); devuelve `True` si todas terminan a tiempo y `False` si no (`bool`).

**Montículo en EDF** (Entrada 3, `task_duration = 10`)

En 10, EDF agrega al montículo los `deadline` de las dos tareas. Cada número nuevo entra abajo y sube mientras sea más pequeño que el número de arriba.

```
agregar 30       agregar 20       20 sube
    30               30              20
                    /               /
                  20              30
```

EDF saca el número de arriba, el `deadline` más próximo:

```
sacar 20: tarea 2, de 10 a 20         sacar 30: tarea 1, de 20 a 30
      30                                    (vacío)
```

**Por qué O(log n):** cuando un número sube o baja en el montículo, se mueve un nivel por cada intercambio (arriba, el 20 subió un nivel con un intercambio). Por eso, los intercambios son, a lo más, el número de niveles. Y los niveles son pocos, porque cada nivel tiene el doble de números que el nivel de arriba:

```
nivel 1:          o                 1
nivel 2:        o   o               2
nivel 3:       o o o o              4
nivel 4:      oooooooo              8
  ...
nivel 14:   oooooooooooo...       hasta 8192
```

Con 10 000 tareas, el montículo tiene unos 14 niveles, así que agregar o sacar un número cuesta, a lo más, unos 13 intercambios. Ese número de niveles es log n: cuántas veces se puede dividir n entre 2 hasta llegar a 1. Por eso agregar o sacar cuesta O(log n). EDF agrega y saca cada tarea una vez, así que en total cuesta O(n log n).

- `move_past_forbidden_regions`: si el tiempo actual cae dentro de una región prohibida, lo mueve al borde derecho de esa región y repite hasta que quede fuera de todas.

## Análisis

- **Construcción del algoritmo:**
  1. Leer `task_duration` y los pares `(earliest_start, deadline)`.
  2. Calcular las regiones prohibidas, del `earliest_start` más tardío al más temprano; si algún grupo no cabe, la respuesta es `no`.
  3. Aplicar EDF del tiempo más temprano al más tardío, saltando las regiones prohibidas.
  4. Imprimir `yes` si todas las tareas terminan a tiempo y `no` si alguna no.

  En EDF, cada parte decide una cosa distinta:
  - `earliest_start` decide **cuándo entra** una tarea al montículo: solo entra cuando `current_time` llega a su `earliest_start`
  - las regiones prohibidas deciden **cuándo** EDF toma la siguiente tarea, porque mueven `current_time` fuera de ellas
  - el montículo decide **cuál** tarea va: de las que ya están dentro, la de `deadline` más pequeño

- **Variables y tipos de datos:** `task_duration`, `earliest_start`, `deadline` y `current_time` son `int`, porque el tiempo se da en unidades enteras; en `pack_backwards`, `current_time` empieza en `float("inf")` para que la primera tarea termine en su `deadline`; `schedule_with_edf` devuelve `bool`: `True` si todas las tareas terminan a tiempo y `False` si alguna no; la salida es `str` (`yes` o `no`), la respuesta en el formato que pide el problema.

- **Estructuras de datos:**
  - tuplas para cada tarea `(earliest_start, deadline)` y cada región `(inicio, fin)`: son pares fijos que no cambian
  - listas para las tareas y las regiones, porque se pueden ordenar y recorrer
  - un conjunto (*set*) para tener cada `earliest_start` una sola vez
  - un montículo (*heap*) para tener siempre a mano el `deadline` más pequeño en O(log n), mientras entran y salen tareas
  - no se necesitan diccionarios, colas ni grafos: no hay que buscar por nombre ni hay conexiones entre tareas

- **Paradigma algorítmico:** voraz (*greedy*) con preprocesamiento; EDF solo falla porque no sabe cuándo esperar, y las regiones prohibidas, calculadas antes, le dan esa información.

- **Estilo de programación:** imperativo/procedural, con una función por paso; así cada parte se puede explicar y probar por separado.

- **Iterativo o recursivo:** iterativo; el montículo es un árbol, pero `heapq` lo guarda en una lista y solo mueve un número por un camino, sin recorrer todo el árbol; además, con hasta 10 000 tareas la recursión podría pasar el límite de profundidad de Python (1000 llamadas).

- **Complejidad:**
  - ordenar las tareas y usar el montículo: O(n log n)
  - lo que más cuesta es `find_forbidden_regions`, porque tiene cuatro ciclos, uno dentro de otro, y cada uno puede repetirse hasta n veces: los valores de `window_start`, las tareas del grupo, las pasadas de `move_out_of_forbidden_regions` y las regiones; n × n × n × n da O(n⁴) en el peor caso: si n se duplica, el costo se multiplica por 16
  - espacio: O(n), porque las listas, el conjunto, las regiones y el montículo tienen, a lo más, n elementos: si n se duplica, la memoria se duplica