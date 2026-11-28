---
layout: default
title: Triángulo de Pascal
parent: Programación dinámica
grandparent: 3. Matemáticas y algoritmos
nav_order: 2
---

# Triángulo de Pascal

El triángulo de Pascal es un arreglo triangular de números que aparece en álgebra y en combinatoria: da los coeficientes de la expansión binomial y cuenta de cuántas formas se pueden elegir elementos de un conjunto. Cada número es la suma de los dos números que tiene justo arriba en el renglón anterior: el de arriba a la izquierda y el de arriba a la derecha. El problema de esta página es calcular el número que está en una posición dada del triángulo.

Se resuelve de tres maneras: con una función recursiva, con la misma función recursiva escrita como `lambda` y con programación dinámica. La versión recursiva aplica esa regla directamente, pero resuelve los mismos subproblemas muchas veces (*subproblemas superpuestos*), así que el número de llamadas crece de forma exponencial. La programación dinámica, en cambio, calcula el valor de cada posición una sola vez, lo guarda en un arreglo y después consulta esos valores ya calculados para regresar el de una posición específica.

---

## Conceptos claves

### Expansión binomial: desarrollar (a+b)ⁿ paso a paso

**Definiciones**
- **binomio:** expresión con dos términos sumados, como a + b
- **expansión binomial** (o **desarrollo del binomio**, *binomial expansion* en inglés): escribir una potencia de un binomio, (a+b)ⁿ, como una suma de términos sin paréntesis. Cada término es un número, llamado **coeficiente**, multiplicado por una potencia de a y una potencia de b, y las dos potencias siempre suman n. La expansión se hace para que queden a la vista los coeficientes. Por ejemplo, (a+b)² = (a+b)(a+b) se expande como a² + 2ab + b². Escrito con todos sus coeficientes, es 1a² + 2ab + 1b², de donde sacamos el renglón 2 del triángulo de Pascal: 1 2 1. En el término 2ab, el coeficiente es 2, y como ab = a¹b¹, las potencias suman 1 + 1 = 2.

**Casos base**
- **(a+b)⁰ = 1:** cualquier número distinto de 0 elevado a la potencia 0 es 1. Por ejemplo, (2+3)⁰ = 5⁰ = 1. Su único coeficiente es 1: es el **renglón 0** del triángulo.
- **(a+b)¹ = a + b:** la potencia 1 deja la expresión igual. Escrito con sus coeficientes, es 1a + 1b: es el **renglón 1** del triángulo, `1 1`.

**Regla:** cada potencia es la anterior multiplicada por (a+b) una vez más. Por ejemplo, (a+b)² = (a+b)¹ · (a+b), y (a+b)³ = (a+b)² · (a+b). Multiplicar por (a+b) quiere decir multiplicar cada término por **a** y por **b**, y luego juntar los términos semejantes (los que tienen las mismas potencias de a y de b). Los árboles de abajo muestran exactamente este paso.

#### De (a+b)¹ a (a+b)²

```
        a                 b
       / \               / \
     ×a   ×b           ×a   ×b
     /     \           /     \
   a²       ab       ab       b²
            └────┬────┘
           ab + ab = 2ab

(a+b)² = a² + 2ab + b²
```

#### De (a+b)² a (a+b)³

```
         a²                 2ab                 b²
        /  \               /   \               /  \
      ×a    ×b           ×a     ×b           ×a    ×b
      /      \           /       \           /      \
     a³      a²b       2a²b      2ab²      ab²      b³
              └────┬────┘         └────┬────┘
                 3a²b                3ab²

(a+b)³ = a³ + 3a²b + 3ab² + b³
```

#### De (a+b)³ a (a+b)⁴

```
         a³               3a²b              3ab²               b³
        /  \              /  \              /  \              /  \
      ×a    ×b          ×a    ×b          ×a    ×b          ×a    ×b
      /      \          /      \          /      \          /      \
     a⁴      a³b     3a³b      3a²b²  3a²b²      3ab³     ab³      b⁴
              └───┬───┘          └───┬───┘        └───┬───┘
                4a³b               6a²b²            4ab³

(a+b)⁴ = a⁴ + 4a³b + 6a²b² + 4ab³ + b⁴
```

### Los coeficientes forman el triángulo de Pascal

