---
layout: default
title: Problema de la mochila
parent: Programación dinámica
grandparent: 3. Matemáticas y algoritmos
nav_order: 1
---

# El problema de la mochila (*knapsack problem* en inglés)

Este problema se resuelve aquí de tres maneras: con fuerza bruta, con recursividad y con programación dinámica. Las dos primeras se explican brevemente; la mayor parte de la página está dedicada a la versión con programación dinámica.

**Entrada:** el número de objetos *n*, el valor de cada objeto *v*, el peso de cada objeto *p* y la capacidad de la mochila *W* (de *weight* en inglés).

**Objetivo:** encontrar el conjunto de objetos con el mayor valor total posible, sin que su peso total pase de la capacidad *W* de la mochila.

**Límites:** todos los valores son enteros positivos. Esta es la variante **0/1** del problema: cada objeto se toma una sola vez y completo (1), o se deja (0). No se permiten fracciones ni copias repetidas.

## Ejemplo de clase
 
| Objeto | Peso | Valor |
|:------:|:----:|:-----:|
| 0      | 2    | 3     |
| 1      | 3    | 4     |
| 2      | 4    | 5     |
| 3      | 5    | 6     |

```python
p = [2, 3, 4, 5]    # pesos
v = [3, 4, 5, 6]    # valores
W = 5               # capacidad de la mochila
```

**Respuesta esperada:** valor máximo **7**, con los objetos **0 y 1** (peso 2 + 3 = 5, valor 3 + 4 = 7).

Las tres versiones deben llegar a esta misma respuesta.

---

## Versión 1: fuerza bruta

