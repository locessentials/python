---
layout: default
title: Problema I
grandparent: 4. Problemas
parent: ICPC 2017
nav_order: 9
---

# ICPC 2017 - Problema I: clausura transitiva

## Problema
- Entrada: m traducciones de letras (a → b, c) y n pares de palabras
- Cada traducción va en una sola dirección, y se pueden encadenar: si a → b y b → c, entonces a puede convertirse en c
- Una letra también puede quedarse igual, sin usar ninguna traducción
- Para cada par, decidir si la primera palabra puede convertirse en la segunda: tienen que tener la misma longitud, y cada letra de la primera tiene que poder convertirse en la letra de la misma posición en la segunda
- Salida: "yes" o "no" para cada par
- Límites: m ≤ 500; n ≤ 50; palabras de 1 a 50 letras, solo de la a a la z

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