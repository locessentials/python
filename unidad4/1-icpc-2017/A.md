---
layout: default
title: Problema A
grandparent: 4. Problemas
parent: ICPC 2017
nav_order: 1
---

# ICPC 2017 - Problema A

Dado un **polígono simple** de *n* vértices, en sentido antihorario, calcular la longitud del **segmento de recta más largo** que cabe dentro de él.

- El segmento **no puede salir** del polígono.
- El segmento **sí puede tocar** el borde o **correr a lo largo** de un lado.
- El polígono puede ser **no convexo**.

**Entrada**

La entrada empieza con un renglón que tiene un entero *n* (3 ≤ n ≤ 200): el número de vértices del polígono. Después siguen *n* renglones, cada uno con dos enteros *x*, *y* (\|x\|, \|y\| ≤ 10⁶): las coordenadas (x, y) de los vértices, en sentido antihorario.

- El polígono es **simple**: sus vértices son distintos y dos lados no se cruzan ni se tocan, salvo los lados consecutivos, que se tocan en su vértice común.
- Dos lados consecutivos **nunca son colineales**.

**Salida**

Mostrar la longitud del segmento de recta más largo que cabe dentro del polígono, con un error absoluto o relativo no mayor que 10⁻⁶.

---

## Conceptos clave

### Fórmulas y métodos para la resolución del problema

| ENG | ESP | Definición |
| --- | --- | ---------- |
| cross product | producto cruz | dados A = (x₁, y₁), B = (x₂, y₂) y P = (x₃, y₃): (x₂ − x₁)(y₃ − y₁) − (y₂ − y₁)(x₃ − x₁); positivo: de A a B y luego a P se gira en sentido antihorario; negativo: en sentido horario; cero: colineales |
| crossing test | prueba de cruce | dados la recta que pasa por A y B, y un lado del polígono con extremos C y D: se calcula el producto cruz con P = C y luego con P = D; signos opuestos: el lado cruza la recta; mismo signo: no la cruza |
| distance formula | fórmula de la distancia | distancia entre (x₁, y₁) y (x₂, y₂): d = √((x₂ − x₁)² + (y₂ − y₁)²) |
| parametric form | forma paramétrica | describe cada punto de la recta AB con un solo número t: (x₁ + t(x₂ − x₁), y₁ + t(y₂ − y₁)); t = 0 en A, t = 1 en B; sirve para ubicar dónde un lado choca con la recta y hasta dónde se puede extender la pista |
| ray casting | *ray casting* | determina si un punto está dentro de un polígono: se traza un rayo desde él y se cuentan los lados que cruza; impar: dentro, par: fuera; se usa con el punto medio de AB para saber si la pista está dentro |

### Vocabulario adicional

| ENG | ESP | Definición |
| --- | --- | ---------- |
| absolute value (\|x\|) | valor absoluto | Distancia de un número al cero, sin importar su signo. Ej.: \|−5\| = 5 y \|5\| = 5. |
| collinear | colineal(es) | que están sobre la misma recta |
| coordinates | coordenadas | par (x, y) que ubica un punto en el plano |
| convex | convexo | sin entrantes; todos sus vértices apuntan hacia afuera |
| not convex | no convexo | tiene al menos un entrante (un vértice que apunta hacia adentro) |
| counter-clockwise | sentido antihorario | contrario al giro de las manecillas del reloj |
| edge | lado | segmento que une dos vértices consecutivos |
| intersect | intersecarse / cortarse | cruzarse en al menos un punto |
| polygon | polígono | figura plana cerrada formada por segmentos de recta |
| simple polygon | polígono simple | polígono cuyos lados no se cruzan ni se tocan, salvo en vértices consecutivos |
| vertex, vertices | vértice, vértices | punto donde se unen dos lados consecutivos |

---

## Panorama del código

### Funciones de geometría

Las funciones de este paso son las herramientas para estudiar una sola recta AB. Cada una responde una pregunta sencilla sobre puntos, rectas y lados. Empezamos con la función `cross`, porque es la base de las demás funciones: con ella se encuentran los puntos donde el borde toca la recta, que son los únicos lugares donde la recta puede salir del polígono.

- `cross(A, B, P)`: ¿de qué lado de la recta AB está P? (izquierda, derecha o sobre ella). 

```
¿De qué lado de AB está P?            │  ¿El lado CD cruza AB?
                                      │
        • P  positivo (izquierda)     │         • C  positivo
                                      │          \
- - A ──────────•────────── B - -     │  - - A ───\──────────── B - -
                P  cero               │            \
                                      │             • D  negativo
        • P  negativo (derecha)       │
                                      │  Signos opuestos: CD cruza AB
```

