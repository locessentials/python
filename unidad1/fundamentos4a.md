---
layout: default
title: Listas
parent: Colecciones
grandparent: 1. Cheat Sheets
nav_order: 1
---

# Cheat Sheet 4: colecciones – listas

Una lista es una secuencia **ordenada** y **modificable** de elementos. Se escribe entre corchetes `[]`, con los elementos separados por comas.

## Crear listas

```python
vacia = []                      # lista vacía
nums = [3, 1, 4]                # lista de números
mezcla = [1, "dos", 3.0, True]  # una lista puede mezclar tipos
numeros = list(range(5))        # [0, 1, 2, 3, 4]
letras = list("hola")           # ['h', 'o', 'l', 'a']
```

### Leer una lista desde la entrada

En HackerRank los datos casi siempre llegan como una línea de texto. Esta línea la convierte en una lista de enteros:

```python
# entrada: 3 1 4 1 5
nums = list(map(int, input().split()))
print(nums)                     # [3, 1, 4, 1, 5]
```

`input().split()` separa el texto en una lista de cadenas; `map(int, ...)` convierte cada cadena en entero; `list(...)` junta el resultado en una lista.

## Índices

Cada elemento tiene una posición. Los índices empiezan en 0, y los índices negativos cuentan desde el final:

```python
nums = [10, 20, 30, 40]
nums[0]                         # 10  (primer elemento)
nums[3]                         # 40
nums[-1]                        # 40  (último elemento)
nums[-2]                        # 30  (penúltimo)
nums[4]                         # IndexError: list index out of range
```

---

![Logo de Python en amarillo y rojo]({{ '/imagenes/python-logo.png' | relative_url }}){: .tip-circle }

Recuerda: si una lista tiene `n` elementos, el último índice es `n - 1`, no `n`. Por eso `nums[len(nums)]` siempre da error, y `nums[-1]` siempre es el último.

<span class="clear"></span>

---

## Rebanadas (slicing)

Una rebanada `nums[inicio:fin:paso]` regresa una lista **nueva**. Incluye `inicio` pero **no** incluye `fin`:

```python
nums = [10, 20, 30, 40, 50]
nums[1:3]                       # [20, 30]  (índices 1 y 2)
nums[:2]                        # [10, 20]  (desde el inicio)
nums[2:]                        # [30, 40, 50]  (hasta el final)
nums[::2]                       # [10, 30, 50]  (uno sí, uno no)
nums[::-1]                      # [50, 40, 30, 20, 10]  (invertida)
nums[:]                         # [10, 20, 30, 40, 50]  (copia completa)
nums[1:100]                     # [20, 30, 40, 50]  (las rebanadas no dan error si te pasas)
```

## Modificar elementos

A diferencia de las cadenas y las tuplas, una lista se puede cambiar después de crearla:

```python
nums = [10, 20, 30]
nums[0] = 99                    # cambia un elemento → [99, 20, 30]
nums[1:3] = [7, 8]              # cambia una rebanada → [99, 7, 8]
del nums[0]                     # borra por índice → [7, 8]
```

## Pertenencia

```python
nums = [3, 1, 4]
4 in nums                       # True
7 in nums                       # False
7 not in nums                   # True
```

## Recorrer una lista

```python
frutas = ["mango", "pera", "uva"]

for fruta in frutas:            # solo los elementos
    print(fruta)

for i, fruta in enumerate(frutas):   # índice y elemento
    print(i, fruta)             # 0 mango, 1 pera, 2 uva
```

Usa `enumerate()` cuando necesites el índice; es más claro que `for i in range(len(frutas))`.

## Operadores

```python
[1, 2] + [3, 4]                 # concatena → [1, 2, 3, 4]
[0] * 3                         # repite → [0, 0, 0]
```

## Funciones útiles

Estas son funciones, no métodos: la lista va dentro de los paréntesis.

```python
nums = [3, 1, 4, 1, 5]
len(nums)                       # 5  (número de elementos)
min(nums)                       # 1
max(nums)                       # 5
sum(nums)                       # 14  (solo con números)
sorted(nums)                    # [1, 1, 3, 4, 5]  (lista NUEVA)
sorted(nums, reverse=True)      # [5, 4, 3, 1, 1]
```

## Copiar una lista

`b = a` **no** copia la lista: crea otro nombre para la misma lista. Cualquier cambio en `b` también aparece en `a`:

```python
a = [1, 2, 3]
b = a                           # b y a son la MISMA lista
b.append(4)
print(a)                        # [1, 2, 3, 4]  (¡a también cambió!)

c = a.copy()                    # c es una lista NUEVA (también sirve a[:])
c.append(5)
print(a)                        # [1, 2, 3, 4]  (a no cambió)
print(c)                        # [1, 2, 3, 4, 5]
```

---

![Logo de Python en amarillo y rojo]({{ '/imagenes/python-logo.png' | relative_url }}){: .tip-circle }

Recuerda: `=` nunca copia una lista, solo le pone otro nombre. Para una copia de verdad usa `a.copy()` o `a[:]`.

<span class="clear"></span>

---

## Métodos de listas

Los métodos para agregar, quitar, ordenar e invertir elementos (`append`, `insert`, `remove`, `pop`, `sort`, `reverse`) están en [Cheat Sheet 6: métodos]({{ '/unidad1/fundamentos6.html' | relative_url }}), junto con la diferencia entre `sort()` y `sorted()`.