Si se escriben solo los coeficientes de cada potencia de (a+b), empezando por (a+b)⁰, cada una en un renglón debajo de la anterior, se obtiene el triángulo de Pascal. Cada número de en medio es la suma de los dos números que tiene justo arriba en el renglón anterior: el de arriba a la izquierda y el de arriba a la derecha. Con índices (contando desde 0), el número en la posición k del renglón n es la suma de las posiciones k − 1 y k del renglón n − 1. Por ejemplo, el 6 del renglón 4 está en la posición 2, y es la suma de las posiciones 1 y 2 del renglón 3: 3 + 3 = 6. El primer y el último número de cada renglón son siempre 1.

```
            posición →   0   1   2   3   4   5
renglón n=0:               1
renglón n=1:               1   1
renglón n=2:               1   2   1
renglón n=3:               1   3   3   1
renglón n=4:               1   4   6   4   1
renglón n=5:               1   5  10  10   5   1
```

### Teorema del binomio

El teorema del binomio es una fórmula que da la expansión de (a+b)ⁿ de una sola vez, para cualquier n, sin tener que multiplicar por (a+b) una potencia tras otra como en los árboles:

```
(a+b)ⁿ = Σₖ₌₀ⁿ C(n,k) · aⁿ⁻ᵏ · bᵏ
```

Donde:

- **Σ (sigma)** significa "sumar". El k=0 de abajo y la n de arriba quieren decir: calcular la expresión para k = 0, 1, 2, … hasta n, y sumar todos los resultados.
- **C(n,k)**, que se lee "n en k" o "combinaciones de n en k", es el número del triángulo de Pascal en el renglón n, posición k (contando desde 0): el coeficiente del término. También se puede calcular directamente:
  C(n,k) = n! / (k! · (n−k)!), donde n! = n · (n−1) · … · 1
- **aⁿ⁻ᵏ · bᵏ:** conforme k sube, la potencia de a baja de n hasta 0 y la de b sube de 0 hasta n.
Por ejemplo, en (a+b)⁴ el término 6a²b² tiene coeficiente C(4,2) = 4! / (2! · 2!) = 24 / 4 = **6**, el mismo que da el árbol.

Con la fórmula se puede calcular un solo término sin construir nada más. Por ejemplo, el término a⁷b³ de (a+b)¹⁰ tiene coeficiente C(10,3) = 120, así que el término es 120a⁷b³.

### Regla de Pascal

La regla de Pascal dice cómo se calcula cada número del triángulo a partir del renglón de arriba: el número del renglón n, posición k, es la suma de los dos números que tiene justo arriba, los de las posiciones k − 1 y k del renglón n − 1. Si C(n,k) es el número del renglón n, posición k, la regla se escribe así:

```
C(n,k) = C(n−1, k−1) + C(n−1, k)
```

Por ejemplo, C(4,2) = C(3,1) + C(3,2) = 3 + 3 = **6**:

```
renglón 3:    1   3   3   1
                   \ /
renglón 4:  1   4   6   4   1
```

---

## Panorama del código

