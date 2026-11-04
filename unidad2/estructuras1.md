---
layout: default
title: Arreglos
parent: 2. Estructuras de datos
nav_order: 2
---

# Arreglos (*arrays*)

Un arreglo es una estructura de datos que guarda elementos **uno junto a otro en la memoria**, en posiciones consecutivas, y permite acceder a cada uno por su **índice** (su posición) en tiempo constante. Es la estructura más básica y la base de casi todas las demás: las pilas, las colas y las tablas hash se construyen encima de un arreglo.

---

## Definición

Un arreglo tiene:

- **elementos:** los valores guardados, todos del mismo tipo en los lenguajes de tipado estricto (en Python pueden ser de cualquier tipo).
- **índice (*index*):** la posición de un elemento, contada desde 0. El primer elemento está en el índice 0, el segundo en el 1, y así.
- **longitud (*length*):** cuántos elementos hay guardados.

Este es el ejemplo que se usa en toda la página: un arreglo de cinco enteros.

```markdown
índice:    0    1    2    3    4
         +----+----+----+----+----+
valor:   | 10 | 20 | 30 | 40 | 50 |
         +----+----+----+----+----+
```

El elemento en el índice 2 es 30. El último índice siempre es la longitud menos 1: aquí la longitud es 5 y el último índice es 4.

---

## Cómo se ve en memoria

Un arreglo ocupa un **bloque contiguo** de memoria: si el primer elemento está en la posición 100 y cada elemento ocupa 8 bytes, el segundo está en 108, el tercero en 116, y así. Por eso acceder al índice k es instantáneo: la computadora calcula la dirección con una multiplicación y una suma, sin recorrer nada.

```markdown
memoria:

pos 100:  +----+
          | 10 |   índice 0
pos 108:  +----+
          | 20 |   índice 1
pos 116:  +----+
          | 30 |   índice 2
pos 124:  +----+
          | 40 |   índice 3
pos 132:  +----+
          | 50 |   índice 4
          +----+
```

La dirección del elemento en el índice k es `dirección_base + k × tamaño_de_cada_elemento`. Por eso `arreglo[k]` es O(1): no hay que buscar, se calcula.

### Longitud y capacidad

En Python, una lista no guarda solo los elementos: guarda también cuántos caben. La **longitud** es cuántos elementos hay; la **capacidad** es cuántos caben antes de tener que pedir más memoria. Casi siempre la capacidad es mayor que la longitud, para no pedir memoria en cada `append`.

```markdown
lista = [10, 20, 30]

longitud:   3
capacidad:  4   (por ejemplo; depende del intérprete)

+----+----+----+----+
| 10 | 20 | 30 |    |   <- una casilla libre
+----+----+----+----+
  ^              ^
  |              |
elementos     capacidad
```

Cuando la longitud llega a la capacidad y se hace otro `append`, Python pide un bloque más grande (normalmente el doble), copia los elementos y libera el viejo. Esa copia es O(n), pero ocurre cada vez menos seguido: al duplicar la capacidad, el costo total de n `append` es O(n), no O(n²). Por eso se dice que `append` es **O(1) amortizado** (*amortized*): un `append` individual puede ser caro, pero el promedio sobre muchos es constante.

Es el mismo tipo de razonamiento que en la página de complejidad: no se mide un solo caso, se mide el total sobre una secuencia de operaciones.

---

## Operaciones y su costo

| Operación | Costo | Por qué |
|---|---|---|
| Acceder al índice k | O(1) | Se calcula la dirección |
| Modificar el índice k | O(1) | Se calcula la dirección |
| `append(x)` al final | O(1) amortizado | Casi siempre hay capacidad libre |
| `pop()` del final | O(1) | Solo se reduce la longitud |
| `insert(0, x)` al inicio | O(n) | Hay que mover todos los elementos |
| `pop(0)` del inicio | O(n) | Hay que mover todos los elementos |
| `insert(k, x)` en medio | O(n) | Hay que mover la mitad |
| `x in lista` (buscar) | O(n) | Hay que revisar uno por uno |
| `lista[k:j]` (rebanada) | O(j − k) | Se copian los elementos |
| `lista.sort()` | O(n log n) | Ordenamiento por comparación |
| `len(lista)` | O(1) | La longitud está guardada |

La regla práctica: **acceder es barato, insertar o borrar en medio es caro**. Si el problema pide muchas inserciones al inicio, un arreglo es mala elección; para eso están las listas enlazadas o una `deque`. Si el problema pide muchos accesos por índice, el arreglo es la elección correcta.

---

## En Python

En Python el arreglo es el tipo `list`. No hay que importar nada: viene integrado.

### Crear y acceder

```python
lista = [10, 20, 30, 40, 50]

print(lista[0])          # 10
print(lista[2])          # 30
print(lista[-1])         # 50   (el último)
print(lista[-2])         # 40   (el penúltimo)
print(len(lista))        # 5
```

Los índices negativos cuentan desde el final: `-1` es el último, `-2` el penúltimo, y así. Es una comodidad de Python que casi ningún otro lenguaje tiene.

### Modificar

