---
layout: default
title: Fibonacci
parent: Programación dinámica
grandparent: 3. Matemáticas y algoritmos
nav_order: 1
---

# Fibonacci

La sucesión de Fibonacci empieza con F₀ = 0 y F₁ = 1, y cada término siguiente es la suma de los dos anteriores. Es uno de los ejemplos clásicos para ver cómo el trabajo repetido aparece en la recursión, cómo la programación dinámica lo evita y cuándo una fórmula matemática directa resulta más conveniente.

---

## Fundamentos matemáticos: de la recurrencia a la fórmula cerrada

Empezamos primero con la relación de recurrencia y luego cómo obtener una fórmula cerrada a partir de ella. Ver el puente entre ambos ayuda a entender de dónde salen los números 1.618… y −0.618… (asociados con la proporción áurea (o *golden ratio* en inglés), φ).

### 1. Relación de recurrencia y valores iniciales

F₀ = 0, F₁ = 1

Fₙ₊₂ = Fₙ₊₁ + Fₙ (para n ≥ 0)

| n | f_n |
|---|-----|
| 0 | 0  |
| 1 | 1  |
| 2 | 1  |
| 3 | 2  |
| 4 | 3  |
| 5 | 5  |
| 6 | 8  |
| 7 | 13 |
| 8 | 21 |

### 2. Por qué se repiten cálculos y cómo crece el trabajo

Si calculamos F₇ dividiendo el problema en subproblemas más pequeños de forma directa, aparecen las mismas llamadas varias veces (por ejemplo, F₅ y F₂):

```text
                      f_7
                 /           \
          f_5                     f_6
        /     \                 /     \
    f_3         f_4         f_4         f_5
   /   \       /   \       /   \       /   \
 f_1   f_2   f_2   f_3   f_2   f_3   f_3   f_4
```

En una recursión sin guardar resultados, el árbol crece de forma exponencial (del orden de 2^(n/2) a φⁿ, donde φ ≈ 1.61803).

### 3. Ecuación característica y proporción áurea (¿por qué importa?)

Para encontrar una fórmula cerrada sin sumar paso por paso, se supone una solución de la forma Fₙ = rⁿ y se sustituye en la recurrencia:

Fₙ₊₂ − Fₙ₊₁ − Fₙ = 0

rⁿ⁺² − rⁿ⁺¹ − rⁿ = 0

rⁿ · r² − rⁿ · r − rⁿ = 0  ⇒  rⁿ(r² − r − 1) = 0

Descartando la solución trivial r = 0, queda la ecuación cuadrática r² − r − 1 = 0. Aplicando la fórmula general para ax² + bx + c = 0:

x = (−b ± √(b² − 4ac)) / (2a)

Con a = 1, b = −1 y c = −1, las raíces son:

φ = (1 + √5) / 2 ≈ 1.61803,    φ̂ = (1 − √5) / 2 ≈ −0.61803

Combinando estas raíces con las condiciones iniciales (F₀ = 0, F₁ = 1) se obtiene la **fórmula de Binet**:

Fₙ = (φⁿ − φ̂ⁿ) / √5

**¿Por qué es relevante esta matemática aquí?**

- Muestra el ritmo real de crecimiento exponencial de Fibonacci a través de φ ≈ 1.61803
- Demuestra que, cuando existe una fórmula cerrada exacta, podemos calcular Fₙ en tiempo O(1) sin recurrencia ni tabla de programación dinámica—un contraste útil frente a problemas como el triángulo de Pascal o la mochila, donde no hay un atajo cerrado tan simple y la programación dinámica aporta una mejora clara

---

## Panorama del código

### Versión 1: Recursión ingenua (`fib(n)` sin caché)

Muestra por qué la recursión directa sin guardar resultados tiene complejidad exponencial (O(φⁿ)): vuelve a calcular `fib(k)` muchas veces, igual que ocurre con el trabajo repetido en el triángulo de Pascal.

*(Código de recursión ingenua pendiente de agregar.)*

### Versión 2: Memoización

Aplica programación dinámica descendente (*top-down*): mantiene la idea recursiva, pero guarda los resultados en `t` para que cada subproblema se resuelva una sola vez (O(n) en tiempo y O(n) en espacio).

[Ver el código en GitHub](https://github.com/locessentials/python/blob/main/unidad3/prog-dinamica/fib1.py)

### Versión 3: Tabulación y optimización de espacio

Construye la solución de abajo hacia arriba (*bottom-up*) sin recursión y comprime el arreglo de programación dinámica a solo dos variables (O(n) en tiempo y O(1) en espacio). Es un buen contraste con el triángulo de Pascal, donde una tabla bidimensional usa O(n²) de espacio.

[Ver el código en GitHub](https://github.com/locessentials/python/blob/main/unidad3/prog-dinamica/fib2.py)

### Versión 4: Fórmula de Binet (teoría de números, sin programación dinámica)

Cuando las matemáticas ofrecen una fórmula cerrada, se puede pasar directo a O(1)—a diferencia del triángulo de Pascal, donde calcular una entrada aislada con n! / (k!(n − k)!) sigue involucrando factoriales o productos.

Aunque varios ejemplos siguientes de programación dinámica en esta unidad (como el triángulo de Pascal o el problema de la mochila) ayudan a reducir la complejidad, aquí una fórmula cerrada de teoría de números es la vía más directa. Conviene analizar siempre cuándo usar programación dinámica y cuándo no.

[Ver el código en GitHub](https://github.com/locessentials/python/blob/main/unidad3/prog-dinamica/fib3.py)