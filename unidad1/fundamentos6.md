---
layout: default
title: Métodos
parent: 1. Cheat Sheets
nav_order: 6
---

# Cheat Sheet 6: métodos

## Métodos integrados

Un método es una función que pertenece a un objeto. Se llama con un punto: `objeto.metodo()`.

Python tiene métodos integrados para cadenas, listas, tuplas, diccionarios y conjuntos. Antes de usarlos, es importante entender una diferencia clave:

- Un método de **cadena** regresa una **nueva** cadena y deja la original sin cambios.
- La mayoría de los métodos que modifican una **lista** cambian la lista misma y regresan `None`.

### Cadenas: hay que capturar el resultado

```python
nombre = "ala"
nombre.upper()            # crea "ALA", pero nada lo captura, así que se pierde
print(nombre)             # ala  (sin cambios)

grito = nombre.upper()    # crea "ALA" y lo guarda en una nueva variable
print(grito)              # ALA
print(nombre)             # ala  (sigue sin cambios)

nombre = nombre.upper()   # crea "ALA" y lo guarda con el mismo nombre
print(nombre)             # ALA
```

#### Más métodos para cadenas

```python
nombre = "  ala marie  "
nombre.title()            # mayúscula al inicio de cada palabra → "  Ala Marie  "
nombre.upper()            # todo en mayúsculas → "  ALA MARIE  "
nombre.lower()            # todo en minúsculas → "  ala marie  "
nombre.swapcase()         # invierte mayúsculas y minúsculas: "  Ala Marie  " → "  aLA mARIE  "
nombre.strip()            # quita espacios de ambos extremos → "ala marie"
nombre.lstrip()           # quita espacios solo a la izquierda → "ala marie  "
nombre.rstrip()           # quita espacios solo a la derecha → "  ala marie"
"ala MARIE".capitalize()  # mayúscula solo en el primer carácter, el resto en minúsculas → "Ala marie"
```

```python
frase = "uno dos tres"
frase.find("dos")         # posición donde empieza la cadena → 4 (o -1 si no existe)
frase.count("o")          # cuántas veces aparece → 2
frase.startswith("uno")   # Verdadero o falso → regresa True
frase.endswith("tres")    # Verdadero o falso → regresa True
"123".isdigit()           # Verdadero o falso → regresa True: solo dígitos
"abc".isalpha()           # Verdadero o falso → regresa True: solo letras
frase.split()             # separa en una lista → ["uno", "dos", "tres"]
"-".join(["a", "b", "c"]) # une una lista con un separador → "a-b-c"
frase.replace("dos", "2") # reemplaza texto → "uno 2 tres"
```

---

![Logo de Python en amarillo y rojo](/imagenes/python-logo.png){: .tip-circle }

Recuerda: los métodos de cadena regresan una cadena NUEVA; `nombre` no cambia a menos que la reasignes:
`nombre = nombre.strip()`

<span class="clear"></span>

---

### Listas: no hay que asignar el resultado

Un método que modifica una lista la cambia directamente, así que no hace falta asignar nada:

```python
nums = [3, 1, 2]
nums.sort()               # la lista ahora es [1, 2, 3]
print(nums)               # [1, 2, 3]
```

Si asignamos el resultado a la misma variable, perdemos la lista, porque `.sort()` regresa `None`:

```python
nums = [3, 1, 2]
nums = nums.sort()        # ordena la lista, pero luego nums apunta a None
print(nums)               # None
```

Lo mismo pasa si asignamos el resultado a otra variable: la lista sí se ordena, pero la nueva variable recibe `None`:

```python
nums = [3, 1, 2]
ordenada = nums.sort()
print(nums)        # [1, 2, 3]
print(ordenada)    # None
```

Si queremos una nueva lista ordenada sin cambiar la original, usamos la función `sorted()`, que sí regresa una lista nueva:

```python
nums = [3, 1, 2]
ordenada = sorted(nums)   # crea y regresa una nueva lista ordenada
print(ordenada)           # [1, 2, 3]
print(nums)               # [3, 1, 2]  (sin cambios)
```

---

![Logo de Python en amarillo y rojo](/imagenes/python-logo.png){: .tip-circle }

#### `sort` vs. `sorted`

- El método `nums.sort()` ordena la lista misma y regresa `None`.
- La función `sorted(nums)` deja la lista igual y regresa una nueva lista ordenada:
  - `ordenada = sorted(nums)` guarda la versión ordenada en otra variable; `nums` no cambia.
  - `nums = sorted(nums)` reemplaza `nums` con la versión ordenada.
- Cómo recordarlo: *sort* es un verbo (una orden: "ordena esta lista"); *sorted* es un adjetivo ("una versión ordenada").

<span class="clear"></span>

---

#### Más métodos para listas

```python
nums = [3, 1, 4]
nums.append(5)            # agrega al final → [3, 1, 4, 5]
nums.insert(0, 9)         # inserta en el índice 0 → [9, 3, 1, 4, 5]
nums.remove(4)            # quita la primera aparición del VALOR 4 → [9, 3, 1, 5]
nums.pop()                # quita y regresa el último elemento (5) → [9, 3, 1]
nums.pop(0)               # quita y regresa el elemento en el índice 0 (9) → [3, 1]
nums.sort()               # ordena de menor a mayor, regresa None → [1, 3]
nums.reverse()            # invierte el orden, regresa None → [3, 1]
```

---

![Logo de Python en amarillo y rojo](/imagenes/python-logo.png){: .tip-circle }

#### Lo que hay que saber sobre `.pop()`

A diferencia de `.sort()`, `.append()` y casi todos los métodos que modifican una lista, `.pop()` no regresa `None`: cambia la lista **y además** regresa algo útil, el elemento que quitó. Por eso sí tiene sentido guardar su resultado:

```python
nums = [9, 3, 1, 5]
ultimo = nums.pop()       # saca el 5 de la lista y lo regresa
print(ultimo)             # 5          (lo que regresó)
print(nums)               # [9, 3, 1]  (la lista cambió)
```

<span class="clear"></span>

---

### Más métodos

Los métodos que más vamos a usar al principio son los de cadenas y listas. Aun así, aquí van unas notas breves sobre los métodos de tuplas, diccionarios y conjuntos.

#### Tuplas

Las tuplas solo tienen dos métodos, porque no se pueden modificar:

```python
t = (1, 2, 2, 3)
t.count(2)             # cuántas veces aparece el 2 → 2
t.index(3)             # posición del primer 3 → 3
```

#### Diccionarios

```python
edades = {"Ana": 20, "Luis": 22}
edades.keys()          # todas las claves → "Ana", "Luis"
edades.values()        # todos los valores → 20, 22
edades.items()         # pares clave-valor, útiles en ciclos for
edades.get("Ana")      # 20 (regresa None en vez de dar error si la clave no existe)
edades.pop("Luis")     # quita "Luis" del diccionario y regresa 22
```

#### Conjuntos

Los conjuntos tienen los dos tipos de métodos: `.add()` y `.remove()` cambian el conjunto mismo, como en las listas; `.union()` e `.intersection()` regresan un conjunto nuevo, como en las cadenas.

```python
a = {1, 2, 3}
b = {2, 3, 4}
a.add(5)               # agrega al conjunto mismo → {1, 2, 3, 5}
a.remove(1)            # quita del conjunto mismo → {2, 3, 5}
a.union(b)             # regresa un conjunto NUEVO con todo lo de ambos → {2, 3, 4, 5}
a.intersection(b)      # regresa un conjunto NUEVO con lo que está en los dos → {2, 3}
```