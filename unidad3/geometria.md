---
layout: default
title: Geometría
parent: 3. Matemáticas y algoritmos
nav_order: 3
---

# Geometría

Herramientas básicas para resolver problemas con puntos, rectas y polígonos. Casi todas salen de dos operaciones: el producto cruz y el producto punto.

## Conceptos clave

| ENG | ESP | Definición |
| --- | --- | ---------- |
| quadrant | cuadrante | cada una de las cuatro partes en que los ejes `x` y `y` dividen el plano |
| vertex, vertices | vértice, vértices | punto donde se unen dos lados consecutivos |
| vector | vector | el viaje de un punto a otro: cuánto se mueve en `x` y cuánto en `y`; de `A = (x1, y1)` a `B = (x2, y2)`: `(x2 − x1, y2 − y1)` |
| distance formula | fórmula de la distancia | longitud del segmento entre dos puntos: `√(dx² + dy²)`, donde `dx = x2 − x1` y `dy = y2 − y1` |
| cross product | producto cruz | cálculo que responde la pregunta de la **orientación**; dados `A = (x1, y1)`, `B = (x2, y2)` y `P = (x3, y3)`: `(x2 − x1)(y3 − y1) − (y2 − y1)(x3 − x1)`; positivo: `P` está a la izquierda de `AB`; negativo: a la derecha; cero: sobre la recta |
| orientation | orientación | pregunta que responde el **producto cruz**: al pasar por `A`, `B` y `P`, ¿el giro es antihorario, horario o en línea recta?; es el signo de `cross(A, B, P)`; positivo: antihorario; negativo: horario; cero: en línea recta |
| crossing test | prueba de cruce | el segmento `CD` cruza la recta `AB` si `cross(A, B, C) × cross(A, B, D) < 0`, es decir, si `C` y `D` dan signos opuestos |
| parametric form | forma paramétrica | forma de describir cada punto de la recta `AB` con un solo número `t`: `(x1 + t(x2 − x1)`, `y1 + t(y2 − y1))`; `t = 0` en `A` y `t = 1` en `B` |
| dot product | producto punto | con `A`, `B` y `P` como en el producto cruz: `(x2 − x1)(x3 − x1) + (y2 − y1)(y3 − y1)`; positivo: `AP` va hacia el mismo lado que `AB`; cero: perpendiculares; negativo: lados contrarios |
| ray casting | *ray casting* | forma de saber si un punto está dentro de un polígono: se traza un rayo desde el punto hacia la derecha y se cuentan los lados del polígono que cruza; impar: dentro; par: fuera |
| shoelace formula | fórmula de la lazada | área de un polígono: la suma de `cross(vertices[0], vertices[k], vertices[k + 1])` para cada par de vértices seguidos, dividida entre 2 |
| closest pair of points | pareja de puntos más cercanos | problema de encontrar los dos puntos con la menor distancia entre sí |

---

## Lo básico

### El plano cartesiano

Dos ejes dividen el plano en cuatro cuadrantes. Los signos de `x` y de `y` dicen en qué cuadrante está un punto, sin necesidad de dibujarlo:

- x positivo: a la derecha del eje vertical; x negativo: a la izquierda
- y positivo: arriba del eje horizontal; y negativo: abajo

```
                 y
                 ▲
   Cuadrante II  │  Cuadrante I
   x negativo    │  x positivo
   y positivo    │  y positivo
                 │
  ───────────────┼───────────────▶ x
                 │(0, 0)
   Cuadrante III │  Cuadrante IV
   x negativo    │  x positivo
   y negativo    │  y negativo
                 │
```

Por ejemplo, si todas las coordenadas son positivas, todos los puntos están en el cuadrante I, arriba y a la derecha del origen (0, 0).

### Puntos y vectores

Un punto se guarda como una tupla `(x, y)`. Para usar sus coordenadas, se separan:

```python
A = (2, 3)
x1, y1 = A
```

Un **vector** es el viaje de un punto a otro. De A = (2, 3) a B = (6, 5), el vector AB es (6 − 2, 5 − 3) = (4, 2): avanza 4 en x y 2 en y.

### Rectas y segmentos

Una **recta** sigue sin fin en las dos direcciones; un **segmento** es solo el pedazo de la recta entre dos puntos. En esta página se usan las dos: por ejemplo, un lado puede cruzar la recta AB sin cruzar el segmento AB.

```
  ◀─ ─ ─ A ──────────── B ─ ─ ─▶   recta AB
         A ──────────── B          segmento AB
```

---

## 1. Distancia entre dos puntos

El viaje de A a B forma un triángulo rectángulo: el lado horizontal mide `dx`, el vertical mide `dy`, y la distancia es el lado largo (teorema de Pitágoras).

