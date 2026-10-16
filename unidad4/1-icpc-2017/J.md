---
layout: default
title: Problema J
grandparent: 4. Problemas
parent: ICPC 2017
nav_order: 10
---

# ICPC 2017 - Problema J: flujo máximo con dos líquidos

Hay una red de **n** nodos y **p** tuberías. Del nodo 1 sale un **líquido L** y del nodo 2 sale **agua**. Los dos tienen que llegar al **nodo 3**.

- Las tuberías se pueden usar en cualquier dirección, pero los dos líquidos no pueden ir en direcciones contrarias por la misma tubería.
- Cada tubería tiene capacidad **c**. Si pasan **f** litros de L y **w** litros de agua, se tiene que cumplir **v × f + w ≤ c**.
- En los demás nodos, lo que entra de cada líquido tiene que ser igual a lo que sale.

Si **F** es la cantidad de L y **W** la cantidad de agua que llegan al nodo 3, ¿cuál es el valor máximo de **F<sup>a</sup> × W<sup>1 − a</sup>**?

**Salida:** para cada tubería, la cantidad de L y de agua que pasa por ella (negativa si va de k a j), y al final el valor máximo. Error permitido: 0.0001.

**Límites:** 3 ≤ n ≤ 200, 1 ≤ v ≤ 10, 0.01 ≤ a ≤ 0.99, 1 ≤ c ≤ 10

**Ejemplos**

| Entrada 1 | Entrada 2 |
| --------- | --------- |
| n = 6, p = 6, v = 3.0, a = 0.66<br>tubería 1: 2–4, c = 8<br>tubería 2: 4–6, c = 1<br>tubería 3: 3–6, c = 1<br>tubería 4: 4–5, c = 5<br>tubería 5: 1–5, c = 7<br>tubería 6: 3–5, c = 3 | n = 5, p = 5, v = 1.0, a = 0.5<br>tubería 1: 1–2, c = 10<br>tubería 2: 2–3, c = 10<br>tubería 3: 3–4, c = 10<br>tubería 4: 4–5, c = 10<br>tubería 5: 3–5, c = 10 |
| **Salida:**<br>tubería 1: L = 0, agua = 1.36<br>tubería 2: L = 0, agua = 1<br>tubería 3: L = 0, agua = −1<br>tubería 4: L = 0, agua = 0.36<br>tubería 5: L = 0.88, agua = 0<br>tubería 6: L = −0.88, agua = −0.36<br>valor máximo: 1.02037965897 | **Salida:**<br>tubería 1: L = 5, agua = 0<br>tubería 2: L = 5, agua = 5<br>tubería 3: L = 4.2, agua = 3.14159<br>tubería 4: L = 4.2, agua = 3.14159<br>tubería 5: L = −4.2, agua = −3.14159<br>valor máximo: 5 |

---

## Conceptos claves

### Flujo máximo

Tenemos una red de nodos y tuberías. Cada tubería tiene una capacidad. Queremos saber cuánto líquido puede llegar, como máximo, de un nodo **fuente** a un nodo **destino**.

Algoritmo de **caminos de aumento más cortos**:

1. Buscar un camino de la fuente al destino donde todas las tuberías tengan espacio libre. Se busca con búsqueda en anchura (**breadth-first search**, BFS), así se encuentra el camino más corto.
2. La cantidad que puede llevar el camino es el espacio libre más pequeño de sus tuberías.
3. Mandar esa cantidad por el camino. En cada tubería del camino, restar esa cantidad del espacio libre.
4. En cada tubería del camino, sumar esa cantidad al espacio libre en la dirección contraria. Este espacio no sirve para mandar líquido hacia atrás: sirve para quitar flujo que ya se mandó. Así, un camino nuevo puede corregir una decisión anterior.

**Ejemplo:** todas las tuberías tienen capacidad 1.

```
         a
       ↗ │ ↘
     s   │   t
       ↘ ↓ ↗
         b
```

