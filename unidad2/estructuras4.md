---
layout: default
title: Listas enlazadas
parent: 2. Estructuras de datos
nav_order: 5
---

# Listas enlazadas (*linked lists*)

Una lista enlazada es una estructura de datos formada por **nodos** que guardan un valor y una referencia al siguiente nodo. A diferencia de una lista normal de Python, los elementos no están guardados uno junto a otro en la memoria: cada nodo "sabe" dónde está el siguiente. Se usa para insertar y borrar elementos sin mover a todos los demás, y para problemas donde hay que recorrer una secuencia de nodos enlazados.

---

## Conceptos básicos

### Definición

Una lista enlazada tiene:

- **nodo:** un par (valor, siguiente). `siguiente` es una referencia al próximo nodo, o `None` si es el último.
- **cabeza (*head*):** el primer nodo de la lista. Si la lista está vacía, la cabeza es `None`.
- **cola (*tail*):** el último nodo. Su `siguiente` es `None`.

Este es el ejemplo que se usa en toda la página. Tiene tres nodos con valores 1, 2 y 3:

```
cabeza
  |
  v
+---+---+    +---+---+    +---+---+
| 1 | *-|--> | 2 | *-|--> | 3 | *-|--> None
+---+---+    +---+---+    +---+---+
```

El asterisco representa el campo `siguiente`. La flecha indica a qué nodo apunta. El último nodo apunta a `None`, que marca el final de la lista.

### Cómo se ve en memoria

En una lista normal de Python, los elementos están en posiciones consecutivas: `[1, 2, 3]` ocupa tres casillas seguidas. En una lista enlazada, **cada nodo puede estar en cualquier parte de la memoria**; lo único que los conecta son las referencias `siguiente`.

```
memoria (posiciones arbitrarias):

  pos 100:  +---+---+
            | 2 | *-|--+
            +---+---+  |
                       |
  pos 250:  +---+---+  |
            | 3 | *-|--|---> None
            +---+---+  |
                       |
  pos 400:  +---+---+  |
            | 1 | *-|--+
            +---+---+
              ^
              |
            cabeza
```

Por eso no se puede "saltar" al nodo k directamente: hay que empezar en la cabeza y seguir las flechas. Esa es la diferencia clave con una lista normal, donde `lista[k]` es instantáneo.

### Tipos de listas enlazadas

- **Simple:** cada nodo apunta solo al siguiente. Es la que se usa en esta página.
- **Doble:** cada nodo apunta al siguiente y al anterior. Permite recorrer en ambos sentidos, pero ocupa más memoria.
- **Circular:** el último nodo apunta de vuelta a la cabeza. No hay `None` al final.

En los problemas de este curso casi siempre es **simple**. Las otras dos aparecen en problemas específicos, y se mencionan cuando hace falta.

### Vocabulario

Estos son los términos que aparecen en las descripciones de los problemas:

- **recorrer:** visitar los nodos uno por uno, empezando en la cabeza y siguiendo `siguiente` hasta llegar a `None`.
- **insertar al inicio:** crear un nodo nuevo y hacer que su `siguiente` sea la cabeza actual; el nodo nuevo pasa a ser la cabeza. Es O(1).
- **insertar al final:** recorrer hasta el último nodo y enlazar el nuevo después. Es O(n) si no se guarda la cola.
- **borrar un nodo:** cambiar el `siguiente` del nodo anterior para que apunte al siguiente del nodo borrado. Es O(1) si ya se tiene el nodo anterior.
- **invertir:** cambiar todas las flechas para que apunten al revés. La cabeza pasa a ser la cola.
- **ciclo:** una lista en la que algún nodo apunta hacia atrás, de modo que al recorrerla nunca se llega a `None`.
- **puntero rápido y lento (*fast/slow pointers*):** dos referencias que avanzan a distinta velocidad para detectar ciclos o encontrar el nodo del medio.

---

## Operaciones y su costo

| Operación | Costo | Por qué |
|---|---|---|
| Acceder al nodo k | O(k) | Hay que recorrer desde la cabeza |
| Insertar al inicio | O(1) | Solo se cambia la cabeza |
| Insertar al final (sin cola guardada) | O(n) | Hay que llegar al último nodo |
| Borrar el primer nodo | O(1) | Se mueve la cabeza |
| Borrar un nodo dado su anterior | O(1) | Se cambia un `siguiente` |
| Buscar un valor | O(n) | Hay que recorrer la lista |
| Recorrer toda la lista | O(n) | Se visita cada nodo una vez |

Comparado con una lista normal de Python: ahí `lista[k]` es O(1) e insertar al inicio es O(n). La lista enlazada invierte esos costos: acceder es caro, pero insertar y borrar en los extremos es barato. Por eso se elige una u otra según el problema.

---

## En Python

En Python **no hay lista enlazada integrada**. Hay que construirla. Lo normal es definir una clase `Nodo` y guardar la cabeza en una variable.

### La clase Nodo

```python
class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None
```

Un nodo con valor `1` y sin siguiente se crea así:

```python
nodo = Nodo(1)
print(nodo.valor)       # 1
print(nodo.siguiente)   # None
```

### Construir una lista

```python
cabeza = Nodo(1)
cabeza.siguiente = Nodo(2)
cabeza.siguiente.siguiente = Nodo(3)

# cabeza -> 1 -> 2 -> 3 -> None
```

También se puede construir con un ciclo, que es lo que se hace al leer una lista desde la entrada:

```python
valores = [1, 2, 3]
cabeza = None
for v in reversed(valores):        # se construye del final hacia el inicio
    nodo = Nodo(v)
    nodo.siguiente = cabeza
    cabeza = nodo
# cabeza -> 1 -> 2 -> 3 -> None
```

