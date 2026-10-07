---
layout: default
title: Diccionarios
parent: Colecciones
grandparent: 1. Cheat Sheets
nav_order: 4
---

# Cheat Sheet 4: colecciones – diccionarios

## Tuplas como claves

A veces una clave necesita más de un dato. Por ejemplo, una posición en un tablero necesita una fila y una columna. Una tupla junta los dos datos en una sola clave:

```python
tablero = {(0, 0): "X", (1, 2): "O"}
tablero[(1, 2)]                 # "O"  (lo que hay en la fila 1, columna 2)
```

Una lista no puede ser clave, porque una lista puede cambiar: si una clave cambiara después de guardarla, el diccionario ya no podría encontrarla. Las tuplas no cambian, así que sí sirven como claves:

```python
{[0, 0]: "X"}                   # TypeError: unhashable type: 'list'  (Python no acepta una lista como clave)
```