- Camino 1: s → a → b → t. Después de este camino, no queda ningún camino libre de s a t.
- Camino 2: s → b → a → t. El paso b → a usa el espacio en la dirección contraria: quita el flujo que el camino 1 mandó por a → b.
- Resultado: la tubería del centro queda en 0, y las partes de los dos caminos se juntan de otra forma: s → a → t y s → b → t. Total: 2.

5. Repetir hasta que no haya camino. La suma de lo que se mandó es el flujo máximo.

### Ideas que usamos junto con el algoritmo

**Varias fuentes**

- Se agrega una **superfuente**, un nodo nuevo conectado a cada fuente. Si la conexión tiene capacidad k, esa fuente puede mandar como máximo k. Importa para este problema porque hay dos fuentes, el nodo 1 (L) y el nodo 2 (agua), y el destino es el nodo 3:

```
            1 ─── ...
      k1  ↗          ╲
   S                   3
      k2  ↘          ╱
            2 ─── ...
```

- S es la superfuente, un nodo nuevo que agregamos. No es parte de la red real.
- S tiene una tubería al nodo 1 con capacidad k1, y una tubería al nodo 2 con capacidad k2.
- Los "..." representan el resto de la red real entre los nodos 1 y 2 y el nodo 3.

Luego usamos el algoritmo una sola vez, de S al nodo 3. El algoritmo solo sabe trabajar con una fuente, así que S hace el papel de esa fuente, y las tuberías que salen de S deciden cuánto puede mandar cada fuente real.

**Corte**

- Si separamos la red en dos lados, uno con la fuente y otro con el destino, todo el flujo tiene que cruzar las tuberías entre los dos lados. Por eso, el flujo máximo es igual a la capacidad del corte más pequeño.

```
          corte A           corte B
             ┊                 ┊
     ┌── 5 ──┊──→ a ─── 1 ─────┊──→ ┐
     s       ┊                 ┊    t
     └── 5 ──┊──→ b ─── 2 ─────┊──→ ┘
             ┊                 ┊
```

- **Corte A** cruza las tuberías s → a y s → b. Capacidad del corte: 5 + 5 = 10.
- **Corte B** cruza las tuberías a → t y b → t. Capacidad del corte: 1 + 2 = 3.
- Todo el flujo tiene que cruzar el corte B, y por ahí solo caben 3. Entonces el flujo máximo es 3, la capacidad del corte más pequeño.

**Cambio de unidades**

Cada litro de L usa v unidades de espacio en la tubería, y cada litro de agua usa 1. L usa más espacio porque es más viscoso que el agua. Si medimos L en unidades de espacio, la regla de cada tubería, v × f + w ≤ c, dice: el espacio que usan L y el agua, sumado, no puede pasar la capacidad de la tubería. Con este cambio, los dos líquidos usan el espacio de la misma forma. En total, L usa x = v × f unidades de espacio.

Aquí:
- **v:** cuántas unidades de espacio usa un litro de L, comparado con un litro de agua, que usa 1
- **f:** litros de L en total que llegan al nodo 3
- **w:** litros de agua en una tubería
- **c:** capacidad de una tubería
- **x:** espacio que usa L en total, x = v × F (el cambio de unidades)

En este problema usamos flujo máximo cinco veces:

- tres veces para encontrar M1, M2 y M12
  - **M1:** lo máximo que el líquido L puede mandar del nodo 1 al nodo 3, si no hay agua. Se mide en unidades de espacio, así que es el valor más grande que puede tener x.
  - **M2:** lo máximo que el agua puede mandar del nodo 2 al nodo 3, si no hay L.
  - **M12:** lo máximo que pueden mandar los dos juntos, porque comparten las tuberías. Es el valor más grande que puede tener x + W.

- una vez para el flujo combinado
- una vez para separar L del agua

### Media geométrica ponderada

