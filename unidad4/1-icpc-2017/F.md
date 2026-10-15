---
layout: default
title: Problema F
grandparent: 4. Problemas
parent: ICPC 2017
nav_order: 6
---

# ICPC 2017 - Problema F: imagen posterizada

- Entrada: **d** intensidades de rojo distintas, en orden creciente (**r** = intensidad, **p** = número de píxeles con esa intensidad), y **k** = número de valores permitidos en la imagen posterizada
- Cada canal de color de un píxel (rojo, verde y azul) es un entero entre 0 y 255; el problema solo usa el rojo. Entonces, elegir k valores enteros dentro de ese rango (no tienen que estar en la entrada); cada píxel se cambia al valor permitido más cercano
- Error de cada píxel: (r − v)², donde **v** es su nuevo valor; elevar al cuadrado quita el signo y castiga más los errores grandes
- Salida: la suma mínima de los errores de todos los píxeles, es decir, la imagen posterizada más parecida a la original
- Límites: d ≤ 256; k ≤ d; p ≤ 2²⁶

**Reto:** solo podemos usar k valores; hay que decidir dos cosas a la vez:
  1. cómo dividir las intensidades en k grupos (cada grupo son intensidades vecinas)
  2. a qué valor v se cambia cada grupo

todo para que la suma total de errores sea la mínima posible

---

## Conceptos clave

### ¿Por qué el promedio ponderado?

- Dentro de un grupo, todas las intensidades se cambian a un mismo valor v; hay que elegir el v que produce el menor error para ese grupo
- Como el error de cada píxel es (r − v)², el error total del grupo forma una parábola (curva en forma de U) según el valor de v: baja, llega a un punto mínimo y vuelve a subir; buscamos ese punto mínimo
- Para encontrar el punto mínimo: cada píxel "jala" a v hacia su propia intensidad, y entre más lejos está, más fuerte jala, porque el error es al cuadrado. Por ejemplo, si un píxel está a distancia 1 de v, su error es 1² = 1; si v se aleja un paso, queda a distancia 2 y su error es 2² = 4 (sube 3). Si un píxel está a distancia 30, su error es 30² = 900; un paso más lejos es 31² = 961 (sube 61)
- Si un lado jala más fuerte, mover v hacia ese lado baja el error total: los píxeles de ese lado bajan su error más de lo que sube el error del otro lado
- Mientras un lado jale más, todavía se puede bajar el error; entonces el punto mínimo es donde los dos lados jalan igual (el punto de equilibrio, o el promedio ponderado), porque ahí ningún movimiento ayuda

**Comprobación con el Ej. 1 (v = 83)**

d = 2
k = 1

| r | p | r × p |
|---|---|---|
| 50 | 20,000 | 1,000,000 |
| 150 | 10,000 | 1,500,000 |
| **total** | **30,000** | **2,500,000** |

v = 2,500,000 / 30,000 = 83.33, que se redondea a 83

| lado | píxeles × distancia | jalón |
|---|---|---|
| izquierda (50) | 20,000 × 33.33 | ≈ 666,667 |
| derecha (150) | 10,000 × 66.67 | ≈ 666,667 |

Si movemos v en cualquier dirección, el error total sube.

**Cómo calcular el promedio ponderado**

Para calcular el mejor valor v de un grupo:

1. **Suma ponderada:** multiplicar cada intensidad r por su número de píxeles p, y sumar los resultados
2. **Total de píxeles:** sumar todos los p
3. **v = suma ponderada / total de píxeles**

$$
v = \frac{\text{suma ponderada}}{\text{total de píxeles}}
$$

- **suma ponderada:** cada intensidad r multiplicada por su número de píxeles p, todo sumado
- **total de píxeles:** todos los p sumados

$$
v = \frac{\sum_{i=1}^{d} p_i \cdot r_i}{\sum_{i=1}^{d} p_i}
$$

$$
v = \frac{50 \cdot 20{,}000 + 150 \cdot 10{,}000}{20{,}000 + 10{,}000} = \frac{2{,}500{,}000}{30{,}000} = 83.33
$$

**Justificación formal:** el error del grupo es una parábola (curva en forma de U) en v, y su punto más bajo está donde la derivada vale 0:

$$
E(v) = \sum p_i (r_i - v)^2
\qquad
\frac{dE}{dv} = -2 \sum p_i (r_i - v) = 0
\quad\Rightarrow\quad
v = \frac{\sum p_i \cdot r_i}{\sum p_i}
$$

