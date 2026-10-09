---
layout: default
title: Funciones
parent: 1. Cheat Sheets
nav_order: 5
has_children: true
---

# Cheat Sheet 5: funciones

Para aprender sobre funciones, empecemos con una que ya viene integrada en Python: `len()`

```python
nums = [1, 2, 3, 4, 5]
print(len(nums))        # 5
```

Las partes:

- **len**: el nombre de la función
- **nums**: el argumento, es decir, lo que le pasas a la función en la llamada para que trabaje con ello (aquí, la lista `[1, 2, 3, 4, 5]`)
- **parámetro**: el nombre de variable que se escribe en la definición de la función y que sirve como marcador de posición para el valor que recibirá cuando la llamen
- **5**: el valor de retorno, es decir, el valor que la función te devuelve

La expresión completa `len(nums)` es una **llamada a una función**: estás llamando a la función `len` y pasándole `nums`. Normalmente tienes que definir una función con `def` antes de poder llamarla, pero las funciones integradas, como `len`, se saltan ese paso porque Python ya las trae definidas.