```python
lista[2] = 99
print(lista)             # [10, 20, 99, 40, 50]

lista.append(60)
print(lista)             # [10, 20, 99, 40, 50, 60]

lista.insert(0, 5)
print(lista)             # [5, 10, 20, 99, 40, 50, 60]

ultimo = lista.pop()
print(ultimo)            # 60
print(lista)             # [5, 10, 20, 99, 40, 50]

primero = lista.pop(0)   # O(n): mueve todos los elementos
print(primero)           # 5
```

### Rebanadas (*slices*)

Una rebanada copia una parte del arreglo. `lista[i:j]` toma desde el índice i hasta el j − 1.

```python
lista = [10, 20, 30, 40, 50]

print(lista[1:4])        # [20, 30, 40]
print(lista[:3])         # [10, 20, 30]   (desde el inicio)
print(lista[2:])         # [30, 40, 50]   (hasta el final)
print(lista[::2])        # [10, 30, 50]   (cada dos)
print(lista[::-1])       # [50, 40, 30, 20, 10]   (invertida)
```

La rebanada **crea una lista nueva**. Modificar la rebanada no modifica la original.

### Ordenar: `sort()` vs `sorted()`

```python
lista = [30, 10, 20]

lista.sort()             # ordena en el lugar, modifica la lista
print(lista)             # [10, 20, 30]

otra = sorted([30, 10, 20])   # devuelve una lista nueva, no modifica la original
print(otra)              # [10, 20, 30]
```

`sort()` modifica la lista y devuelve `None`. `sorted()` devuelve una lista nueva. Confundirlos es un error común: `lista = lista.sort()` deja `lista` en `None`.

Para ordenar con un criterio propio se usa `key`:

```python
palabras = ["bbb", "a", "cc"]
palabras.sort(key=len)
print(palabras)          # ['a', 'cc', 'bbb']

pares = [(3, "c"), (1, "a"), (2, "b")]
pares.sort(key=lambda p: p[0])
print(pares)             # [(1, 'a'), (2, 'b'), (3, 'c')]
```

### Comprensiones de listas (*list comprehensions*)

Una forma corta de construir una lista a partir de otra:

```python
numeros = [1, 2, 3, 4, 5]

cuadrados = [n * n for n in numeros]
print(cuadrados)         # [1, 4, 9, 16, 25]

pares = [n for n in numeros if n % 2 == 0]
print(pares)             # [2, 4]
```

Son equivalentes a un ciclo con `append`, pero más cortas. En problemas de examen conviene usarlas solo cuando la lógica es simple; si hay condiciones anidadas, un ciclo normal se lee mejor.

---

## Patrones de problemas

Estos son los patrones que aparecen una y otra vez en problemas de arreglos. Cada uno tiene un ejemplo en la lista de problemas al final.

- **Sumas de prefijos (*prefix sums*):** guardar en `prefijo[k]` la suma de los primeros k elementos. Con eso, la suma de un rango `[i, j)` es `prefijo[j] − prefijo[i]`, en O(1). Se usa para responder muchas consultas de suma sobre el mismo arreglo.
- **Dos punteros (*two pointers*):** dos índices que avanzan desde los extremos o en la misma dirección. Sirve para encontrar pares que suman un valor, para invertir en el lugar, o para recorrer dos arreglos ordenados a la vez.
- **Invertir en el lugar:** intercambiar el primero con el último, el segundo con el penúltimo, y así, hasta la mitad. Es O(n) y no usa memoria extra.
- **Ordenar y recorrer (*sort + sweep*):** ordenar el arreglo y luego recorrerlo una vez para encontrar lo que se busca (el par más cercano, los intervalos que se solapan, etc.). El ordenamiento es O(n log n) y el recorrido O(n).
- **Ventana deslizante (*sliding window*):** mantener una ventana `[i, j)` que se expande y se contrae mientras se recorre el arreglo. Sirve para "la sublista más larga que cumple X" o "la suma máxima de k elementos consecutivos".

---

## Trampas

- **Aliasing:** `b = a` no copia la lista, solo crea otro nombre para la misma lista. Modificar `b` modifica `a`. Para copiar de verdad: `b = a[:]` o `b = a.copy()` o `b = list(a)`. Es el mismo problema que en la página de grafos con `[[0] * (n + 1)] * (n + 1)`.
- **`pop(0)` es O(n):** sacar el primer elemento mueve todos los demás. Si el problema necesita sacar del inicio muchas veces, usa `collections.deque`, que lo hace en O(1).
- **`[[0] * n] * m` no crea m listas distintas:** crea m referencias a la misma lista. Modificar una modifica todas. Lo correcto es `[[0] * n for _ in range(m)]`.
- **Modificar mientras se recorre:** si se recorre una lista con `for x in lista` y se borran elementos dentro del ciclo, el recorrido se salta elementos o falla. Para borrar, recorre una copia (`for x in lista[:]`) o construye una lista nueva.
- **`sort()` devuelve `None`:** `lista = lista.sort()` deja `lista` en `None`. Usa `lista.sort()` sin asignar, o `lista = sorted(lista)`.
- **Índice fuera de rango:** `lista[len(lista)]` falla; el último índice válido es `len(lista) - 1`. Con índices negativos, `lista[-len(lista)]` es válido pero `lista[-len(lista) - 1]` no.
- **Rebanadas fuera de rango no fallan:** `lista[0:100]` no da error, devuelve lo que haya. Es cómodo, pero puede esconder un error de lógica.