La ecuación Σ pᵢ(rᵢ − v) = 0 es el mismo equilibrio: lo que jalan los de la izquierda menos lo que jalan los de la derecha da 0.

v tiene que ser entero, así que probamos el entero de abajo y el de arriba del promedio (83 y 84) y nos quedamos con el que da menos error.

---

## Panorama del código

El código tiene tres pasos: una función que calcula el error de un grupo, una tabla con el error de cada grupo posible, y la programación dinámica, que usa esa tabla para encontrar la mejor forma de dividir las intensidades en k grupos.

### 1. Error de un grupo (`group_error`)

- Un grupo es un tramo (*stretch, as in stretch of road*) de intensidades vecinas en `red_v` (lista de valores de intensidad del rojo y su p), desde la posición `start` hasta `end` (las dos incluidas). Todas se cambian a un mismo valor v.
- Primer ciclo: sumamos `total_pixels` (todos los p, p = número de píxeles que tienen la intensidad de rojo r) y `weighted_sum` (cada r, o valor de intensidad del rojo, multiplicada por su p).
- Con eso calculamos el promedio ponderado. `//` redondea hacia abajo y da `v_low`; `v_high` es el entero de arriba.
- Segundo ciclo: calculamos el error del grupo con cada uno de los dos valores. Cada intensidad suma p × (r − v)²: elevar al cuadrado quita el signo y castiga más los errores grandes, y multiplicamos por p porque todos los píxeles con esa intensidad tienen el mismo error.
- Regresamos el menor de los dos errores.

### 2. Tabla de errores (`error_table`)

- Un grupo se define por dónde empieza (`start`) y dónde termina (`end`). `error_table[start][end]` guarda su error.
- Llenamos la tabla con dos ciclos: para cada `start`, probamos cada `end` desde `start` hasta la última intensidad. Si `end` es menor que `start` no hay grupo, y ese espacio se queda en 0.
- Así calculamos el error de cada grupo una sola vez, y el paso 3 solo lo consulta.

Ejemplo 3 (intensidades 0, 25, 50, 255): cada espacio guarda el error del grupo que se muestra.

```
              end = 0   end = 1    end = 2        end = 3
start = 0     [0]       [0, 25]    [0, 25, 50]    [0, 25, 50, 255]
start = 1      —        [25]       [25, 50]       [25, 50, 255]
start = 2      —         —         [50]           [50, 255]
start = 3      —         —          —             [255]
```
Los mismos espacios con su error (cada intensidad tiene 30,000 píxeles):

```
              end = 0   end = 1      end = 2       end = 3
start = 0     0         9,390,000    37,500,000    1,227,780,000
start = 1      —        0            9,390,000     955,500,000
start = 2      —         —           0             630,390,000
start = 3      —         —            —            0
```

### 3. Programación dinámica (`best_error`)

- `best_error[num_groups][covered]` guarda el menor error para las primeras `covered` intensidades, usando `num_groups` grupos. Usa los errores de `error_table` y los combina para encontrar la mejor forma de dividir las intensidades en k grupos. La tabla empieza llena de `INFINITY` (todavía no se puede), menos `best_error[0][0] = 0`: 0 intensidades con 0 grupos no tienen error. Ese es el punto de partida.

```
                covered=0  covered=1  covered=2   covered=3             covered=4
num_groups=0    0          INF        INF         INF                   INF
num_groups=1    INF        [0]        [0,25]      [0,25,50]             [0,25,50,255]
num_groups=2    INF        INF        [0]|[25]    mejor de 2 opciones   mejor de 3 opciones  ← respuesta
                                                 es decir, [0] | [25, 50]
                                                 o [0, 25] | [50]

```

```
                covered=0  covered=1  covered=2   covered=3    covered=4
num_groups=0    0          INF        INF         INF          INF
num_groups=1    INF        0          9,390,000   37,500,000   1,227,780,000
num_groups=2    INF        INF        0           9,390,000    37,500,000  ← respuesta
```

- `num_groups` va de 1 a k (el máximo de valores de rojo distintos permitidos), porque para encontrar la respuesta con k grupos, el programa primero resuelve los casos más pequeños; `covered` funciona igual, pero con las intensidades: va de 1 a d (el total de distintos rojos), y quiere decir "usar solo las primeras `covered` intensidades, como si las demás no existieran todavía".

Para [0, 25, 50, 255]:

