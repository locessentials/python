---
layout: default
title: Problema F
grandparent: 4. Problemas
parent: ICPC 2017
nav_order: 6
---

# ICPC 2017 - Problema F: 

## Problema
- Entrada: **d** intensidades de rojo distintas, en orden creciente (**r** = intensidad, **p** = número de píxeles con esa intensidad), y **k** = número de valores permitidos en la imagen posterizada
- Cada canal de color de un píxel (rojo, verde y azul) es un entero entre 0 y 255; el problema solo usa el rojo. Entonces, elegir k valores enteros dentro de ese rango (no tienen que estar en la entrada); cada píxel se cambia al valor permitido más cercano
- Error de cada píxel: (r − v)², donde **v** es su nuevo valor; elevar al cuadrado quita el signo y castiga más los errores grandes
- Salida: la suma mínima de los errores de todos los píxeles, es decir, la imagen posterizada más parecida a la original
- Si k = d, cada intensidad conserva su valor y la respuesta es 0
- Ej. 1: 20,000 píxeles en 50 y 10,000 en 150, k = 1 → promedio ponderado 83.33, se redondea a 83 → 20,000 × 33² + 10,000 × 67² = 66,670,000
- Reto: elegir cada valor permitido vⱼ (j = 1, …, k) y el rango de intensidades que se cambian a ese valor, de modo que la suma total de errores E sea la mínima posible
- Límites: d ≤ 256; k ≤ d; p ≤ 2²⁶

$$
v = \frac{\sum_{i=1}^{d} p_i \cdot r_i}{\sum_{i=1}^{d} p_i}
$$

$$
v = \frac{50 \cdot 20{,}000 + 150 \cdot 10{,}000}{20{,}000 + 10{,}000} = \frac{2{,}500{,}000}{30{,}000} = 83.33
$$

- `E` (`int`): puede llegar a cerca de 2⁵⁰ (256 intensidades × 2²⁶ píxeles × 255²); en Python un `int` no tiene límite, y usamos `int` y no `float` para que el resultado sea exacto