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