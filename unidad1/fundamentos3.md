---
layout: default
title: Estructuras de control
parent: 1. Cheat Sheets
nav_order: 3
---

# Cheat Sheet 3: estructuras de control

## Ciclos (o *bucles*, de *loops* en inglés, para repetir código)

### Ciclo `for`

`for` repite el bloque una vez por cada elemento en una **secuencia** o **iterable**.

```python
for <variable> in <iterable>:
    # cuerpo del bucle (código indentado)

# Iterable: cadena
for letra in "hola":
    print(letra)  # "h", "o", "l", "a"

# Iterable: lista
for fruta in ["mango", "pera", "uva"]:
    print(fruta)  # "mango", "pera", "uva"

lista = ["mango", "pera", "uva"]
for fruta in lista:
    print(fruta)

# Iterable: rango
for i in range(3):
    print(i)  # 0, 1, 2
```

También se pueden usar ciclos `for` con tuplas y diccionarios.

### Rango

`range()` es una **función integrada** en Python que se usa con frecuencia en ciclos `for`, y por eso se incluye aquí. Genera una secuencia de números enteros para contar o repetir un número fijo de veces (`range(fin)`, `range(inicio, fin)`, `range(inicio, fin, paso)`). El límite `fin` no se incluye (se detiene justo antes de `fin`; `range(4)` da `0, 1, 2, 3`).

```python
for i in range(4):          # 0, 1, 2, 3
    print(i)

for i in range(1, 5):       # 1, 2, 3, 4 (inicio y fin)
    print(i)

for i in range(0, 10, 2):   # 0, 2, 4, 6, 8 (inicio, fin y paso)
    print(i)
```

### Ciclo `while`

`while` repite el bloque mientras una condición sea verdadera (`True`).

```python
restantes = 3
while restantes > 0:
    print(restantes)        # 3, 2, 1
    restantes -= 1          # actualiza la condición para evitar un bucle infinito
```

Con ciclos `while`, hay que tener cuidado para evitar un ciclo infinito, donde la condición nunca se convierte en falso (`False`).

### Control dentro de ciclos

- **break**: sale del bucle de inmediato.
- **continue**: salta a la siguiente iteración del bucle.

## Condicionales (elegir código, ejecutar una vez)

### `if`/`elif`/`else`

`if`, `elif` y `else` se usan juntos para ejecutar un bloque solo si se cumple una condición. Cada frase representa una **rama** dentro de la cadena `if`/`elif`/`else`.

```python
calificacion = 85

if calificacion >= 90:
    print("Excelente")
elif calificacion >= 70:
    print("Aprobado")       # se ejecuta este bloque
else:
    print("Reprobado")
```