[Ver el código en GitHub](https://github.com/locessentials/python/blob/main/unidad3/prog-dinamica/knapsack.py)

La fuerza bruta revisa **todas** las combinaciones posibles:

1. Genera todos los subconjuntos de objetos (el conjunto potencia). Con 4 objetos hay 2⁴ = 16 subconjuntos.
2. Descarta los que pesan más que *W*.
3. De los que quedan, elige el de mayor valor.
Siempre encuentra la respuesta correcta, porque no se salta ninguna combinación. El problema es que el número de subconjuntos se duplica con cada objeto nuevo: con 30 objetos ya son más de mil millones.

---

## Versión 2: recursiva

[Ver el código en GitHub](https://github.com/locessentials/python/blob/main/unidad3/prog-dinamica/knapsack2.py)

```python
def mochila(p, v, W, n):        # W: capacidad restante de la mochila
                                # n: número de objetos que quedan por considerar
    if n == 0 or W == 0:
        return 0
    if p[n-1] > W:                      # no cabe, saltamos el objeto
        return mochila(p, v, W, n-1)
    nto = mochila(p, v, W, n-1)                     # nto = no tomar objeto
    to = v[n-1] + mochila(p, v, W - p[n-1], n-1)    # to = tomar objeto
    return max(nto, to)
```

La función revisa los objetos del último al primero. La primera llamada considera el objeto 3, que es el cuarto y último objeto (`n = 4` cuenta cuántos objetos quedan, y el último está en la posición `p[n-1]`, o sea `p[3]`), y cada llamada recursiva baja `n` en 1.

Cada llamada empieza por revisar si ya terminó. Ese es el **caso base**: si ya no quedan objetos por considerar (`n == 0`) o ya no queda espacio (`W == 0`), el valor es 0. Es lo que detiene la recursión. 

Mientras no se llegue al caso base, hay **tres casos** para el objeto actual:

1. **No cabe:** el objeto pesa más que el espacio que queda. No hay decisión que tomar; se salta y se resuelve el problema con los objetos restantes.
2. **No tomarlo (`nto`):** se deja el objeto y se busca lo mejor con los objetos restantes y el mismo espacio.
3. **Tomarlo (`to`):** se suma su valor, y se busca lo mejor con los objetos restantes y el espacio que queda después de meterlo (`W - p[n-1]`).

De los casos 2 y 3 se queda con el mayor (`max`).

### Seguimiento del ejemplo de clase
 
**Parte 1: bajando ⬇️** (se hacen preguntas, todavía no se responde nada)
 
```
DECISIÓN A │ Objeto 3 (peso 5, valor 6) │ espacio: 5
           │ TOMAR    → 6 + (espacio 0, ya no cabe nada)
           │ NO TOMAR → ❓ pregunta a DECISIÓN B
DECISIÓN B │ Objeto 2 (peso 4, valor 5) │ espacio: 5      ← la pide NO TOMAR de A
           │ TOMAR    → 5 + ❓ pregunta a DECISIÓN C
           │ NO TOMAR →     ❓ pregunta a DECISIÓN D
DECISIÓN C │ espacio: 1                                  ← la pide TOMAR de B
           │ Objeto 1 (peso 3) no cabe → se salta
           │ Objeto 0 (peso 2) tampoco cabe → se salta
           │ No quedan objetos
DECISIÓN D │ Objeto 1 (peso 3, valor 4) │ espacio: 5      ← la pide NO TOMAR de B
           │ TOMAR    → 4 + ❓ pregunta a DECISIÓN E
           │ NO TOMAR →     ❓ pregunta a DECISIÓN F
DECISIÓN E │ Objeto 0 (peso 2, valor 3) │ espacio: 2      ← la pide TOMAR de D
           │ TOMAR    → 3
           │ NO TOMAR → 0
DECISIÓN F │ Objeto 0 (peso 2, valor 3) │ espacio: 5      ← la pide NO TOMAR de D
           │ TOMAR    → 3
           │ NO TOMAR → 0
```

E y F están hasta abajo: ya no quedan más objetos, así que pueden responder de inmediato.

**Parte 2: subiendo ⬆️** (cada respuesta regresa a quien la pidió)

| Paso | Quién responde | Su respuesta | Se envía a | Lo que completa |
|:----:|:--------------:|:------------:|:----------:|:---------------:|
| 1 | E | max(3, 0) = 3 | TOMAR de D | 4 + 3 = 7 |
| 2 | F | max(3, 0) = 3 | NO TOMAR de D | 3 |
| 3 | D | max(7, 3) = 7 | NO TOMAR de B | 7 |
| 4 | C | no cupo nada = 0 | TOMAR de B | 5 + 0 = 5 |
| 5 | B | max(5, 7) = 7 | NO TOMAR de A | 7 |
| 6 | A | max(6, 7) = 7 | — | 🏁 Respuesta final: 7 |

Cada decisión solo puede responder después de recibir las respuestas de las decisiones que preguntó. Por eso los `max` se resuelven al final, de abajo hacia arriba.

### El problema

La versión recursiva tiene la lógica correcta, pero **no recuerda nada**. Si dos caminos distintos llegan a la misma pregunta (los mismos objetos restantes y el mismo espacio), la vuelve a resolver desde cero. En el peor caso explora del orden de 2ⁿ caminos, igual que la fuerza bruta.

---

## Versión 3: programación dinámica

[Ver el código en GitHub](https://github.com/locessentials/python/blob/main/unidad3/prog-dinamica/knapsack3.py)

La programación dinámica usa **exactamente la misma lógica** que la versión recursiva (los mismos tres casos), pero en vez de volver a calcular cada pregunta, la calcula **una sola vez** y guarda la respuesta en un arreglo. Cuando otra parte del cálculo necesita esa respuesta, solo la consulta.

### El arreglo `A`: qué significan los renglones y las columnas

- **Las columnas son capacidades.** Cada columna es una cantidad de espacio en la mochila: 0 kg, 1 kg, 2 kg… hasta *W*. Los renglones van de "ningún objeto" (0) a "los 4 objetos" (4). Contar de 0 a 4 son **5** renglones, o sea *n* + 1. El renglón 4 no es un quinto objeto: significa "los cuatro objetos permitidos".
- **Los renglones son cuántos objetos se permiten.** Cada renglón permite usar un objeto más que el renglón de arriba. Las columnas van de 0 kg a 5 kg. Contar de 0 a 5 son **6** columnas, o sea *W* + 1.

```
                                        espacio en la mochila →   0  1  2  3  4  5
renglón 0: ningún objeto                                          0  0  0  0  0  0
renglón 1: + objeto 0 (peso 2, valor 3)                           0  0  3  3  3  3
renglón 2: + objeto 1 (peso 3, valor 4)                           0  0  3  4  4  7
renglón 3: + objeto 2 (peso 4, valor 5)                           0  0  3  4  5  7
renglón 4: + objeto 3 (peso 5, valor 6)                           0  0  3  4  5  7
```

Cada celda `A[i][c]` responde una sola pregunta:

> Si la mochila tiene **c** kg de espacio y solo puedo usar los objetos permitidos en el renglón **i**, ¿cuál es el mayor valor que puedo llevar?

Por ejemplo, el renglón 1 solo permite el objeto 0 (peso 2, valor 3). Con 0 o 1 kg de espacio no cabe, así que el valor es 0. Con 2 kg o más sí cabe, y como es el único objeto permitido, el valor es 3. Por eso el renglón es `0, 0, 3, 3, 3, 3`.

### El renglón 0 y la columna 0: el caso base

El renglón 0 y la columna 0 están llenos de ceros, y el código nunca los modifica después de crearlos. Pero eso **no** significa que no se usen: el código los **consulta** todo el tiempo.

- **Renglón 0** = ningún objeto permitido → valor 0.
- **Columna 0** = ningún espacio en la mochila → valor 0.

Son el caso base de la versión recursiva (`if n == 0 or W == 0: return 0`), guardado en el arreglo. La parte `n == 0` es el renglón 0, y la parte `W == 0` es la columna 0.

**¿Cuándo se consultan?**

- **El renglón 0 se consulta cada vez que se llena el renglón 1**, porque el renglón 1 siempre mira el renglón de arriba. Por ejemplo, el renglón 1 con 2 kg: `3 + A[0][0] = 3 + 0 = 3`.
- **La columna 0 se consulta cada vez que un objeto ocupa exactamente todo el espacio.** Por ejemplo, el renglón 4 (objeto 3, peso 5) con 5 kg: `6 + A[3][5 - 5] = 6 + A[3][0] = 6 + 0 = 6`.

Sin ese renglón y esa columna, esas consultas no tendrían a dónde ir y el programa fallaría.

### Llenar el arreglo: los tres casos

Primero se crea el arreglo de (*n* + 1) renglones × (*W* + 1) columnas, todo en ceros. Después se llena renglón por renglón, empezando en el renglón 1 (el renglón 0 ya está en ceros), y en cada renglón se recorren todas las columnas, de 0 kg a *W* kg.

En cada celda, el renglón agrega un objeto nuevo, con su peso (`peso = p[i-1]`) y su valor (`val = v[i-1]`). La celda se llena con los mismos tres casos de la versión recursiva:

1. **No cabe** (`peso > c`): el objeto pesa más que el espacio. La respuesta es la misma que sin este objeto, así que se copia el valor de la celda de arriba: `A[i][c] = A[i-1][c]`.
2. **No tomarlo** (`nto = A[i-1][c]`): la respuesta sin este objeto, con el mismo espacio. Está en el renglón de arriba, misma columna.
3. **Tomarlo** (`to = val + A[i-1][c - peso]`): el valor de este objeto, **más** el mayor valor que los objetos anteriores pueden agregar en el espacio que sobra.
   - `c - peso` es el espacio que queda después de meter el objeto: el objeto ocupa espacio, así que se resta su peso.
   - `A[i-1][c - peso]` es el mayor valor que los objetos anteriores pueden agregar en ese espacio. Esa respuesta **ya está calculada**, porque el renglón de arriba se llenó antes.

Si el objeto cabe, la celda se queda con la mejor de las dos opciones: `A[i][c] = max(nto, to)`.

#### Los dos −1 que no significan lo mismo

En el código aparecen `p[i-1]` (y `v[i-1]`) y `A[i-1]`. Se ven iguales, pero hacen cosas distintas.

**`p[i-1]` y `v[i-1]`: un desfase entre dos formas de contar.** El arreglo `A` tiene un renglón extra al principio (el renglón 0, "ningún objeto"), pero las listas `p` y `v` no lo tienen: su posición 0 ya es el objeto 0. Por eso los renglones van un número adelante de los objetos:

```
Renglón i:    0      1      2      3      4
A[...]:      A[0]   A[1]   A[2]   A[3]   A[4]    ← mismo número, sin desfase
p[...]:       —     p[0]   p[1]   p[2]   p[3]    ← un número atrás: se necesita i-1
```

El renglón 1 agrega el objeto 0, el renglón 2 agrega el objeto 1, y así. El −1 **no** regresa a un objeto anterior: encuentra el objeto correcto para ese renglón. Si se escribiera `p[i]`, el renglón 1 tomaría el peso del objeto 1 (el objeto 0 nunca se usaría) y el renglón 4 pediría `p[4]`, que no existe.

**`A[i-1]`: el renglón de arriba.** Aquí no hay desfase. `A` sí tiene el renglón 0, así que el renglón actual es simplemente `A[i]`. El `i-1` significa literalmente "el renglón anterior", porque ahí está la respuesta sin el objeto actual.

#### La respuesta siempre está en `A[n][W]`

La celda de abajo a la derecha es la única que hace exactamente la pregunta original:
 
- **Último renglón:** todos los objetos permitidos.
- **Última columna:** la mochila completa (*W* kg).

Todas las demás celdas responden versiones más pequeñas del problema. El mismo valor puede aparecer en otras celdas (en el ejemplo, el 7 también aparece en los renglones 2 y 3, porque la mejor combinación ya se encontró en el renglón 2), pero la esquina es la única que garantiza ser la respuesta.

La función regresa **todo el arreglo**, no solo el 7, porque la reconstrucción lo necesita para encontrar los objetos.

### Reconstrucción: encontrar los objetos

El arreglo da el valor máximo, pero no dice qué objetos lo forman. Para encontrarlos, se recorre el arreglo **hacia atrás**, desde la esquina de abajo a la derecha hasta arriba. Se empieza con una lista vacía de objetos (`S = []`) y con el peso de la mochila completa (`c = W`).

**Cómo se mueve por el arreglo:**

- **El renglón** lo controla el ciclo `for i in range(n, 0, -1)`, que empieza en *n*, se detiene **antes** de 0 y baja de 1 en 1: 4, 3, 2, 1. No llega al renglón 0 porque ahí no hay ningún objeto que revisar.
- **La columna** es `c`. Empieza en *W* y **solo se mueve cuando se toma un objeto** (`c = c - peso`).

**En cada renglón, la pregunta es: ¿este objeto entró en la mochila?** Para saberlo, se repite la misma comparación que en el llenado: tomarlo (`to = val + A[i-1][c - peso]`) contra no tomarlo (`nto = A[i-1][c]`).

Si el objeto cabe y tomarlo da un total igual o mayor que no tomarlo (`to >= nto`), el objeto entró: se anota su número (`S.append(i-1)`) y se resta su peso del espacio. Si no entró, o no cabe, no se hace nada: el ciclo sube al siguiente renglón con el mismo espacio. Cuando termina el renglón 1, el ciclo acaba y la función regresa `S`.

**Seguimiento del ejemplo de clase**, empezando con `c = 5`:

| Renglón | Objeto | ¿Cabe? | Tomarlo | No tomarlo | ¿Entró? | Espacio después |
|:-------:|:------:|:------:|:-------:|:----------:|:-------:|:---------------:|
| 4 | 3 (peso 5, valor 6) | sí | 6 + A[3][0] = 6 | A[3][5] = 7 | no | 5 |
| 3 | 2 (peso 4, valor 5) | sí | 5 + A[2][1] = 5 | A[2][5] = 7 | no | 5 |
| 2 | 1 (peso 3, valor 4) | sí | 4 + A[1][2] = 7 | A[1][5] = 3 | **sí** | 5 − 3 = 2 |
| 1 | 0 (peso 2, valor 3) | sí | 3 + A[0][0] = 3 | A[0][2] = 0 | **sí** | 2 − 2 = 0 |

Resultado: `S = [1, 0]`, los objetos 1 y 0.

### Empates

Si tomar y no tomar dan el mismo total, el `>=` hace que se tome el objeto. No hay una razón profunda: en un empate, las dos opciones llevan al mismo valor máximo, así que las dos son correctas. Con `>` los empates irían a "no tomar", y también sería correcto.

El **valor** máximo nunca cambia; lo que puede cambiar es **cuál conjunto** se regresa cuando hay varios con el mismo valor. Por ejemplo:

```
Objeto 0: peso 1, valor 5
Objeto 1: peso 1, valor 5
Mochila de 1 kg
```

Solo cabe un objeto, y el mejor valor es 5 de cualquier forma. Con `>=` la reconstrucción regresa el objeto 1; con `>`, el objeto 0. Las dos respuestas son correctas.

La reconstrucción sigue **un solo camino** por el arreglo, así que regresa **un solo conjunto**, aunque haya otros igual de buenos. En el ejemplo de clase no hay empate (los objetos 0 y 1 son la única forma de llegar a 7), así que con `>=` o con `>` el resultado es `[1, 0]`.

---

## De recursivo a programación dinámica, línea por línea

La versión con programación dinámica se construye directamente sobre la recursiva. Cada llamada recursiva se convierte en una consulta al renglón de arriba:

| Versión recursiva | Programación dinámica |
|-------------------|-----------------------|
| `mochila(p, v, W, n)` | `A[i][c]` (*i* objetos permitidos, *c* kg de espacio) |
| `if n == 0 or W == 0: return 0` | renglón 0 y columna 0 llenos de ceros |
| `if p[n-1] > W:` | `if peso > c:` |
| `return mochila(p, v, W, n-1)` | `A[i][c] = A[i-1][c]` |
| `nto = mochila(p, v, W, n-1)` | `nto = A[i-1][c]` |
| `to = v[n-1] + mochila(p, v, W - p[n-1], n-1)` | `to = val + A[i-1][c - peso]` |
| `return max(nto, to)` | `A[i][c] = max(nto, to)` |

Las diferencias:

- La recursiva **pregunta** y espera la respuesta; la programación dinámica **consulta** una respuesta que ya está guardada.
- La recursiva empieza con el problema grande y lo divide (de arriba hacia abajo); la programación dinámica empieza con los problemas pequeños y va construyendo (de abajo hacia arriba).
- La recursiva solo da el valor; con el arreglo guardado se pueden reconstruir también los objetos.

---

## Complejidad

| Versión | Tiempo | Memoria | ¿Da los objetos? |
|---------|--------|---------|:----------------:|
| Fuerza bruta | O(*n* · 2ⁿ) | O(*n* · 2ⁿ) | sí |
| Recursiva | O(2ⁿ) en el peor caso | O(*n*) | no |
| Programación dinámica | O(*n* · *W*) + O(*n*) para reconstruir | O(*n* · *W*) | sí |

- **Fuerza bruta:** genera los 2ⁿ subconjuntos y suma el peso y el valor de cada uno (hasta *n* objetos por subconjunto). Además, guarda todos los subconjuntos en una lista al mismo tiempo.
- **Recursiva:** cada objeto que cabe abre dos ramas (tomar y no tomar), así que en el peor caso hay del orden de 2ⁿ llamadas. Solo usa memoria para las llamadas que están abiertas al mismo tiempo, que son como máximo *n*.
- **Programación dinámica:** llena (*n* + 1) × (*W* + 1) celdas, y cada una se calcula en un número fijo de pasos. La reconstrucción recorre un renglón por objeto: *n* pasos.

Para darse una idea: con 30 objetos y una mochila de 100 kg, la fuerza bruta revisa más de mil millones de subconjuntos (2³⁰ = 1,073,741,824). La programación dinámica llena 31 × 101 = 3,131 celdas.

### Un detalle importante: O(*n* · *W*) depende del **valor** de *W*

La complejidad de la programación dinámica depende de qué tan grande es el **número** *W*, no solo de cuántos objetos hay. Si la mochila tuviera capacidad *W* = 1,000,000,000, el arreglo necesitaría mil millones de columnas, y la programación dinámica dejaría de ser práctica.

A esto se le llama complejidad **pseudopolinomial**: parece polinomial, pero crece con el valor de un número de la entrada, no con su tamaño. Por eso la programación dinámica funciona muy bien cuando *W* es razonablemente pequeño, pero no resuelve el problema de la mochila de forma eficiente en todos los casos.

---

## Más práctica

### Ideas para extender el código

- **Encontrar todos los conjuntos óptimos:** la reconstrucción actual regresa un solo conjunto. Para encontrar todos los conjuntos con el valor máximo, habría que dividir el camino en cada empate y seguir las dos opciones (por ejemplo, con una reconstrucción recursiva), y juntar todos los conjuntos que se obtengan.

### Variantes de este problema

- **Mochila sin límite (*unbounded knapsack*):** cada tipo de objeto tiene copias ilimitadas, así que se puede tomar el mismo objeto todas las veces que se quiera. Un ejemplo de su aplicación: el problema del cambio de monedas (formar una cantidad exacta con monedas que se pueden repetir).
- **Mochila fraccionaria (*fractional knapsack*):** se puede tomar cualquier fracción de un objeto y se obtiene esa misma fracción de su valor. Por ejemplo, polvo de oro o líquidos en lugar de objetos sólidos.