```
                        • B
                      ╱ │
          distancia ╱   │ dy = y2 − y1
                  ╱     │
              A •───────┘
               dx = x2 − x1
```

```python
def distance(A, B):
    x1, y1 = A
    x2, y2 = B
    dx = x2 - x1
    dy = y2 - y1
    return (dx**2 + dy**2) ** 0.5
```

Para **comparar** distancias no hace falta la raíz: si `dx**2 + dy**2` es más chico, la distancia también. Con coordenadas enteras, así no hay errores de redondeo.

---

## 2. Producto cruz: ¿de qué lado de la recta está un punto?

```python
def cross(A, B, P):
    x1, y1 = A
    x2, y2 = B
    x3, y3 = P
    return (x2 - x1) * (y3 - y1) - (y2 - y1) * (x3 - x1)
```

**Qué mide:** el área del paralelogramo que forman el vector AB y el vector AP, con signo.

```
           P •─────────────────•
            ╱                 ╱
           ╱      área       ╱
          ╱                 ╱
       A •─────────────────• B
```

**Por qué el signo dice el lado:** si caminas de A hacia B,

- P a tu izquierda (giro antihorario de AB hacia AP): el área es **positiva**
- P a tu derecha (giro horario): el área es **negativa**
- P sobre la recta: el paralelogramo queda aplastado, sin área: **cero**

```
         • P  positivo (izquierda)

  - - A ──────────•────────── B - -
                  P  cero

         • P  negativo (derecha)
```

Ejemplo con A = (0, 0) y B = (4, 0), caminando hacia la derecha:

- P = (1, 3): (4)(3) − (0)(1) = 12, positivo: izquierda
- P = (1, −3): (4)(−3) − (0)(1) = −12, negativo: derecha
- P = (2, 0): (4)(0) − (0)(2) = 0: sobre la recta

Con coordenadas enteras, el resultado es entero, así que `cross(A, B, P) == 0` es una prueba exacta.

---

## 3. Prueba de cruce: ¿un segmento cruza una recta?

El segmento CD cruza la recta AB si C y D quedan en lados opuestos: un producto cruz positivo y el otro negativo. Al multiplicarlos, el resultado es negativo.

```
          • C  positivo
           \
  - - A ────\──────────── B - -
             \
              • D  negativo

  Signos opuestos: CD cruza la recta AB
```

```python
def crosses(A, B, C, D):
    return cross(A, B, C) * cross(A, B, D) < 0
```

**Dos segmentos que se cruzan:** no basta con que CD cruce la recta AB, porque la recta sigue más allá de A y de B:

```
                            • C
                            │
       A •──────• B  - - - -│- - -   (la recta AB sigue)
                            │
                            • D

  CD cruza la recta AB, pero no el segmento AB
```

Por eso hay que probar en los dos sentidos: CD cruza la recta AB, **y** AB cruza la recta CD.

```python
def segments_cross(A, B, C, D):
    return crosses(A, B, C, D) and crosses(C, D, A, B)
```

Esta versión no cuenta los casos en que un extremo toca al otro segmento (producto cruz igual a cero); esos casos se revisan aparte si el problema los pide.

---

## 4. Forma paramétrica: un número t para cada punto de la recta

Cada punto de la recta AB se describe con un número t: se empieza en A y se avanza t veces el vector AB.

```
   t = −0.5     t = 0      t = 0.5      t = 1      t = 1.5
  ─────•──────────•───────────•───────────•───────────•─────
                  A                       B
```

- t entre 0 y 1: el punto está entre A y B
- t menor que 0: antes de A
- t mayor que 1: después de B

```python
def point_at(A, B, t):
    x1, y1 = A
    x2, y2 = B
    return (x1 + t * (x2 - x1), y1 + t * (y2 - y1))
```

---

## 5. ¿En qué t corta un segmento a la recta?

Para encontrar el t donde el segmento CD cruza la recta AB, se usa el producto cruz respecto a CD:

- `a = cross(C, D, A)`: el valor en A (t = 0)
- `b = cross(C, D, B)`: el valor en B (t = 1)

Al avanzar de A a B, este valor cambia de forma pareja, en línea recta, de `a` a `b`. El corte está donde el valor llega a cero, porque ahí el punto está sobre la recta CD.

```
  cross(C, D, punto)

     6 •  en A (t = 0)
         ╲
           ╲
     0 ─ ─ ─ ─•─ ─ ─ ─ ─ ─   el valor llega a cero en t = 6 / (6 − (−3)) = 2/3
                 ╲
                   ╲
    −3               •  en B (t = 1)
```

