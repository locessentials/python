---
layout: default
title: Problema J
grandparent: 4. Problemas
parent: ICPC 2017
nav_order: 10
---

# ICPC 2017 - Problema J: mezclar dos líquidos en una red de tuberías

Hay una red de **n** nodos conectados por **p** tuberías. Por la red se mandan dos líquidos:

- el **líquido L**, que sale del nodo 1
- el **agua**, que sale del nodo 2

Los dos líquidos tienen que llegar al **nodo 3**, donde se mezclan.

## Reglas de la red

- Cada tubería conecta dos nodos **j** y **k** y se puede usar en cualquier dirección.
- Por una misma tubería pueden pasar los dos líquidos, pero **no en direcciones contrarias**.
- Cada tubería tiene una capacidad **c**. El líquido L es más espeso que el agua: cada litro de L ocupa lo mismo que **v** litros de agua. Si por una tubería pasan **f** litros por segundo de L y **w** litros por segundo de agua, se tiene que cumplir:

  **v × f + w ≤ c**

- En cada nodo que no sea el 1, el 2 o el 3, la cantidad de cada líquido que entra tiene que ser igual a la cantidad que sale. En los nodos se pueden separar y reorganizar los líquidos como se quiera.

## Qué se busca

Sea **F** la cantidad de líquido L que llega al nodo 3 y **W** la cantidad de agua que llega al nodo 3 (en litros por segundo). Se quiere que la mezcla tenga la mayor calidad posible, medida con esta fórmula:

**F<sup>a</sup> × W<sup>1 − a</sup>**

donde **a** es un número dado entre 0 y 1.

## Entrada

- Primer renglón: **n**, **p**, **v** y **a**
- Luego **p** renglones, uno por tubería: **j**, **k** y **c** (con j < k)

## Salida

- Para cada tubería, en el mismo orden de la entrada: la cantidad de L y la cantidad de agua que pasan por ella. El número es positivo si el líquido va de j a k y negativo si va de k a j.
- Al final: el valor máximo de F<sup>a</sup> × W<sup>1 − a</sup>.

Si hay varias soluciones, cualquiera es válida. Se acepta un error de hasta 0.0001.

**Límites:** 3 ≤ n ≤ 200, n − 1 ≤ p ≤ n(n − 1)/2, 1 ≤ v ≤ 10, 0.01 ≤ a ≤ 0.99, 1 ≤ c ≤ 10. La red siempre está conectada y no hay dos tuberías entre el mismo par de nodos.

## Ejemplos

| Entrada 1 | Entrada 2 |
| --------- | --------- |
| n = 6, p = 6, v = 3.0, a = 0.66<br>tubería 1: 2–4, c = 8<br>tubería 2: 4–6, c = 1<br>tubería 3: 3–6, c = 1<br>tubería 4: 4–5, c = 5<br>tubería 5: 1–5, c = 7<br>tubería 6: 3–5, c = 3 | n = 5, p = 5, v = 1.0, a = 0.5<br>tubería 1: 1–2, c = 10<br>tubería 2: 2–3, c = 10<br>tubería 3: 3–4, c = 10<br>tubería 4: 4–5, c = 10<br>tubería 5: 3–5, c = 10 |
| **Salida:**<br>tubería 1: L = 0, agua = 1.36<br>tubería 2: L = 0, agua = 1<br>tubería 3: L = 0, agua = −1<br>tubería 4: L = 0, agua = 0.36<br>tubería 5: L = 0.88, agua = 0<br>tubería 6: L = −0.88, agua = −0.36<br>valor máximo: 1.02037965897 | **Salida:**<br>tubería 1: L = 5, agua = 0<br>tubería 2: L = 5, agua = 5<br>tubería 3: L = 4.2, agua = 3.14159<br>tubería 4: L = 4.2, agua = 3.14159<br>tubería 5: L = −4.2, agua = −3.14159<br>valor máximo: 5 |