Para saber dónde la recta AB podría salir del polígono, hay que encontrar los puntos donde los lados la cortan. Esto se hace con dos funciones:

- `crosses(A, B, C, D)`: ¿el lado CD cruza la recta AB? Sí, si C y D quedan en lados opuestos
- `crossing_t(A, B, C, D)`: ¿en qué punto de la recta AB choca el lado CD? Lo da como un número t

Los puntos de corte dividen la recta en pedazos. Para saber si un pedazo está dentro del polígono, basta probar un solo punto: su punto medio, que llamamos P. 

```
            t1 = 0.2      P (t = 0.5)      t2 = 0.8
  A─────────────•──────────────○──────────────•──────────B
  t = 0         └───────── un pedazo ─────────┘         t = 1
```

Se usan estas funciones:

- `piece_inside(A, B, t1, t2)`: ¿el pedazo de la recta entre t1 y t2 está dentro? Calcula el t del punto medio, (t1 + t2) / 2, y prueba ese punto P. Basta probar un punto: la recta solo puede pasar de dentro a fuera en un punto de corte, así que entre dos cortes seguidos el pedazo está todo dentro o todo fuera
- `point_at(A, B, t)`: convierte un número t en un punto (x, y) de la recta AB; así se obtiene P a partir de su t
- `inside(P)`: ¿el punto P está dentro del polígono? Usa el *ray casting*: traza un rayo desde P hacia la derecha y cuenta cuántos lados cruza; impar: dentro, par: fuera. Si P está justo sobre el borde, este método puede dar una respuesta equivocada, así que antes revisa cada lado con `on_wall`

```
          ┌─────────┐           ┌──────────┐
          │         │           │          │
  ────────•─────────•───────────•──────────•────────
   fuera  │ dentro  │   fuera   │  dentro  │  fuera
          │         │           │          │
          └─────────┘           └──────────┘
        corte     corte       corte      corte
```

- `on_wall(C, D, P)`: ¿el punto P está sobre el lado CD? Esto pasa cuando el segmento corre a lo largo de un lado; en ese caso, P cuenta como dentro. Para saberlo, revisa dos cosas: que `cross(C, D, P)` sea casi cero (P está sobre la recta CD) y que P esté entre C y D

### Probar cada recta que pasa por dos vértices

En esta parte del código, usamos las funciones de geometría de la sección anterior con cada recta que pasa por dos vértices, para quedarnos con el segmento más largo y dar la respuesta del problema.

Idea clave: el segmento más largo siempre toca dos vértices. Si no, se podría mover o girar hasta hacerlo más largo. Por eso basta probar la recta de cada par de vértices A, B.

Para cada par de vértices:

**1.** Encontrar todos los puntos donde el borde toca la recta AB y guardarlos en la lista `ts`, cada uno como un número t. Hay dos casos:

- un vértice V que está justo sobre la recta: el producto cruz da cero, `cross(A, B, V) == 0`. A y B también son vértices sobre la recta, así que sus posiciones siempre están en `ts`: t = 0 para A (donde la recta empieza) y t = 1 para B (donde termina)
- un lado CD que cruza la recta: `crosses(A, B, C, D)` dice si lo cruza, y `crossing_t(A, B, C, D)` da su t

**2.** Ordenar `ts` de menor a mayor con `ts.sort()`. En el paso 3.1 los t se encontraron en el orden en que revisamos los vértices y los lados, no en el orden en que aparecen sobre la recta. Al ordenarlos, dos t seguidos en la lista son dos cortes vecinos sobre la recta, y el tramo entre ellos es un pedazo. Después, `ts.index(0.0)` y `ts.index(1.0)` dan la posición de A y de B en la lista; se guardan en `start` y `end`.

**3.** Revisar con `piece_inside` cada pedazo entre A y B, desde `start` hasta `end`. Si alguno está fuera, el segmento AB sale del polígono, así que este par no sirve y el código pasa al siguiente par con `continue`.

**4.** Después del paso anterior, sabemos que el segmento de A a B está dentro del polígono, ero quizás el segmento puede seguir más allá de A or más allá de B, todavía dentro del polígono. Por eso, en este paso, revisamos hasta dónde puede llegar hacia atrás, un pedazo a la vez.

Para A: `lo` es una posición en la lista `ts`. Empieza en la posición de A (`start`) y se mueve a la izquierda mientras el pedazo anterior esté dentro.

