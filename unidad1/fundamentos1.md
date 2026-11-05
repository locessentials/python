---
layout: default
title: Tipos de datos y variables
parent: 1. Cheat Sheets
nav_order: 1
---

# Cheat Sheet 1: tipos de datos y variables

## ¿Qué es un tipo?

En Python, todo valor tiene un **tipo**: una categoría que determina qué contiene el valor y qué operaciones son válidas sobre él. Dos `int` se pueden sumar; dos `str` se pueden concatenar; una `list` acepta `.append()`, mientras un `int` no. Cada valor pertenece exactamente a un tipo, y ese tipo se puede consultar con `type()`:

```python
type(5)        # <class 'int'>
type(5.0)      # <class 'float'>
type("hola")   # <class 'str'>
```

Los tipos que se usan en este curso son pocos: `int`, `float`, `str`, `bool`, `list`, `dict`, `tuple` y los tipos definidos por el programador con `class` (este wiki cubre las clases en más detalle en **Cheat Sheet 7: clases y objetos** de esta unidad).

## Tipos básicos

```python
y = 5         # int (número entero)
z = 5.0       # float (número con punto decimal)
```

## Valores especiales de `float`

- `float("inf")`: infinito positivo; cualquier número real es menor que él.
- `float("-inf")`: infinito negativo; cualquier número real es mayor que él.

## f-strings

```python
print(f"{lo:.9f}")
```

`f"..."` permite insertar una variable dentro de `{ }` y Python la reemplaza por su valor.

En el ejemplo, `:.9f` indica que la variable se imprima con 9 decimales en notación decimal (en lugar de notación científica, por ejemplo).