- **Media aritmética** de A y B: (A + B) / 2. Ejemplo: A = 4, B = 9 → 6.5
- **Media geométrica**: √(A × B), que es lo mismo que A<sup>0.5</sup> × B<sup>0.5</sup>. Ejemplo: A = 4, B = 9 → 6
- **Media geométrica ponderada**: A<sup>a</sup> × B<sup>1 − a</sup>. El número a dice cuánto "pesa" A, y 1 − a dice cuánto pesa B. Con 1 − a, los dos pesos suman 1, y eso hace falta para que sea un promedio.

**Regla clave:** si la suma A + B = T no cambia, el valor máximo de A<sup>a</sup> × B<sup>1 − a</sup> se encuentra con A = a × T y B = (1 − a) × T.

En nuestro problema:
- **A** es x, el espacio que usa L en total. Como x = v × f, buscar el máximo con x da la misma respuesta que buscarlo con f.
- **B** es W, el agua en total.
- **T** es M12, el valor más grande que puede tener x + W.

Ejemplo con T = 10 y a = 0.5:

| A | B | A<sup>0.5</sup> × B<sup>0.5</sup> |
| - | - | --- |
| 2 | 8 | 4 |
| 5 | 5 | **5** |
| 8 | 2 | 4 |

Si A o B es 0, el valor es 0, porque cualquier número multiplicado por 0 da 0. Por eso, el mejor valor siempre manda de los dos líquidos.

**Por qué importa aquí:**

1. Queremos el máximo de F<sup>a</sup> × W<sup>1 − a</sup>. Como F = x / v, el número 1 / v solo multiplica el valor y no cambia dónde está el máximo. Entonces podemos trabajar con x y W.
2. Más de cualquiera de los dos líquidos sube el valor. Por eso, en el mejor punto, x + W = M12, el total máximo.
3. Por la regla clave, x = a × M12 y W = (1 − a) × M12.
4. Si ese x no cumple x ≤ M1 o W ≤ M2, usamos el límite más cercano. El valor solo sube cuando nos acercamos al punto ideal, así que el límite más cercano es el mejor punto posible.

---

## Estructura del código

1. **`read_input`**: leer n, p, v y a. Luego leer las tuberías, una por renglón; p dice cuántas son. Cada tubería tiene dos nodos, j y k, y una capacidad c. Cada tubería se guarda en las dos direcciones, j → k y k → j, las dos con capacidad c, porque se puede usar en cualquier dirección. También se guarda el orden de entrada, porque la salida se imprime en ese orden.

   - **n:** número de nodos
   - **p:** número de tuberías
   - **v:** cuántas unidades de espacio usa un litro de L, comparado con un litro de agua, que usa 1
   - **a:** un número entre 0 y 1 que dice cuánto cuenta L en el valor final, F^a × W^(1 − a); el agua cuenta 1 − a

2. **`max_flow` para encontrar la mayor cantidad que puede llegar al nodo 3**, usando varios caminos al mismo tiempo sin pasar ninguna capacidad.
   - Agrega la superfuente S, con una tubería al nodo 1 de capacidad k1 y una al nodo 2 de capacidad k2.
   - Busca con BFS (búsqueda en anchura) un camino desde la superfuente S hasta el nodo 3 que solo use tuberías con espacio libre. Como los números son decimales y tienen errores de redondeo, el espacio libre solo cuenta si es mayor que un margen pequeño, por ejemplo 0.000000001.
   - Si no hay camino, termina. Si hay, la cantidad que se manda es el espacio libre más pequeño de sus tuberías, porque es lo máximo que puede pasar por todo el camino.
   - En cada tubería del camino, esa cantidad se resta del espacio libre y se suma al espacio libre en la dirección contraria. Luego se repite.
   - Devuelve el total que llegó al nodo 3 y cuánto pasa por cada tubería.

3. **Tres llamadas a max_flow para encontrar los límites**: cuánto puede llegar al nodo 3 de L solo, de agua sola y de los dos juntos. No mandamos estos flujos; el paso 4 los usa para revisar si la cantidad ideal es posible. Hay dos casos:

