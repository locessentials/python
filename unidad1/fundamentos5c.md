---
layout: default
title: Lambda
parent: Funciones
grandparent: 1. Cheat Sheets
nav_order: 5
has_children: true
---

# Cheat Sheet 5: funciones lambda

Una lambda es una forma de escribir una función pequeña en una sola línea, sin usar `def`.

**La estructura**

```python
lambda  parameters  :  expression
lambda  parámetros  :  expresión
```

- **lambda** indica "esto es una función".
- Los **parámetros** van antes de los `:`. Puede haber cero, uno o varios, separados por comas.
- La **expresión** va después de los `:`. Su resultado se regresa automáticamente, sin necesidad de la palabra clave `return`.

Por ejemplo, estas dos son idénticas:

```python
cuadrado = lambda x: x * x

def cuadrado(x):
    return x * x
```
## Ejemplos

### Ejemplos básicos

```python
doble = lambda x: x * 2              # un parámetro
suma = lambda a, b: a + b            # dos parámetros
saludo = lambda: "hola"              # sin parámetros

doble(4)       # → 8
suma(3, 5)     # → 8
saludo()       # → "hola"
```

### Ejemplo con `sorted`

Normalmente, `sorted` ordena las cadenas de texto alfabéticamente. Con `key=` puedes cambiar **lo que `sorted` compara**. Le pasas una función, y `sorted`:

1. llama a esa función con cada elemento
2. ordena los elementos según los resultados, en lugar de según los elementos mismos

Con `key=lambda n: len(n)`, los elementos se ordenan por su longitud, en lugar de alfabéticamente.

```python
nombres = ["Sebastián", "Bo", "Ana"]

sorted(nombres)                       # → ['Ana', 'Bo', 'Sebastián']  (alfabético)
sorted(nombres, key=lambda n: len(n)) # → ['Bo', 'Ana', 'Sebastián']  (por longitud)
```

### Ejemplos de transformaciones

Supongamos que escribes una función que procesa una lista y deja que quien la llama elija cómo transformar cada elemento:

```python
def procesar(lista, transformar):
    return [transformar(x) for x in lista]

procesar([1, 2, 3], lambda x: x * 2)    # → [2, 4, 6]
procesar([1, 2, 3], lambda x: x ** 2)   # → [1, 4, 9]
procesar([1, 2, 3], lambda x: x)        # → [1, 2, 3]   ← función identidad, sin cambios

`procesar` necesita una función, así que cuando quieres que los valores se queden igual, le pasas la función identidad.