### Recorrer una lista

```python
actual = cabeza
while actual is not None:
    print(actual.valor)            # 1 \n2 \n3
    actual = actual.siguiente
```

La condición es `actual is not None`, no `actual.siguiente is not None`. Si se usa la segunda, el último nodo no se visita. Es el error más común al empezar.

### Imprimir una lista como lista normal

```python
def a_lista(cabeza):
    resultado = []
    actual = cabeza
    while actual is not None:
        resultado.append(actual.valor)
        actual = actual.siguiente
    return resultado

print(a_lista(cabeza))             # [1, 2, 3]
```

Esta función es útil para depurar: convierte la lista enlazada en una lista normal de Python para verla de un vistazo.

---

## Recorrer e invertir paso a paso

Invertir una lista enlazada es el problema clásico de esta estructura. Se necesitan **tres referencias** que avanzan juntas: `anterior`, `actual` y `siguiente`. Al final, `anterior` es la nueva cabeza.

Estos son los pasos con la lista `1 -> 2 -> 3 -> None`.

**Estado inicial:**

```
anterior = None
actual   = 1

None        1 -> 2 -> 3 -> None
 ^          ^
 |          |
anterior   actual
```

**Paso 1:** guardar el siguiente de `actual` para no perder el resto de la lista.

```
siguiente = actual.siguiente      # siguiente = 2
```

**Paso 2:** invertir la flecha de `actual`.

```
actual.siguiente = anterior       # 1 -> None

None <- 1    2 -> 3 -> None
        ^    ^
        |    |
     anterior actual
```

**Paso 3:** avanzar `anterior` y `actual`.

```
anterior = actual                 # anterior = 1
actual   = siguiente              # actual = 2

None <- 1    2 -> 3 -> None
             ^    ^
             |    |
         anterior actual
```

**Paso 4:** repetir con el nodo 2.

```
siguiente = 3
2.siguiente = 1                   # 2 -> 1 -> None
anterior = 2
actual   = 3

None <- 1 <- 2    3 -> None
              ^    ^
              |    |
          anterior actual
```

**Paso 5:** repetir con el nodo 3.

```
siguiente = None
3.siguiente = 2                   # 3 -> 2 -> 1 -> None
anterior = 3
actual   = None

None <- 1 <- 2 <- 3
              ^
              |
          anterior (nueva cabeza)
```

**Paso 6:** el ciclo termina porque `actual` es `None`. Se devuelve `anterior`, que es `3`, la nueva cabeza.

El código completo:

```python
def invertir(cabeza):
    anterior = None
    actual = cabeza
    while actual is not None:
        siguiente = actual.siguiente   # guardar el resto
        actual.siguiente = anterior    # invertir la flecha
        anterior = actual              # avanzar
        actual = siguiente
    return anterior                    # nueva cabeza
```

El orden de las tres líneas dentro del ciclo importa: si se mueve `anterior` antes de guardar `siguiente`, se pierde el resto de la lista.

---

## Patrones de problemas

Estos son los patrones que aparecen una y otra vez. Cada uno tiene un ejemplo en los problemas de HackerRank al final de la página.

- **Invertir:** el de arriba. Tres referencias, orden fijo de las líneas.
- **Detectar ciclo (puntero rápido y lento):** dos referencias, una avanza un nodo y la otra dos. Si hay ciclo, se encuentran; si no, la rápida llega a `None`.
- **Encontrar el nodo del medio:** el mismo par de punteros. Cuando la rápida llega al final, la lenta está en el medio.
- **Fusionar dos listas ordenadas:** una referencia a cada lista, se elige el menor y se avanza esa. Al final se enlaza el resto de la que no se acabó.
- **Borrar un nodo dado:** se necesita el anterior. Se cambia `anterior.siguiente = actual.siguiente`.

---

## Trampas

- **Perder el resto de la lista:** al invertir o borrar, si se cambia `actual.siguiente` sin haber guardado antes `siguiente = actual.siguiente`, se pierde el resto. Es el mismo problema que `b = a` en "Copiar una lista" (Cheat Sheet 4: listas), pero con referencias.
- **`while actual:` vs `while actual.siguiente:`:** la primera visita todos los nodos; la segunda se salta el último. Casi siempre se quiere la primera.
- **Lista vacía:** si la cabeza es `None`, cualquier recorrido debe terminar de inmediato. Conviene probar el código con `cabeza = None` antes de entregarlo.
- **Un solo nodo:** invertir o borrar con un solo nodo es un caso aparte. Conviene probarlo también.
- **Modificar la cabeza:** si se inserta al inicio, hay que actualizar la variable `cabeza` fuera de la función, o devolver la nueva cabeza. Si no, la lista "desaparece" desde el punto de vista de quien la llamó.

---

## Problemas para practicar

En HackerRank, sección **Data Structures → Linked Lists**:

- *Print the Elements of a Linked List* — recorrer.
- *Insert a Node at the Tail of a Linked List* — insertar al final.
- *Insert a node at a specific position in a linked list* — insertar en medio.
- *Delete a Node* — borrar dado el valor.
- *Reverse a linked list* — el patrón de invertir.
- *Cycle Detection* — puntero rápido y lento.
- *Find Merge Point of Two Lists* — recorrer dos listas a la vez.
- *Merge two sorted linked lists* — fusionar.

---

## Para leer más

- Luis E. Vargas Azcona, [*Problemas y Algoritmos*](https://omegaup.com/docs/assets/libroluisvargas.pdf), sección de listas enlazadas (libro de la Olimpiada Mexicana de Informática).
```