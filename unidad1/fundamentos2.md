---
layout: default
title: Operadores y expresiones
parent: 1. Cheat Sheets
nav_order: 2
---

# Cheat Sheet 2: operadores y expresiones

## Expresiones

Una expresión es cualquier parte del código que Python evalúa para obtener un valor. Los operadores sirven para combinar valores y formar expresiones más grandes.

| Expresión | Valor |
|---|---|
| `7` | `7` |
| `7 + 3` | `10` |
| `7 > 3` | `True` |
| `"a" in "casa"` | `True` |

## Operadores

### Aritméticos

| Nombre | Representación | Sintaxis |
|---|---|---|
| Suma | `+` | `a + b` |
| Resta | `-` | `a - b` |
| Multiplicación | `*` | `a * b` |
| División | `/` | `a / b` |
| División entera | `//` | `a // b` |
| Módulo (residuo) | `%` | `a % b` |
| Exponenciación | `**` | `a ** b` |

### Comparación

| Nombre | Representación | Sintaxis |
|---|---|---|
| Igual a | `==` | `a == b` |
| Distinto de | `!=` | `a != b` |
| Mayor que | `>` | `a > b` |
| Menor que | `<` | `a < b` |
| Mayor o igual que | `>=` | `a >= b` |
| Menor o igual que | `<=` | `a <= b` |

### Asignación

La asignación no es una expresión: no produce un valor, sino que guarda el valor de una expresión en una variable. Por ejemplo, en `total = precio * 2`, la expresión es `precio * 2`. 

| Nombre | Representación | Sintaxis |
|---|---|---|
| Asignación | `=` | `a = b` |
| Suma y asignación | `+=` | `a += b` |
| Resta y asignación | `-=` | `a -= b` |
| Multiplicación y asignación | `*=` | `a *= b` |
| División y asignación | `/=` | `a /= b` |
| División entera y asignación | `//=` | `a //= b` |
| Módulo y asignación | `%=` | `a %= b` |
| Exponenciación y asignación | `**=` | `a **= b` |

**Nota:** En su documentación oficial, Python llama delimitadores a `=` y sus formas combinadas (como `+=`), no operadores, pero la mayoría de los tutoriales los incluyen entre los operadores.

### Lógicos

| Nombre | Representación | Sintaxis |
|---|---|---|
| Y | `and` | `a and b` |
| O | `or` | `a or b` |
| Negación | `not` | `not a` |

### Pertenencia

| Nombre | Representación | Sintaxis |
|---|---|---|
| Está en | `in` | `a in b` |
| No está en | `not in` | `a not in b` |

### Identidad

| Nombre | Representación | Sintaxis |
|---|---|---|
| Es el mismo objeto | `is` | `a is b` |
| No es el mismo objeto | `is not` | `a is not b` |