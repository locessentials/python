---
layout: default
title: Clases y métodos
parent: 1. Cheat Sheets
nav_order: 6
---

# Cheat Sheet 6: clases y métodos

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
