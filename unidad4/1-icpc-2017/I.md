---
layout: default
title: Problema I
grandparent: 4. Problemas
parent: ICPC 2017
nav_order: 9
---

# ICPC 2017 - Problema I: clausura transitiva (grafos)

- Entrada: m traducciones de letras (a → b, c) y n pares de palabras
- Cada traducción va en una sola dirección, y se pueden encadenar: si a → b y b → c, entonces a puede convertirse en c
- Una letra también puede quedarse igual, sin usar ninguna traducción
- Para cada par, decidir si la primera palabra puede convertirse en la segunda: tienen que tener la misma longitud, y cada letra de la primera tiene que poder convertirse en la letra de la misma posición en la segunda
- Salida: "yes" o "no" para cada par
- Límites: m ≤ 500; n ≤ 50; palabras de 1 a 50 letras, solo de la a a la z

---

## Panorama de la resolución

### Preparación: leer las entradas
- Guardar las traducciones en un diccionario `t`: cada letra es una clave, y su valor es la lista de letras a las que se traduce directamente
- Guardar los pares de palabras en una lista `p`

### Función `find_letters()`
Encuentra todas las letras en las que se puede convertir una letra, con una traducción o con varias seguidas.
1. Empezar con la letra en `found` (porque siempre puede quedarse igual) y en `to_check`
2. Mientras queden letras en `to_check`, sacar una
3. Si tiene traducciones en `t`, revisar cada una: si no está en `found`, agregarla a `found` y a `to_check`, para revisar también sus traducciones
4. Cuando ya no quedan letras por revisar, devolver `found`

### Resolución: revisar cada par de palabras
1. Si las palabras no tienen la misma longitud, imprimir "no"
2. Si tienen la misma longitud, revisar cada posición: usar `find_letters()` con la letra de la primera palabra y ver si la letra de la segunda palabra está en la lista
3. Si todas las posiciones pasan, imprimir "yes"; si alguna falla, imprimir "no"

[Ver el código completo en GitHub](https://github.com/locessentials/python/blob/main/unidad4/1-icpc-2017/i.py)

---

## Análisis del código

- **Construcción del algoritmo:** (1) leer `m`, `n`, las traducciones en `t` y los pares en `p`; (2) para cada par, si las palabras no tienen la misma longitud, imprimir "no"; (3) si la tienen, para cada posición, usar `find_letters()` con la letra de `original` y revisar si la letra de `deciphered` está en `found`; (4) imprimir "yes" si todas las posiciones pasan, y "no" si alguna falla
- **Variables y tipos de datos:** `m`, `n` y `position` son `int`, porque son cantidades y posiciones; las letras (`letter`, `current`, `next`) y las palabras (`original`, `deciphered`) son `str`; `match` es `bool`, porque solo puede ser verdadero o falso
- **Estructuras de datos:** el grafo se guarda como lista de adyacencia (*adjacency list*) en el diccionario `t`: cada letra es una clave y su valor es la lista de letras a las que se traduce, así se encuentran rápido las traducciones de una letra; `p` es una lista de tuplas (`original`, `deciphered`), porque los pares no cambian; en `find_letters()`, `found` guarda las letras encontradas y `to_check` funciona como pila (*stack*), porque `pop()` saca la última letra que entró; `found` podría ser un conjunto (*set*) para revisar más rápido si una letra ya está, pero como solo hay 26 letras, una lista basta
- **Paradigma algorítmico:** búsqueda en grafos (*graph search*): las letras son nodos (*nodes*) y las traducciones son aristas dirigidas (*directed edges*), y desde cada letra se siguen las aristas para encontrar todas las letras en las que se puede convertir (clausura transitiva, *transitive closure*); como `to_check` siempre saca la última letra que entró, es una búsqueda en profundidad (DFS, *depth-first search*): sigue un camino hasta el final antes de probar otro
- **Estilo de programación:** procedural: una función para la búsqueda y un ciclo para revisar los pares, suficiente para un problema con dos pasos
- **Iterativo o recursivo:** iterativo: el `while` con la pila `to_check` hace el mismo trabajo que una DFS recursiva; como un camino tiene como mucho 26 letras, la recursión también funcionaría, pero la versión iterativa es más fácil de seguir paso a paso
- **Complejidad:** temporal O(n × L × m), donde L es el largo de las palabras: para cada par y cada posición se hace una búsqueda que puede recorrer las m traducciones; espacial O(m + n × L), por el diccionario `t` y la lista `p` (`found` y `to_check` tienen como mucho 26 letras); la operación que determina la complejidad es la búsqueda de `find_letters()`, que se repite en cada posición