---
layout: default
title: Integradas
parent: Funciones
grandparent: 1. Cheat Sheets
nav_order: 5
has_children: true
---

# Cheat Sheet 5: funciones integradas

Las funciones integradas vienen con Python, y no hay que definirlas con `def` ni importarlas. La mayoría no es exclusiva de un solo tipo de dato; muchas aceptan cualquier **iterable**, es decir, cualquier cosa que se pueda recorrer elemento por elemento: cadenas, listas, tuplas, conjuntos y diccionarios.

## Entrada y salida

```python
input()    # lee la siguiente línea de entrada y la devuelve como cadena (str)
print()    # muestra en pantalla lo que le pases; acepta cualquier tipo de dato
```

## Conversión de tipos

```python
int()      # convierte a número entero; acepta cadenas ("42") y decimales (3.9 → 3, corta sin redondear)
float()    # convierte a número decimal; acepta cadenas ("1.5") y enteros (2 → 2.0)
list()     # convierte un iterable en lista (modificable, con orden)
tuple()    # convierte un iterable en tupla (no modificable, con orden)
set()      # devuelve un conjunto NUEVO sin duplicados; sin orden y sin índices
```

## Para iterables (cadenas, listas, tuplas, conjuntos, diccionarios)

```python
len()      # número de elementos: len("hola") → 4, len([1, 2]) → 2
sorted()   # devuelve una lista NUEVA ordenada de menor a mayor; el original no cambia
map()      # aplica una función a cada elemento de un iterable
zip()      # empareja elementos de dos o más iterables según su posición:
           # zip([1, 2], ['a', 'b']) → (1, 'a'), (2, 'b')
enumerate()  # da cada elemento junto con su posición: (0, primero), (1, segundo)...
any()        # True si AL MENOS UN elemento es verdadero
all()        # True si TODOS los elementos son verdaderos
```

### Más sobre map()

`map()` acepta cualquier iterable (cadenas, listas, tuplas, conjuntos, `range()`...). Lo que devuelve no es una lista ni una tupla, sino un objeto `map`. Si lo imprimes directamente, solo ves algo como `<map object at 0x...>`, así que para ver el resultado lo conviertes con `list()`, `tuple()` o `set()`.

```python
list(map(float, ['1.5', '2']))          # [1.5, 2.0]
list(map(str, [1, 2, 3]))               # ['1', '2', '3']
list(map(len, ['hi', 'hello']))         # [2, 5]
list(map(str.upper, ['a', 'b']))        # ['A', 'B']

list(map(str.upper, 'hola'))            # ['H', 'O', 'L', 'A']  (cadena)
tuple(map(int, ('4', '5')))             # (4, 5)  (tupla)
list(map(doble, range(3)))              # [0, 2, 4]  (range)

def doble(n):
    return n * 2

list(map(doble, [1, 2, 3]))             # [2, 4, 6]
```

Si la función que recibe el resultado ya acepta iterables, no hace falta convertirlo. Por ejemplo, `" ".join()` toma el objeto `map` directamente:

```python
nums = [1, 2, 3]
print(" ".join(map(str, nums)))         # "1 2 3"
```

### Más sobre any() y all()

- `any()` devuelve `True` si **al menos un** elemento cumple la condición.
- `all()` devuelve `True` si **todos** los elementos la cumplen.

Un uso común es revisar los caracteres de una cadena:

```python
s = input()

print(any(c.isalnum() for c in s))   # ¿hay alguna letra o dígito?
print(any(c.isalpha() for c in s))   # ¿hay alguna letra?
print(any(c.isdigit() for c in s))   # ¿hay algún dígito?
print(any(c.islower() for c in s))   # ¿hay alguna minúscula?
print(any(c.isupper() for c in s))   # ¿hay alguna mayúscula?
```

`c.isalpha() for c in s` revisa cada carácter `c` de `s`, uno por uno, y produce `True` o `False` para cada uno. `any()` recibe esos resultados y te dice si al menos uno fue `True`.

Esta línea:

```python
print(any(c.isalpha() for c in s))
```

equivale a esta versión larga:

```python
encontrado = False
for c in s:              # recorre cada carácter
    if c.isalpha():      # revisa solo ese carácter
        encontrado = True
        break            # any() se detiene en cuanto encuentra un True
print(encontrado)
```

`all()` funciona igual, pero al revés: empieza suponiendo `True` y se detiene en cuanto encuentra un `False`.

```python
print(all(c.isdigit() for c in "2026"))   # True: todos son dígitos
print(all(c.isdigit() for c in "20a6"))   # False: 'a' no es dígito
```

### Más sobre enumerate()

`enumerate()` envuelve un iterable para que, en cada vuelta del ciclo, recibas dos cosas: el número de posición y el elemento en esa posición.

Sin `enumerate()`, un ciclo solo te da los elementos:

```python
frutas = ['manzana', 'pera', 'mango']

for fruta in frutas:
    print(fruta)            # manzana \npera \nmango
```

Con `enumerate()`, cada vuelta te entrega un par: primero el número y luego el elemento.

```python
for i, fruta in enumerate(frutas):
    print(i, fruta)
```

```
0 manzana
1 pera
2 mango
```

**¿Por qué hay dos nombres antes de `in`?** 

En cada vuelta, `enumerate()` produce un par como `(0, 'manzana')`. Al escribir `i, fruta`, el par se separa: la primera parte va a `i` y la segunda a `fruta`. Es el mismo truco que:

```python
a, b = 3, 7      # a recibe 3, b recibe 7
```

Los nombres `i` y `fruta` los eliges tú; `for num, f in enumerate(frutas)` funciona igual.

Es un atajo para esta versión más larga, que hace lo mismo:

```python
for i in range(len(frutas)):
    fruta = frutas[i]
    print(i, fruta)
```

Si quieres que la numeración empiece en 1 en lugar de 0, usa `start`:

```python
for i, fruta in enumerate(frutas, start=1):
    print(i, fruta)    # 1 manzana, 2 pera, 3 mango
```

**¿Cuántos nombres se pueden usar con enumerate()?**

`enumerate()` siempre produce **pares**: la posición y el elemento. Por eso, cuántos nombres pones antes de `in` depende de la forma de lo que estás separando.

**Un nombre** guarda el par completo, como tupla:

```python
for par in enumerate(frutas):
    print(par)             # (0, 'manzana')
```

**Dos nombres** separan cada par:

```python
for i, fruta in enumerate(frutas):
    print(i, fruta)        # 0 manzana
```

**Tres nombres sueltos** dan error, porque cada par solo tiene dos partes:

```python
for i, n, fruta in enumerate(frutas):
    ...
# ValueError: not enough values to unpack (expected 3, got 2)
```

**Tres nombres sí funcionan si el elemento también es un par**, pero necesitas paréntesis para indicar la estructura. Por ejemplo, combinándolo con `zip()`:

```python
nums = [10, 20, 30]
frutas = ['manzana', 'pera', 'mango']

for i, (n, fruta) in enumerate(zip(nums, frutas)):
    print(i, n, fruta)
```

```
0 10 manzana
1 20 pera
2 30 mango
```

En cada vuelta, `enumerate()` entrega algo como `(0, (10, 'manzana'))`: la posición y luego un par que viene de `zip()`. Los paréntesis en `i, (n, fruta)` reflejan esa misma forma.

## Otras

```python
hash()     # devuelve un número entero que funciona como "huella digital" de un valor;
           # valores iguales dan el mismo hash; solo funciona con tipos no modificables
           # (str, int, tuple), no con listas ni diccionarios
```