En la posición t, el valor es `a + t * (b − a)`. Para encontrar t, se iguala a cero: t = a / (a − b).

```python
def crossing_t(A, B, C, D):
    a = cross(C, D, A)
    b = cross(C, D, B)
    return a / (a - b)
```

---

## 6. Producto punto: ¿cuánto avanza un punto en la dirección de AB?

```python
def dot(A, B, P):
    x1, y1 = A
    x2, y2 = B
    x3, y3 = P
    return (x2 - x1) * (x3 - x1) + (y2 - y1) * (y3 - y1)
```

Su signo dice la dirección de AP comparada con AB:

- positivo: AP va hacia el mismo lado que AB
- cero: AP es perpendicular a AB (forman un ángulo recto)
- negativo: AP va hacia el lado contrario

**El t de un punto que ya está sobre la recta:** si V está sobre la recta AB, su t es `dot(A, B, V) / dot(A, B, B)`. El denominador, `dot(A, B, B)`, es el cuadrado de la longitud de AB.

```
       A •────────────• V ─────────• B
       t = 0          t = 0.6        t = 1
```

---

## 7. ¿Un punto está dentro de un polígono? (*ray casting*)

Desde el punto, se traza un rayo hacia la derecha y se cuentan los lados que cruza. Cada cruce cambia de dentro a fuera, o de fuera a dentro. Lejos, a la derecha, siempre se está fuera, así que:

- número impar de cruces: el punto está **dentro**
- número par de cruces: el punto está **fuera**

```
   ┌────────┐          ┌────────┐
   │    P •─┼──────────┼────────┼───▶   P: 3 cruces (impar), dentro
   │        │   Q •────┼────────┼───▶   Q: 2 cruces (par), fuera
   │        └──────────┘        │
   └────────────────────────────┘
```

```python
def inside(P, vertices):
    x, y = P
    result = False
    n = len(vertices)
    for k in range(n):
        x1, y1 = vertices[k]
        x2, y2 = vertices[(k + 1) % n]       # % n regresa del último vértice al primero
        if (y1 > y) != (y2 > y):             # un extremo está arriba de P y el otro no
            x_hit = x1 + (y - y1) * (x2 - x1) / (y2 - y1)   # x del lado a la altura de P
            if x_hit > x:                    # el cruce está a la derecha de P
                result = not result
    return result
```

- `(y1 > y) != (y2 > y)`: el lado pasa por la altura de P, así que el rayo lo puede cruzar
- `x_hit`: la x del lado a la altura de P; es la forma paramétrica con t = (y − y1) / (y2 − y1)

Si P puede estar justo sobre el borde, esta prueba puede fallar; en ese caso, primero se revisa si P está sobre algún lado (ver `on_wall` en el problema A de ICPC 2017).

---

## 8. Área de un polígono (fórmula de la lazada)

Se parte el polígono en triángulos desde el primer vértice. Cada triángulo es la mitad de un paralelogramo, así que su área es el producto cruz dividido entre 2.

```
    V3 •───────────• V2
       │         ╱ │
       │  2    ╱   │
       │     ╱  1  │
       │   ╱       │
    V0 •───────────• V1

   triángulo 1: cross(V0, V1, V2) / 2
   triángulo 2: cross(V0, V2, V3) / 2
```

```python
def polygon_area(vertices):
    first = vertices[0]
    total = 0
    for k in range(1, len(vertices) - 1):
        total += cross(first, vertices[k], vertices[k + 1])
    return total / 2
```

- Funciona también con polígonos no convexos: los triángulos que quedan fuera dan área negativa y se restan.
- Si los vértices van en sentido antihorario, el área es positiva; en sentido horario, negativa. Si no se sabe el orden, se usa `abs(polygon_area(vertices))`.

---

## 9. Pareja de puntos más cercanos

Dada una lista de puntos, encontrar la menor distancia entre dos de ellos.

- **Fuerza bruta, O(n²):** probar cada par de puntos y guardar la menor distancia.
- **Divide y vencerás, O(n log n):** ordenar los puntos por x, partir la lista a la mitad, resolver cada mitad, y después revisar solo los puntos cerca de la línea que divide las mitades. Si la menor distancia de las dos mitades es d, una pareja más cercana que cruza la línea solo puede estar en la franja de ancho d a cada lado.

```
     mitad izquierda      │      mitad derecha
                     ┆    │    ┆
       •       •     ┆  • │    ┆      •
           •         ┆    │ •  ┆   •
       •        •    ┆ •  │    ┆         •
                     ┆    │    ┆
                     └─ d ┴ d ─┘
                       franja
```

_Código: por escribir._
