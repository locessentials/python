---
layout: default
title: Quicksort
parent: Ordenamiento y búsqueda
grandparent: 3. Matemáticas y algoritmos
nav_order: 1
---

# Quicksort

Quicksort es un algoritmo de ordenamiento de tipo **divide y vencerás**, y uno de los más usados en la práctica porque, en la mayoría de los casos, es muy rápido. La idea es sencilla: se elige un elemento de la lista (el **pivote**), se separan los demás en "menores que el pivote" y "mayores que el pivote", y cada parte se ordena de la misma forma, de manera recursiva.

Aquí se ven dos versiones que solo se diferencian en cómo eligen el pivote: una con **pivote fijo** y otra con **pivote aleatorio**. Esta página compara la complejidad de las dos.

**Entrada:** una lista de números *a*, con *n* elementos.

**Objetivo:** regresar los mismos números ordenados de menor a mayor.

## Prueba

```python
a = [8, 3, 1, 7, 0, 10, 2, 5]
```

**Respuesta esperada:** `[0, 1, 2, 3, 5, 7, 8, 10]`

Las dos versiones deben llegar a esta misma respuesta.

[Ver el código en GitHub](https://github.com/locessentials/python/blob/main/unidad3/ordenamiento-busqueda/qs.py)

---

## Versión 1: pivote fijo

```python
def qsf(a):
    if len(a) <= 1:
        return a
    piv = a[-1]                             # pivote: siempre el último elemento
    men = [x for x in a if x < piv]         # menores que el pivote
    igual = [x for x in a if x == piv]      # iguales al pivote
    may = [x for x in a if x > piv]         # mayores que el pivote

    return qsf(men) + igual + qsf(may)
```

Cada llamada empieza por revisar el **caso base**: una lista vacía o con un solo elemento que ya está ordenada. En este caso, se regresa la lista tal cual, y es  lo que detiene la recursión.

Si la lista tiene dos o más elementos, la función hace cuatro cosas:

1. **Elige el pivote:** en esta versión, siempre el último elemento (`a[-1]`).
2. **Separa la lista en tres grupos:** `men` (menores que el pivote), `igual` (iguales al pivote) y `may` (mayores que el pivote).
3. **Ordena `men` y `may`** llamándose a sí misma con cada uno.
4. **Junta todo:** `men` ordenado + `igual` + `may` ordenado.

`igual` no necesita ordenarse, porque todos sus elementos valen lo mismo. Ahí siempre queda el pivote, y también cualquier valor repetido igual a él. Gracias a `igual`, la lista se hace más pequeña en cada llamada aunque haya números repetidos.

¿Por qué el resultado queda ordenado? Todo lo que está en `men` es menor que el pivote y todo lo que está en `may` es mayor. Así que, una vez que cada grupo está ordenado por dentro, basta con ponerlos uno después del otro.

### Seguimiento de la prueba

**Parte 1: bajando ⬇️** (se divide la lista, todavía no se junta nada)

```
[8, 3, 1, 7, 0, 10, 2, 5]   pivote 5   → men [3, 1, 0, 2] │ igual [5]  │ may [8, 7, 10]
   [3, 1, 0, 2]             pivote 2   → men [1, 0]       │ igual [2]  │ may [3]
      [1, 0]                pivote 0   → men []           │ igual [0]  │ may [1]
   [8, 7, 10]               pivote 10  → men [8, 7]       │ igual [10] │ may []
      [8, 7]                pivote 7   → men []           │ igual [7]  │ may [8]
```

Las listas `[]`, `[1]`, `[3]` y `[8]` ya son caso base: tienen 0 o 1 elementos y se regresan tal cual.

**Parte 2: subiendo ⬆️** (cada llamada junta sus tres grupos y regresa el resultado a quien la llamó)

| Paso | Lista | men ordenado + igual + may ordenado | Resultado |
|:----:|:-----:|:-----------------------------------:|:---------:|
| 1 | `[1, 0]` | `[] + [0] + [1]` | `[0, 1]` |
| 2 | `[3, 1, 0, 2]` | `[0, 1] + [2] + [3]` | `[0, 1, 2, 3]` |
| 3 | `[8, 7]` | `[] + [7] + [8]` | `[7, 8]` |
| 4 | `[8, 7, 10]` | `[7, 8] + [10] + []` | `[7, 8, 10]` |
| 5 | `[8, 3, 1, 7, 0, 10, 2, 5]` | `[0, 1, 2, 3] + [5] + [7, 8, 10]` | 🏁 `[0, 1, 2, 3, 5, 7, 8, 10]` |

Cada llamada solo puede juntar sus grupos después de recibir `men` y `may` ya ordenados. Por eso la lista final se arma al último, de abajo hacia arriba.

### Un pivote bueno y uno malo

Fíjate en dos pivotes del seguimiento:

- **Pivote 5 (bueno):** parte la lista de 8 elementos en un grupo de 4 y uno de 3. Los dos lados quedan de tamaño parecido.
- **Pivote 10 (malo):** en `[8, 7, 10]`, el 10 es el **mayor** de la lista, así que `may` queda vacío y `men` tiene todos los demás. La lista solo se hizo un elemento más pequeña.

La diferencia entre estos dos tipos de pivote es justo lo que determina la complejidad de quicksort.

---

## Versión 2: pivote aleatorio

```python
import random

def qsr(a):
    if len(a) <= 1:
        return a
    piv = random.choice(a)                  # pivote: un elemento al azar
    print(f"Pivot point: {piv}")
    men = [x for x in a if x < piv]
    igual = [x for x in a if x == piv]
    may = [x for x in a if x > piv]

    return qsr(men) + igual + qsr(may)
```

Es **exactamente el mismo algoritmo**. Solo cambia una línea: en vez de tomar siempre el último elemento, `random.choice(a)` elige cualquier elemento de la lista al azar. El `print` es solo para ver qué pivote se eligió en cada llamada.

Como el pivote cambia en cada ejecución, los grupos y los pasos también cambian, pero el resultado final siempre es la misma lista ordenada.

```
Pivot point: 8
Pivot point: 3
Pivot point: 1
Pivot point: 5
[0, 1, 2, 3, 5, 7, 8, 10]
```

---

## Complejidad: pivote fijo vs. pivote aleatorio

### El trabajo de cada nivel

En cada llamada, las tres listas por comprensión recorren la lista completa para armar `men`, `igual` y `may`. Si la lista tiene *k* elementos, eso son unos 3*k* pasos, o sea O(*k*).

Ahora se juntan todas las llamadas que están a la misma profundidad de la recursión (un "nivel"). En la prueba:

- **Nivel 1:** `[8, 3, 1, 7, 0, 10, 2, 5]` → 8 elementos
- **Nivel 2:** `[3, 1, 0, 2]` y `[8, 7, 10]` → 4 + 3 = 7 elementos (con 5 como el pivote)
- **Nivel 3:** `[1, 0]`, `[3]` y `[8, 7]` → 2 + 1 + 2 = 5 elementos (con 2 y 10 siendo pivotes)

Las llamadas de un mismo nivel trabajan con pedazos distintos de la lista original, así que entre todas nunca tienen más de *n* elementos. Por eso, **las llamadas de un nivel tardan en total unos 3*n* pasos como máximo: tiempo O(*n*) por nivel**.

El tiempo total es entonces:

> (tiempo por nivel) × (número de niveles) ≈ *n* × (número de niveles)

Y el número de niveles depende de qué tan bien parte la lista el pivote.

### Mejor caso y caso promedio: O(*n* log *n*)

Si el pivote parte la lista más o menos a la mitad, cada nivel tiene listas de la mitad del tamaño que el anterior: *n*, *n*/2, *n*/4… hasta llegar a listas de 1 elemento. Partir *n* a la mitad una y otra vez hasta llegar a 1 toma unos log₂ *n* pasos, así que hay unos log₂ *n* niveles.

> *n* × log *n* = **O(*n* log *n*)**

Con los 8 elementos del ejemplo de clase, eso serían unos 3 niveles (2³ = 8).

### Peor caso: O(*n*²)

Si el pivote siempre es el **menor** o el **mayor** de la lista (como el 10 del seguimiento), uno de los dos grupos queda vacío y el otro tiene todos los demás. Al quitar el pivote, quedan ***n* − 1 elementos por ordenar**: la lista solo se hace un elemento más pequeña en cada llamada.

Con pivote fijo, esto pasa cuando **la lista ya está ordenada**. El último elemento siempre es el mayor:

```
[0, 1, 2, 3, 5, 7, 8, 10]   pivote 10  → men [0, 1, 2, 3, 5, 7, 8] │ may []
[0, 1, 2, 3, 5, 7, 8]       pivote 8   → men [0, 1, 2, 3, 5, 7]    │ may []
[0, 1, 2, 3, 5, 7]          pivote 7   → men [0, 1, 2, 3, 5]       │ may []
[0, 1, 2, 3, 5]             pivote 5   → men [0, 1, 2, 3]          │ may []
[0, 1, 2, 3]                pivote 3   → men [0, 1, 2]             │ may []
[0, 1, 2]                   pivote 2   → men [0, 1]                │ may []
[0, 1]                      pivote 1   → men [0]                   │ may []
```

En vez de 3 niveles, hay 8: uno por elemento. Lo mismo pasa con una lista ordenada al revés (el último elemento siempre es el menor).

Cada nivel recorre una lista un elemento más corta que el anterior, así que el trabajo total es:

> *n* + (*n* − 1) + (*n* − 2) + … + 2 + 1 = *n*(*n* + 1) / 2 = **O(*n*²)**

### ¿Qué cambia con el pivote aleatorio?

Las dos versiones tienen el mismo mejor caso y el mismo peor caso. La diferencia está en **qué tan fácil es caer en el peor caso**.

- **Pivote fijo:** el peor caso lo provoca una entrada concreta y muy común, una lista que ya está ordenada (o casi). Con esa entrada, el peor caso pasa **siempre**.
- **Pivote aleatorio:** ninguna entrada es mala de forma garantizada, porque el pivote no depende del orden de la lista. Para caer en el peor caso habría que tener la mala suerte de elegir el menor o el mayor en casi todas las llamadas, y eso es muy poco probable. Por eso su tiempo **esperado** es O(*n* log *n*) para cualquier entrada, incluso una lista ya ordenada.

| Versión | Mejor caso | Caso promedio | Peor caso | ¿Cuándo pasa el peor caso? |
|---------|:----------:|:-------------:|:---------:|----------------------------|
| Pivote fijo (`qsf`) | O(*n* log *n*) | O(*n* log *n*) | O(*n*²) | Siempre que la lista ya está ordenada (o al revés) |
| Pivote aleatorio (`qsr`) | O(*n* log *n*) | O(*n* log *n*) esperado | O(*n*²) | Solo por muy mala suerte, con cualquier entrada |

Para darse una idea: con 1,000 elementos, *n*² es 1,000,000, mientras que *n* log₂ *n* es más o menos 10,000. Con un millón de elementos, *n*² es un billón (10¹²), y *n* log₂ *n* son unos 20 millones.

### Un detalle sobre la memoria

Esta versión crea listas nuevas (`men`, `igual`, `may`) en cada llamada, así que usa memoria extra. Las implementaciones que se usan en la práctica ordenan la lista **en su lugar** (*in place*): mueven los elementos dentro de la misma lista en vez de copiarlos. La idea del pivote es la misma, pero el código para separar los grupos es más complicado.

---

## Más práctica

### Ideas para extender el código

- **Contar el trabajo:** agrega un contador de comparaciones y compara `qsf` y `qsr` con una lista desordenada y con una lista ya ordenada de, por ejemplo, 500 elementos.
- **Mediana de tres:** en vez de un pivote al azar, elige la mediana entre el primer elemento, el del medio y el último. Es otra forma común de evitar el peor caso con listas ordenadas.