M1 es mayor que la x ideal (a × M12): M1 no cambia nada, y se manda la cantidad ideal.
M1 es menor que la x ideal: no se puede mandar la cantidad ideal, y se manda exactamente M1.

Ejemplo: la x ideal es 6, pero M1 = 2. Sin M1, no sabríamos que 6 es imposible, y el paso 5 no podría mandarlo.

M1 es una revisión: ¿la cantidad ideal de L es posible? Si no, lo máximo que se puede mandar es M1. M1 no dice nada sobre los caminos; el paso 5 decide los caminos. M2 hace lo mismo para el agua. Una capacidad infinita (∞) nunca limita el flujo. En el código se usa un número mayor que cualquier flujo posible.
   - M1: k1 = ∞, k2 = 0, solo L.
   - M2: k1 = 0, k2 = ∞, solo agua.
   - M12: k1 = ∞ y k2 = ∞, los dos juntos.

4. **`choose_amounts` para decidir cuánto mandar de cada líquido**: x es el espacio que usa L en total, y W es el espacio que usa el agua en total (para el agua, litros y unidades de espacio son el mismo número). Los pares posibles de (x, W) son los que cumplen x ≤ M1, W ≤ M2 y x + W ≤ M12.
   - **Primero, x = a × M12.** Es la regla clave: el total es M12, y la mejor división le da a L la parte a y al agua la parte 1 − a.
   - **Si x es mayor que M1, usar x = M1. Si x es menor que M12 − M2, usar x = M12 − M2.** Se revisa que la división sea posible. L no puede usar más que M1, por eso, si x es mayor que M1, hay que usar x = M1; el agua no puede usar más que M2, y como recibe M12 − x, x no puede ser menor que M12 − M2: si lo es, hay que usar x = M12 − M2. En los dos casos, x se mueve al límite más cercano, que da el mejor valor posible.
   - **Al final, W = M12 − x.** Se usa todo el total M12, y el agua recibe lo que L no usa.

5. **Flujo combinado para encontrar el espacio total que usan los dos líquidos en cada tubería**: llamar a `max_flow` (la cuarta llamada) con k1 = x y k2 = W. El resultado da, para cada tubería, una dirección y una cantidad g:

- **c:** lo que puede llevar la tubería (lo da el problema)
- **g:** lo que pasa de verdad por la tubería, L y agua juntos, cuando se toma en cuenta toda la red (lo da el paso 5)

Los dos líquidos van a usar esa misma dirección, y así se cumple la regla de no ir en direcciones contrarias.

**Nota:** k1 y k2 no son nodos: son las capacidades de las tuberías S → 1 y S → 2, donde S = superfuente; k1 y k2 no tienen relación con la k de las tuberías j–k.

6. **`split_flow` para encontrar cuánto de cada tubería es L y cuánto es agua**: separar L del agua.
   - Usar el resultado de la llamada a `max_flow` del paso 5, el flujo combinado, para construir una red nueva: cada tubería solo va en la dirección del flujo combinado, con capacidad g. Si g = 0, la tubería no se usa.
   - Hacer otra llamada a `max_flow`, la quinta, solo desde el nodo 1, con k1 = x y k2 = 0. x es la cantidad total de L que decidió el paso 4; esta llamada no busca una cantidad nueva, sino cuánto de esa x pasa por cada tubería: h, la parte de x en una tubería.  
   - Siempre llegan las x unidades, porque en el paso 5 esas x unidades ya pasaron del nodo 1 al nodo 3 dentro de las mismas g.
   - El agua en cada tubería es g − h. Este flujo sale solo del nodo 2, porque el flujo combinado sale de los nodos 1 y 2, y h sale solo del nodo 1.
   - En cada tubería, h + (g − h) = g ≤ c, así que se cumple v × f + w ≤ c.

