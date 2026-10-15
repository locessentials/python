---
layout: default
title: Problema J
grandparent: 4. Problemas
parent: ICPC 2017
nav_order: 10
---

# ICPC 2017 - Problema J: flujo máximo con dos líquidos

Hay una red de **n** nodos y **p** tuberías. Del nodo 1 sale un **líquido L** y del nodo 2 sale **agua**. Los dos tienen que llegar al **nodo 3**.

- Las tuberías se pueden usar en cualquier dirección, pero los dos líquidos no pueden ir en direcciones contrarias por la misma tubería.
- Cada tubería tiene capacidad **c**. Si pasan **f** litros de L y **w** litros de agua, se tiene que cumplir **v × f + w ≤ c**.
- En los demás nodos, lo que entra de cada líquido tiene que ser igual a lo que sale.

Si **F** es la cantidad de L y **W** la cantidad de agua que llegan al nodo 3, ¿cuál es el valor máximo de **F<sup>a</sup> × W<sup>1 − a</sup>**?

**Salida:** para cada tubería, la cantidad de L y de agua que pasa por ella (negativa si va de k a j), y al final el valor máximo. Error permitido: 0.0001.

**Límites:** 3 ≤ n ≤ 200, 1 ≤ v ≤ 10, 0.01 ≤ a ≤ 0.99, 1 ≤ c ≤ 10

## Ejemplo

| Entrada | Salida |
| ------- | ------ |
| n = 5, p = 5, v = 1.0, a = 0.5<br>tubería 1: 1–2, c = 10<br>tubería 2: 2–3, c = 10<br>tubería 3: 3–4, c = 10<br>tubería 4: 4–5, c = 10<br>tubería 5: 3–5, c = 10 | L = 5, agua = 0<br>L = 5, agua = 5<br>L = 4.2, agua = 3.14159<br>L = 4.2, agua = 3.14159<br>L = −4.2, agua = −3.14159<br>valor máximo: 5 |