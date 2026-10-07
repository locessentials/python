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

A veces los datos llegan como una línea de texto. Esta línea la convierte en una lista de enteros:

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

Nota: dentro de los corchetes para un índice puede ir un número, una variable o una expresión. Python primero calcula su valor y luego lo usa como índice. Si una lista tiene `n` elementos, el último índice es `n - 1`, no `n`. Por eso `nums[len(nums)]` siempre da error, y `nums[-1]` siempre es el último.

<span class="clear"></span>

---

## Rebanadas (slicing)

Una rebanada `nums[inicio:fin:paso]` regresa una lista **nueva**. Incluye `inicio` pero **no** incluye `fin`:

```python
nums = [10, 20, 30, 40, 50]
nums[1:3]                       # [20, 30]  (desde el índice 1 hasta el elemento antes del índice 3)
nums[:2]                        # [10, 20]  (desde el inicio hasta el elemento antes del índice 2)
nums[2:]                        # [30, 40, 50]  (desde el índice 2 hasta el final)
nums[0:4:2]                     # [10, 30]  (paso: de 2 en 2)
nums[::2]                       # [10, 30, 50]  (sin inicio ni fin: toda la lista, uno sí, uno no)
nums[1::2]                      # [20, 40]  (igual que el anterior, pero empezando en el índice 1)
nums[::-1]                      # [50, 40, 30, 20, 10]  (paso negativo: recorre la lista hacia atrás)
nums[4:1:-1]                    # [50, 40, 30]  (del índice 4 hacia atrás, sin incluir el 1)
nums[::-2]                      # [50, 30, 10]  (hacia atrás, uno sí, uno no)
nums[:]                         # [10, 20, 30, 40, 50]  (copia completa)
nums[1:100]                     # [20, 30, 40, 50]  (fin pasa del final)
```

Con paso positivo, un `inicio` vacío significa "desde el índice 0". Con paso negativo, significa "desde el último elemento", por eso `nums[::-1]` invierte la lista.

Una rebanada nunca da error si te pasas del final: toma los elementos que existen. Un índice solo, como `nums[100]`, sí da `IndexError`, porque pide un elemento específico que no existe.

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
    print(fruta)                # mango \npera \n uva

for i, fruta in enumerate(frutas):   # índice y elemento
    print(i, fruta)             # 0 mango \n1 pera \n2 uva
```

Usa `enumerate()` cuando necesites el índice; es más claro que `for i in range(len(frutas))`.

## Operadores

```python
[1, 2] + [3, 4]                 # concatena → [1, 2, 3, 4]
[0] * 3                         # repite → [0, 0, 0]
```

## Funciones útiles

Python tiene funciones integradas que trabajan con listas. En `len(nums)`, `len` es el nombre de la función y `nums`, dentro de los paréntesis, es el argumento: el valor que recibe la función. El argumento puede ser la variable que nombra la lista o la lista escrita directamente: `len(nums)` o `len([3, 1, 4])`. Las funciones se explican en más detalle en [Cheat Sheet 5]({{ '/unidad1/fundamentos5.html' | relative_url }}).

```python
nums = [3, 1, 4, 1, 5]
len(nums)                       # 5  (número de elementos)
sum(nums)                       # 14  (solo con números)
```

### Ordenamiento

```python
sorted(nums)                    # crea [1, 1, 3, 4, 5], pero nada lo captura
print(nums)                     # [3, 1, 4, 1, 5]  (sin cambios)
ordenada = sorted(nums)         # guarda la lista nueva en otra variable
nums = sorted(nums)             # o reemplaza nums con la versión ordenada
sorted(nums, reverse=True)      # [5, 4, 3, 1, 1]  (de mayor a menor)
```

---

![Logo de Python en amarillo y rojo]({{ '/imagenes/python-logo.png' | relative_url }}){: .tip-circle }

Para ordenar la lista misma, sin crear una nueva, se usa el método `nums.sort()`; ver [Cheat Sheet 6]({{ '/unidad1/fundamentos6.html' | relative_url }}).

<span class="clear"></span>

---

### `min()` y `max()`

```python
nums = [3, 1, 4, 1, 5]
min(nums)                       # 1
max(nums)                       # 5
max(3, 7, 2)                    # 7  (también funcionan sin lista)

frutas = ["mango", "pera", "Uva"]
min(frutas)                     # "Uva"  (orden alfabético: las mayúsculas van antes que las minúsculas)
max(frutas, key=len)            # "mango"  (key=len compara por longitud: la palabra más larga)

min([])                         # ValueError: la lista está vacía
min([], default=0)              # 0  (default= evita el error)
min([1, "dos"])                 # TypeError: no se pueden comparar números con cadenas
min(["10", "9"])                # "10"  (compara como texto: "1" va antes que "9")
min([10, 9])                    # 9     (compara como números)
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