[Ver el código en GitHub](https://github.com/locessentials/python/blob/main/unidad3/prog-dinamica/pascal.py)

Las tres versiones calculan el mismo valor, `pascal(5, 2)`, y deben dar **10**.

### Versión 1: recursiva

```python
def pascal(n, k):
    if k == 0 or n == k:
        return 1
    return pascal(n-1, k-1) + pascal(n-1, k)
```

La función es la regla de Pascal tal cual:

- **Caso base:** si la posición está en una orilla (`k == 0` o `n == k`), regresa 1. Es lo que detiene la recursión.
- **Caso recursivo:** si no, suma el número de arriba a la izquierda, `pascal(n-1, k-1)`, y el de arriba a la derecha, `pascal(n-1, k)`.

Esta suma no se puede evaluar hasta que las dos llamadas recursivas regresen su valor, así que cada llamada genera dos llamadas nuevas y se queda pendiente en la pila de llamadas (call stack) hasta que ambas terminan. La recursión se ramifica así hasta que cada rama llega a un caso base, una orilla del triángulo, que regresa 1. A partir de ahí, los valores regresan y se suman de abajo hacia arriba.

Por ejemplo: `pascal(5, 2)`

**Parte 1: bajando ⬇️**

`pascal(5, 2)` se divide en `pascal(4, 1)` + `pascal(4, 2)`, y cada una se sigue dividiendo hasta llegar a un 1 en la orilla del triángulo.

```
pascal(5,2)
├─ pascal(4,1)
│   ├─ pascal(3,0) → 1
│   └─ pascal(3,1)
│       ├─ pascal(2,0) → 1
│       └─ pascal(2,1)
│           ├─ pascal(1,0) → 1
│           └─ pascal(1,1) → 1          → 2
│                                       → 3
│                                       → 4
└─ pascal(4,2)
    ├─ pascal(3,1)
    │   ├─ pascal(2,0) → 1
    │   └─ pascal(2,1)
    │       ├─ pascal(1,0) → 1
    │       └─ pascal(1,1) → 1          → 2
    │                                   → 3
    └─ pascal(3,2)
        ├─ pascal(2,1)
        │   ├─ pascal(1,0) → 1
        │   └─ pascal(1,1) → 1          → 2
        └─ pascal(2,2) → 1              → 3
                                        → 6
                                        → 10
```

**Parte 2: subiendo ⬆️** (las sumas se resuelven de abajo hacia arriba)

| Llamada | Cálculo | Resultado |
|:-------:|:-------:|:---------:|
| `pascal(2,1)` | 1 + 1 | 2 |
| `pascal(3,1)` | 1 + 2 | 3 |
| `pascal(3,2)` | 2 + 1 | 3 |
| `pascal(4,1)` | 1 + 3 | 4 |
| `pascal(4,2)` | 3 + 3 | 6 |
| `pascal(5,2)` | 4 + 6 | **10** |

Coincide con el renglón 5 del triángulo: 1 5 **10** 10 5 1.

#### El problema: trabajo repetido

- `pascal(3,1)` se calcula **2 veces**.
- `pascal(2,1)` se calcula **3 veces**.
- El árbol tiene **19 llamadas** en total: 6 calculan valores distintos (los seis renglones de la tabla de arriba), 3 repiten un cálculo que ya se hizo y 10 son casos base que regresan 1.

Como la versión recursiva no guarda ningún resultado, el número de llamadas crece de forma exponencial con n.

---

![Logo de Python en amarillo y rojo]({{ '/imagenes/python-logo.png' | relative_url }}){: .tip-circle }

**Versión recursiva con `lambda`**

El código tiene la misma función recursive escrita como una `lambda`. Como una `lambda` no puede tener `return` ni bloques `if`, el `if` se escribe como **expresión condicional**: `VALOR_SI if CONDICIÓN else VALOR_NO`. La `lambda` se puede llamar a sí misma porque está guardada en el nombre `pascal`, y Python busca ese nombre en el momento de cada llamada.

```python
pascal = lambda n, k : 1 if k == 0 or n == k else pascal(n-1, k-1) + pascal(n-1, k)
```

<span class="clear"></span>

---

### Versión 2: programación dinámica

La programación dinámica usa **la misma regla de Pascal**, pero en vez de volver a calcular el valor de cada posición, lo calcula **una sola vez** y lo guarda en un arreglo. Cuando se necesita ese valor para calcular otra posición, el programa consulta el valor en el arreglo en vez de volver a calcularlo.

#### El arreglo `A`

`A` es una lista de listas: cada lista es un renglón del triángulo, así que `A[n][k]` es el número del renglón n, posición k. Cada renglón tiene un número más que el renglón anterior.

```
A[0] = [1]
A[1] = [1, 1]
A[2] = [1, 2, 1]
A[3] = [1, 3, 3, 1]
A[4] = [1, 4, 6, 4, 1]
A[5] = [1, 5, 10, 10, 5, 1]
```

#### Construir el triángulo (`triangle(n)`) y consultar un valor (`lookup(A, n, k)`)

El programa construye el triángulo de Pascal con dos ciclos `for` anidados: el externo recorre las filas y el interno recorre las posiciones dentro de cada fila.

En cada vuelta del ciclo externo:

1. `[1] * (renglon + 1)` crea el renglón lleno de 1, así que las orillas (el caso base) ya quedan correctas.
2. El ciclo interno, `for k in range(1, renglon)`, llena las posiciones de en medio, de la 1 a la `renglon - 1`, con la regla de Pascal, usando el renglón de arriba, `A[renglon - 1]`.
3. `append` agrega el renglón terminado a `A`.

En los renglones 0 y 1, `range(1, renglon)` está vacío, así que el ciclo interno no corre y no hace falta un `if`. A partir del renglón 2, el renglón de arriba ya está en `A` porque la vuelta anterior lo agregó.

Con el triángulo completo, `lookup` solo regresa `A[n][k]`.

---

## De recursivo a programación dinámica

Las dos versiones del programa aplican la misma regla de Pascal. Lo que cambia es de dónde sale el valor de cada posición del triángulo. La versión recursiva lo calcula de nuevo con otra llamada cada vez que lo necesita, y la de programación dinámica lo lee del renglón de arriba, que ya está guardado en `A`. 

Esta tabla pone cada parte de la versión recursiva junto a la línea que la reemplaza:

| Versión recursiva | Programación dinámica |
|-------------------|-----------------------|
| `pascal(n, k)` | `A[renglon][k]` |
| `if k == 0 or n == k: return 1` | `[1] * (renglon + 1)`: las orillas empiezan en 1 y no se tocan |
| `pascal(n-1, k-1)` | `A[renglon - 1][k - 1]` |
| `pascal(n-1, k)` | `A[renglon - 1][k]` |
| `return pascal(n-1, k-1) + pascal(n-1, k)` | `nuevo_renglon[k] = A[renglon - 1][k - 1] + A[renglon - 1][k]` |

Las diferencias:

- La recursiva **pregunta** y espera la respuesta; la programación dinámica **consulta** una respuesta que ya está guardada.
- La recursiva empieza con el problema grande y lo divide (de arriba hacia abajo); la programación dinámica empieza con los renglones pequeños y va construyendo (de abajo hacia arriba). A esta forma de programación dinámica se le llama **tabulación**.
- La recursiva calcula un solo valor; la programación dinámica construye el triángulo completo, y después se puede consultar cualquier posición.

---

## Complejidad

Para darse una idea de la diferencia entre la complejidad de la versión recursiva y la de programación dinámica, se puede comparar cuánto trabajo hace cada una para calcular el número del renglón 30, posición 15. La versión recursiva, `pascal(30, 15)`, hace **310,235,039** llamadas. La programación dinámica hace solo **496** sumas, una por cada número del triángulo hasta el renglón 30, y después puede usar ese mismo triángulo para dar el valor de cualquier posición de esos renglones sin volver a calcular nada.

| Versión | Tiempo | Memoria |
|---------|--------|---------|
| Recursiva (y `lambda`) | Exponencial: casi 2ⁿ llamadas en el peor caso (la posición de en medio) | O(*n*): solo las llamadas pendientes en la pila |
| Programación dinámica | O(*n*²) para construir el triángulo, O(1) por consulta | O(*n*²): todo el triángulo |

### De dónde sale O(2ⁿ) en la versión recursiva

Cada llamada que no está en una orilla hace dos llamadas nuevas, y cada una de esas llamadas baja un renglón. Como se empieza en el renglón n y el último renglón es el 0, el árbol tiene a lo más n niveles debajo de la primera llamada. Si en cada nivel todas las llamadas se dividieran en dos, el número de llamadas se duplicaría en cada nivel:

```
nivel 0:   1 llamada
nivel 1:   2 llamadas
nivel 2:   4 llamadas
nivel 3:   8 llamadas
   …
nivel n:   2ⁿ llamadas
```

Por eso la versión recursiva es O(2ⁿ). En la práctica hace un poco menos, porque las ramas que llegan a una orilla se detienen antes; el peor caso es la posición de en medio, que es la que más tarda en llegar a las orillas.

### De dónde sale O(*n*²) en la programación dinámica

La programación dinámica calcula cada posición del triángulo una sola vez, así que el trabajo depende de cuántas posiciones tiene el triángulo. Hay n + 1 renglones y cada uno tiene a lo más n + 1 posiciones, entonces el triángulo tiene (n + 1)(n + 2) / 2 posiciones con valor, más o menos la mitad de un cuadrado de (n + 1) × (n + 1):

```
■ □ □ □ □
■ ■ □ □ □
■ ■ ■ □ □
■ ■ ■ ■ □
■ ■ ■ ■ ■
```

Por eso es O(*n*²).