```
covered = 1:   [0]                  25   50   255   ← todavía no se usan
covered = 2:   [0, 25]                   50   255   ← todavía no se usan
covered = 3:   [0, 25, 50]                    255   ← todavía no se usan
covered = 4:   [0, 25, 50, 255]
```

- Llenamos la tabla con 1 grupo, luego con 2, hasta k. Para cada `covered`, probamos cada lugar donde puede ir el último corte (`last_start` = donde empieza el último grupo); lo de la izquierda del corte ya está resuelto en el renglón de arriba.

```
last_start = 1:   [0]          | [25, 50, 255]
last_start = 2:   [0, 25]      | [50, 255]
last_start = 3:   [0, 25, 50]  | [255]
```

- Cada corte divide el problema en dos partes: `error_before`, el mejor error antes del corte con un grupo menos (ya guardado en `best_error`), y `error_last`, el error del último grupo (de `error_table`). Guardamos la suma más pequeña en best_error[num_groups][covered], y el renglón de abajo la usa después.

```
1 GRUPO (solo hay una forma: todo en un grupo)
  [0]              →  error del grupo [0]
  [0, 25]          →  error del grupo [0, 25]
  [0, 25, 50]      →  error del grupo [0, 25, 50]

2 GRUPOS, para [0, 25, 50, 255]: probamos cada corte
  [0]          +  [25, 50, 255]
  [0, 25]      +  [50, 255]
  [0, 25, 50]  +  [255]
  ───────────     ─────────────
  ya guardado      un grupo más
  arriba           (error_table)
```

- `covered` empieza en `num_groups` y `last_start` en `num_groups − 1` porque cada grupo necesita al menos una intensidad.
- Esta es la idea de la programación dinámica: cada respuesta se construye con respuestas más pequeñas que ya están guardadas, sin volver a calcularlas.
- Así cada renglón se construye con el de arriba, hasta llegar a `best_error[k][d]`: todas las d intensidades con k grupos. Esa es la respuesta.

## Análisis del código

### Construcción del algoritmo

1. Leer d, k y las d parejas (r, p).
2. `group_error`: para un grupo, calcular el promedio ponderado, probar el entero de abajo y el de arriba, y regresar el menor error.
3. `error_table`: calcular el error de cada grupo posible una sola vez.
4. `best_error`: llenar renglón por renglón (1 grupo, 2 grupos, hasta k); en cada espacio, probar cada lugar del último corte y guardar la suma más pequeña.
5. Imprimir `best_error[k][d]`.

### Variables y tipos de datos

- Todo es `int`: d, k, r, p, las sumas, v y los errores. La respuesta debe ser un entero exacto, y `float` puede perder precisión.
- Por eso usamos `//` (da `int`) para el promedio, e `INFINITY = 2 ** 63` (entero) en lugar de `float('inf')`.

### Estructuras de datos

- `red_v`: lista de parejas [r, p], en orden creciente; el orden es importante porque los grupos son intensidades vecinas.
- `error_table` y `best_error`: matrices (listas de listas). Los índices son enteros seguidos (0, 1, 2…), así que una lista da acceso directo a cada espacio en O(1); un diccionario no da ninguna ventaja aquí.
- No se necesitan colas, montículos ni grafos: no hay que buscar caminos ni sacar siempre el menor elemento.

### Paradigma algorítmico

- Programación dinámica: el mejor resultado con k grupos se construye con los mejores resultados con k − 1 grupos, y esos resultados se repiten, así que se guardan para no volver a calcularlos.
- Fuerza bruta no sirve: hay demasiadas formas de dividir d intensidades en k grupos.
- Voraz no sirve: elegir el mejor corte en cada paso no garantiza el menor error total.

### Estilo de programación

- Imperativo/procedural: una función (`group_error`) y ciclos. Es un problema pequeño con una sola entrada; basta con una función y ciclos.

### Iterativo o recursivo

- Iterativo: los ciclos llenan las tablas de los casos pequeños a los grandes, así que el renglón de arriba siempre está listo cuando se necesita.
- Sin recursión, no hay riesgo de pasar el límite de recursión de Python y se usa menos memoria.

### Complejidad

- Tiempo: O(d³). Llenar `error_table` es O(d³) (d² grupos, y cada `group_error` recorre hasta d intensidades); la programación dinámica es O(k · d²), y k ≤ d. Con d = 256, son unos millones de operaciones.
- Espacio: O(d²), por las dos tablas.
- La operación que determina el tiempo son las sumas dentro de `group_error`.