7. **`print_output`**: para cada tubería, en el orden de entrada:
   - L = h / v, para cambiar de unidades de espacio a litros.
   - agua = g − h.
   - Si el flujo va de k a j, los dos números son negativos.
   - Al final, imprimir el valor máximo, (x / v)^a × W^(1 − a), con suficientes decimales para cumplir el error permitido de 0.0001.

---

## Análisis de la solución

### Construcción del algoritmo

1. Leer el número de nodos, el número de tuberías y la capacidad c de cada tubería.
2. `max_flow`: función que calcula el flujo máximo; la usa el resto del programa.
3. Tres llamadas a `max_flow` para encontrar los límites de L, del agua y de los dos juntos (M1, M2 y M12). Sirven para revisar si se puede mandar la cantidad ideal; si no, se manda lo que sí es posible.
4. `choose_amounts`: decidir cuánto L (x) y cuánta agua (W) llegan en total al nodo 3.
5. Flujo combinado: encontrar los caminos y la cantidad g de L y agua juntos en cada tubería, tomando en cuenta las capacidades de toda la red.
6. `split_flow`: dividir cada g en L (h) y agua (g − h).
7. `print_output`: imprimir L y agua de cada tubería, y el valor máximo.

### Variables y tipos de datos

- `int`: n, p y los números de los nodos, porque son conteos y posiciones.
- `float`: v, a, c, x, W, M1, M2, M12, g y h, porque los flujos pueden ser decimales (por ejemplo, 0.88).
- `float` para el margen pequeño (0.000000001), porque los decimales tienen errores de redondeo y no se pueden comparar con 0 de forma exacta.
- `bool`: para marcar qué nodos ya visitó el BFS.
- `str`: solo al leer la entrada, antes de cambiarla a números.

### Estructuras de datos

- **Lista de tuplas** (j, k, c) para las tuberías: guarda el orden de entrada, que se necesita para la salida. Las tuplas no cambian, como los datos de la entrada.
- **Matriz de capacidades** (n × n): da el espacio libre de j → k y de k → j de inmediato. Con n ≤ 200, son 40,000 números, que caben bien en memoria.
- **Lista de adyacencia:** para cada nodo, la lista de sus vecinos. Así el BFS solo revisa las tuberías que existen, no los 200 nodos cada vez.
- **Cola** (`deque`): el BFS saca los nodos en el orden en que entran, y así encuentra el camino más corto. `deque` saca del principio rápido; una lista normal es lenta para eso.
- **Lista de padres:** guarda de qué nodo se llegó a cada nodo, para reconstruir el camino al final del BFS.

### Paradigma algorítmico

**Búsqueda en grafos dentro de flujo máximo (algoritmo de caminos de aumento más cortos con BFS).** Parece voraz porque cada camino manda lo más que puede, pero el espacio en la dirección contraria permite corregir decisiones anteriores; por eso siempre encuentra el máximo. La división entre L y agua usa una regla matemática (media geométrica ponderada), no una búsqueda.

### Estilo de programación

**Procedural.** Cada paso es una función (`read_input`, `max_flow`, `choose_amounts`, `split_flow`, `print_output`). Conviene porque `max_flow` se usa cinco veces con distintos datos, y así se escribe una sola vez.

### Iterativo o recursivo

**Iterativo.** El BFS usa una cola y un ciclo `while`, y `max_flow` repite la búsqueda en otro ciclo hasta que no hay camino. El BFS es iterativo por naturaleza, y así no hay riesgo de pasar el límite de recursión de Python.

### Complejidad

- **Temporal:** O(n × p²) para cada llamada a `max_flow`. Cada BFS cuesta O(n + p), y Edmonds–Karp hace como máximo O(n × p) caminos, sin importar las capacidades. Cinco llamadas no cambian la complejidad, porque 5 es una constante. La operación que la determina es el BFS repetido.
- **Espacial:** O(n²) por la matriz de capacidades; las listas usan O(n + p).