Para B: `hi` también es una posición en la lista `ts`. Empieza en la posición de B (`end`) y se mueve a la derecha mientras el pedazo siguiente esté dentro.

Al final, el segmento va de `ts[lo]` a `ts[hi]`.

**5.** Calcular la longitud del segmento. El segmento va de `ts[lo]` a `ts[hi]`. La resta `ts[hi] − ts[lo]` compara el segmento con AB: si da 1.7, el segmento es 1.7 veces más largo que AB. 

- De t = 0 a t = 1: la diferencia es 1, y la distancia es exactamente AB.
- De t = 0 a t = 2: la diferencia es 2, y la distancia es dos veces AB, una después de la otra.
- Entonces, una diferencia de 1.7 es un AB completo más 0.7 de otro AB: 1.7 veces AB.

Por eso, la longitud real es `(ts[hi] − ts[lo]) × ab_length`, donde `ab_length` es la distancia de A a B (fórmula de la distancia). Si es mayor que `best`, se guarda en `best`.

Al terminar de probar todos los pares de vértices, `best` tiene la longitud del segmento más largo, y el código la imprime.

---

## Análisis del código

- **Construcción del algoritmo:**
  1. Leer `n` y la lista `vertices`.
  2. Definir las funciones de geometría: dónde corta el borde una recta (`cross`, `crosses`, `crossing_t`) y qué pedazos quedan dentro (`piece_inside`, `point_at`, `inside`, `on_wall`).
  3. Para cada par de vértices A, B: encontrar los cortes, ordenarlos, revisar que AB esté dentro, extender el segmento hacia atrás y hacia adelante, y medir su longitud.
  4. Imprimir `best`, la longitud más grande.

- **Variables y tipos de datos:**
  - `int`: `n`, las coordenadas de los vértices y las posiciones en listas (`start`, `end`, `lo`, `hi`). Las coordenadas son enteras, así que `cross` con vértices da un resultado exacto: `cross(A, B, V) == 0` no tiene errores de redondeo.
  - `float`: los valores t, el punto P, `ab_length` y `best`. Salen de divisiones y raíces cuadradas, así que tienen decimales; por eso `on_wall` no pregunta si el resultado es exactamente 0, sino si es casi 0: menor que un margen muy pequeño, `1e-7` (0.0000001).
  - `bool`: `ok` (si AB está dentro) y `result` en `inside` (dentro o fuera; cambia en cada cruce).
  - `str`: solo al leer la entrada, antes de convertirla a `int`.

- **Estructuras de datos:**
  - Tuplas para los puntos `(x, y)`: un punto siempre tiene dos valores que no cambian, y se pueden separar fácil: `x, y = P`.
  - Lista `vertices`: guarda los vértices en orden; con `vertices[(k + 1) % n]` se obtiene el vértice siguiente; l `% n` (residuo) hace que el siguiente del último vértice sea el primero, para cerrar el polígono.
  - Lista `ts`: guarda los cortes de una recta; se puede ordenar con `sort()` y recorrer por posición.
  - No se necesitan diccionarios, conjuntos, colas, montículos ni grafos: no buscamos datos por nombre ni quitamos repetidos, y el polígono no se trata como grafo.

- **Paradigma algorítmico:** fuerza bruta. Hay infinitas rectas posibles, pero el segmento más largo siempre toca dos vértices, así que basta probar las rectas que pasan por cada par de vértices: un número finito de candidatas. Se prueban todas y se guarda la mejor.

- **Estilo de programación:** imperativo/procedural, con funciones pequeñas. Cada función responde una sola pregunta de geometría, así que es fácil revisarlas y explicarlas una por una.

- **Iterativo o recursivo:** iterativo. Todo se hace con ciclos `for` y `while`. No hay árboles ni grafos, así que la recursión no ayuda, y lo iterativo usa menos memoria.

- **Complejidad:**
  - Temporal: hay O(n²) pares de vértices. Para cada par, encontrar los cortes es O(n) y ordenarlos es O(n log n). Revisar los pedazos es lo más costoso: puede haber O(n) pedazos y cada `inside` revisa los n lados, O(n²). En total, O(n⁴) en el peor caso. En la práctica es mucho menos: el paso 3 se detiene en el primer pedazo fuera, y la mayoría de las rectas tienen pocos cortes.
  - Espacial: O(n). Solo se guardan `vertices` y `ts`, y cada una tiene a lo más del orden de n elementos.

[Ver el código completo en GitHub](https://github.com/locessentials/python/blob/main/unidad4/1-icpc-2017/a.py)