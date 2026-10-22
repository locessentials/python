---
layout: default
title: Euclid
parent: Teoría de números
grandparent: 3. Matemáticas y algoritmos
nav_order: s
---

# Euclid

El algoritmo euclid se usa para calcular el máximo común divisor entre dos números. Se puede representar euclid con varias fórmulas:

a = b * q + r  
a = b * cociente (es decir, *quotient*) + residuo (es decir, *remainder*)

## Steps

1. Divide a by b.
    a. If a / b has a remainder 0, return answer a.

| a = 7, b = 1| 7 / 1 returns q = 7, r = 0 | answer = 7 |

    b. If not, 

## Programas

### Euclid iterativo

En el programa iterativo de Euclides, las variables `a` y `b` se actualizan dentro de un ciclo. La variable `residuo` guarda el residuo de `a % b` para que no se pierda cuando `b` cambia.

[Ver el código en Github](https://github.com/locessentials/python/blob/main/unidad3/euclid/iterative.py)

### Euclid recursivo

En el programa recursivo de Euclides, cada llamada a la función euclid recibe nuevos valores para `a` y `b`: el `b` anterior y el residuo de `a % b`.

[Ver el código en Github](https://github.com/locessentials/python/blob/main/unidad3/euclid/recursive.py)

### Euclid recursivo: show your work

Esta versión de Euclides recursivo usa `print` para mostrar su procedimiento: en cada llamada imprime los valores de a y b, el cociente y el residuo.

[Ver el código en Github](https://github.com/locessentials/python/blob/main/unidad3/euclid/showyourwork.py)

### Euclid recursivo: mínimo común múltiplo

Esta versión usa Euclides para encontrar el máximo común divisor y con él calcula el mínimo común múltiplo: a * b // mcd.

[Ver el código en Github](https://github.com/locessentials/python/blob/main/unidad3/euclid/withlcm.py)

## Referencias

[Khan Academy: What is modular arithmetic?](https://www.khanacademy.org/computing/computer-science/cryptography/modarithmetic/a/what-is-modular-arithmetic)  
[Khan Academcy: The Euclidean Algorithm](https://www.khanacademy.org/computing/computer-science/cryptography/modarithmetic/a/the-euclidean-algorithm)
[The Euclidean Algorithm](https://extendedeuclideanalgorithm.com/euclidean.php#video)  
[The Extended Euclidean Algorithm](https://extendedeuclideanalgorithm.com/xea.php)  

