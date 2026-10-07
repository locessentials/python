---
layout: default
title: Tuplas
parent: Colecciones
grandparent: 1. Cheat Sheets
nav_order: 2
---

# Cheat Sheet 4: colecciones – tuplas

Una tupla es una secuencia **ordenada**, como una lista, pero **inmutable**: una vez creada, no se puede cambiar. Se escribe entre paréntesis `()`.

## Crear tuplas

```python
t = (1, 2, 3)                   # tupla de tres elementos
vacia = ()                      # tupla vacía
uno = (5,)                      # tupla de UN elemento: necesita la coma
no_es_tupla = (5)               # esto es solo el número 5
sin_parentesis = 1, 2, 3        # también es una tupla: (1, 2, 3)
tuple([1, 2, 3])                # de lista a tupla → (1, 2, 3)
tuple("abc")                    # ('a', 'b', 'c')
```

---

![Logo de Python en amarillo y rojo]({{ '/imagenes/python-logo.png' | relative_url }}){: .tip-circle }

Recuerda: lo que crea una tupla es la **coma**, no los paréntesis. Por eso `(5,)` es una tupla y `(5)` no.

<span class="clear"></span>

---

## Lo que funciona igual que en las listas

Todo lo que **lee** una secuencia sin cambiarla funciona con tuplas:

```python
t = (10, 20, 30, 40)
t[0]                            # 10
t[-1]                           # 40
t[1:3]                          # (20, 30)  (una rebanada de tupla es otra tupla)
len(t)                          # 4
20 in t                         # True
min(t), max(t), sum(t)          # (10, 40, 100)
(1, 2) + (3,)                   # (1, 2, 3)
sorted(t, reverse=True)         # [40, 30, 20, 10]  (sorted() siempre regresa una LISTA)

for x in t:
    print(x)
```

## Lo que no se puede hacer: modificar

```python
t = (10, 20, 30)
t[0] = 99                       # TypeError: 'tuple' object does not support item assignment
t.append(40)                    # AttributeError: las tuplas no tienen append()
```

Para "cambiar" una tupla hay que crear una nueva:

```python
t = t + (40,)                   # nueva tupla → (10, 20, 30, 40)

lista = list(t)                 # o convertirla en lista,
lista[0] = 99                   # modificar la lista
t = tuple(lista)                # y convertirla de vuelta → (99, 20, 30, 40)
```

## Métodos de tuplas

Como no se pueden modificar, las tuplas solo tienen dos métodos:

```python
t = (1, 2, 2, 3)
t.count(2)                      # cuántas veces aparece el 2 → 2
t.index(3)                      # posición del primer 3 → 3
t.index(9)                      # ValueError: el 9 no está en la tupla
```

## Desempaquetar

Desempaquetar es asignar cada elemento de una tupla a su propia variable:

```python
punto = (3, 4)
x, y = punto
print(x)                        # 3
print(y)                        # 4

a, b = (1, 2, 3)                # ValueError: too many values to unpack (sobran valores)
```

También funciona dentro de un `for`, algo muy común al recorrer pares:

```python
personas = [("Ana", 20), ("Luis", 22)]
for nombre, edad in personas:
    print(nombre, edad)         # Ana 20, Luis 22
```

`enumerate()` y el método `.items()` de los diccionarios también regresan tuplas, por eso `for i, x in enumerate(lista)` funciona.

## Intercambiar variables

```python
a = 1
b = 2
a, b = b, a                     # del lado derecho se crea la tupla (2, 1) y luego se desempaqueta
print(a, b)                     # 2 1
```

## Regresar varios valores de una función

Cuando una función regresa varios valores separados por comas, en realidad regresa una tupla:

```python
def min_max(nums):
    return min(nums), max(nums)

menor, mayor = min_max([3, 1, 4])
print(menor, mayor)             # 1 4
```

## Tuplas como claves de diccionario

Una tupla puede ser clave de un diccionario porque no cambia; una lista no puede:

```python
lugares = {(0, 0): "origen", (2, 3): "tienda"}
lugares[(2, 3)]                 # "tienda"

{[0, 0]: "origen"}              # TypeError: unhashable type: 'list'
```

## ¿Lista o tupla?

| | **Lista** | **Tupla** |
| --- | --- | --- |
| **Sintaxis** | `[1, 2, 3]` | `(1, 2, 3)` |
| **¿Se puede modificar?** | sí | no |
| **Métodos** | muchos (ver [Cheat Sheet 6]({{ '/unidad1/fundamentos6.html' | relative_url }})) | solo `count()` e `index()` |
| **¿Clave de diccionario?** | no | sí |
| **Cuándo usarla** | datos que van a cambiar: agregar, quitar, ordenar | datos fijos: coordenadas, pares, varios valores de regreso |