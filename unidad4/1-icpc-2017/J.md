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

Cada litro de L usa v unidades de espacio en la tubería. Si medimos L en unidades de espacio, x = v × F, la regla de cada tubería queda como x + w ≤ c. Con este cambio, los dos líquidos usan el espacio de la misma forma.

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
- **Media geométrica ponderada**: A<sup>a</sup> × B<sup>1 − a</sup>. El número a dice cuánto "pesa" A, y 1 − a dice cuánto pesa B.

**Regla clave:** si la suma A + B = S no cambia, el valor máximo de A<sup>a</sup> × B<sup>1 − a</sup> se encuentra con A = a × S y B = (1 − a) × S.

Ejemplo con S = 10 y a = 0.5:

| A | B | A<sup>0.5</sup> × B<sup>0.5</sup> |
| - | - | --- |
| 2 | 8 | 4 |
| 5 | 5 | **5** |
| 8 | 2 | 4 |

Si A o B es 0, el valor es 0. Por eso conviene mandar de los dos líquidos.

**Por qué importa aquí:**

1. Queremos el máximo de F<sup>a</sup> × W<sup>1 − a</sup>. Como F = x / v, el número 1 / v solo multiplica el valor y no cambia dónde está el máximo. Entonces podemos trabajar con x y W.
2. Más de cualquiera de los dos líquidos sube el valor. Por eso, en el mejor punto, x + W = M12, el total máximo.
3. Por la regla clave, x = a × M12 y W = (1 − a) × M12.
4. Si ese x no cumple x ≤ M1 o W ≤ M2, usamos el límite más cercano. El valor solo sube cuando nos acercamos al punto ideal, así que el límite más cercano es el mejor punto posible.