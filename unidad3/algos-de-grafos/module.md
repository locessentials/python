---
layout: default
title: El módulo graphs.py
parent: Algoritmos de grafos
grandparent: 3. Matemáticas y algoritmos
nav_order: 2
---

# El módulo `graphs.py`

## Introducción

En la sección anterior (**Introducción**), vimos el origen matemático de los grafos y la notación formal **G = (V, E)**. En la sección **2. Estructuras de datos > Grafos** aprendimos a guardar grafos usando las estructuras básicas de Python: diccionarios, listas y tuplas. 

Sin embargo, cuando pasamos del almacenamiento a los algoritmos (BFS, DFS, Dijkstra), trabajar con diccionarios sueltos y tuplas `(vecino, peso)` se vuelve complicado. Cada función tendría que saber cómo está armado el diccionario, y un error en un solo lugar rompería todo el programa.

La solución es usar **Programación Orientada a Objetos (POO)**: encapsular toda la lógica de un grafo en un módulo reutilizable. Así, el algoritmo de BFS no necesita saber si el grafo se guarda en un diccionario o en una matriz; solo le dice al grafo *"dame los vecinos de este nodo"* y el grafo se encarga.

En esta página analizaremos el módulo **[`graphs.py`](https://github.com/locessentials/python/blob/main/unidad3/algoritmos-de-grafos/graphs.py)**, disponible en el repositorio del wiki. El archivo contiene tres clases:

- **`Edge`** – una conexión entre dos nodos (y su peso)
- **`Node`** – un nodo, que contiene sus aristas y su etiqueta
- **`Graph`** – el grafo completo, que administra la colección de nodos

Ya vimos la sintaxis básica de clases y la de `import` en los Cheat Sheets 7 y 8. Por eso, esta página no repite esos conceptos: se enfoca en las **decisiones de diseño** detrás de cada clase: por qué tiene ciertos atributos, por qué tiene ciertos métodos, y cómo se conectan entre sí para formar un módulo cohesivo.

Analizaremos el código clase por clase, y al final mostraremos un archivo `test.py` que pone todo a prueba.

---

## 1. La clase `Edge`

```python
class Edge:
    def __init__(self, from_node: int, to_node: int, weight: float):
        self.from_node: int = from_node
        self.to_node: int = to_node
        self.weight: float = weight
```

`class Edge:` declara un tipo nuevo, `Edge`, cuyos valores representan una arista. Cada `Edge` contiene tres atributos: `from_node`, `to_node` y `weight`. Para crear un objeto de la clase, se la llama como si fuera una función: `Edge(0, 3, 2.5)`. Esa llamada crea una instancia de `Edge` con los tres atributos ya establecidos, y ejecuta automáticamente `__init__`, el constructor de la clase, cuya función es recibir los argumentos y guardarlos como atributos del objeto. 

El programa que importa el módulo nunca llama a `__init__` directamente; solo escribe `Edge(...)` y Python se encarga del resto.

### La firma

```python
def __init__(self, from_node: int, to_node: int, weight: float):
```

- **`self`** es el objeto que se está construyendo. Python lo llena automáticamente, así que no hay que incluirlo entre los argumentos al llamar a `Edge`. Por eso la llamada `Edge(0, 3, 2.5)` lleva tres argumentos aunque la firma tenga cuatro parámetros.
- **`from_node`, `to_node`, `weight`** son los parámetros para los tres datos que un `Edge` necesita. Se pueden pasar por posición (`Edge(0, 3, 2.5)`) o por nombre (`Edge(from_node=0, to_node=3, weight=2.5)`).
- **`: int` y `: float`** son anotaciones de tipo. Son documentación para quien lee el código y para herramientas externas; Python no las verifica al ejecutar el programa. En este módulo aparecen tanto en la firma como en la línea del atributo, algo que parece redundante, pero cada anotación sirve a una herramienta distinta: la de la firma alimenta el autocompletado del editor cuando alguien llama a `Edge(...)`, y la del atributo permite que verificadores de tipos como `mypy` sepan qué contiene `e.from_node` sin rastrear el constructor. Sin embargo, se pueden omitir y el comportamiento no cambia:

```python
class Edge:
    def __init__(self, from_node, to_node, weight):
        self.from_node = from_node
        self.to_node = to_node
        self.weight = weight
```

### El cuerpo: los atributos

Cada línea del cuerpo de `__init__` tiene la forma `self.<atributo> = <valor>` y guarda un valor **dentro del objeto**, bajo un nombre propio.

```python
self.from_node: int = from_node
self.to_node: int = to_node
self.weight: float = weight
```

El `self.` es lo que ancla el valor al objeto. Sin `self.`, los tres parámetros son solo variables locales de `__init__` que existen mientras el constructor se ejecuta y desaparecen al terminar. Con `self.`, cada valor se guarda como atributo del objeto y sigue accesible como `e.from_node`, `e.to_node` y `e.weight` mientras el objeto exista.

Cada nombre de los parámetros aparece múltiples veces entre la firma y el cuerpo porque cumple tres roles distintos:

- En la firma, es el nombre del **parámetro** con el que `__init__` recibe el valor, y el que se puede usar al pasar el argumento por nombre (`Edge(from_node=0, ...)`).
- Después de `self.`, es el nombre del **atributo** al que se accede desde fuera como `e.from_node`.
- A la derecha del `=`, es una **referencia al parámetro**, es decir, el valor recibido.

Es importante entender la distinción entre los atributos y los parámetros. El parámetro se usa una sola vez, al construir el objeto, y el atributo se usa después, cada vez que el programa lee el objeto. Por eso sus nombres pueden coincidir sin conflicto, aunque también pueden ser distintos sin cambiar el objeto resultante. Que el autor los haya hecho coincidir es una decisión de conveniencia, no una obligación del lenguaje: mantener un solo nombre evita tener que recordar dos. El siguiente constructor produce objetos idénticos:

```python
def __init__(self, origen, destino, costo):
    self.from_node = origen
    self.to_node = destino
    self.weight = costo
```

La única diferencia es que `Edge(from_node=0, ...)` ya no funciona, porque el parámetro se llama `origen`, no `from_node`.

### Más decisiones de diseño

- **¿Por qué `Edge` y no una tupla `(to_node, weight)`?** Por legibilidad (`edge.weight` en vez de `graph[0][3][1]`), extensibilidad (agregar un atributo es una sola línea en `__init__`, no cambiar cada tupla e índice) e identidad (dos tuplas `(3, 2.5)` son iguales; dos `Edge` no, lo cual importa en colas de prioridad como las de Dijkstra).
- **¿Por qué se guarda `from_node`?** No es estrictamente necesario, ya que en una lista de adyacencia la arista sabe su origen por el nodo que la contiene. Se guarda para que la arista sea autocontenida, de modo que operaciones como `Graph.make_edge_list()` produzcan aristas independientes de sus nodos que, sin `from_node`, no permitirían reconstruir el grafo. Es un intercambio de memoria por conveniencia.
- **¿Por qué `Edge` no tiene métodos?** Porque es un contenedor de datos puro. Cada operación debe vivir en la clase que tiene la información para realizarla, así que agregar o eliminar aristas le corresponde a `Node`. Un método `remove()` en `Edge` tendría que saber en qué nodo está registrada la arista, es decir, dependería de `Node`, y eso la haría más difícil de pasar, copiar y leer de forma independiente.

---

## 2. La clase `Node`

Un `Node` representa un nodo del grafo junto con todas las aristas que salen de él. Su atributo central es un diccionario, `edges`, y casi todos sus métodos son una sola operación sobre ese diccionario. Aquí aparecen solo los fragmentos que se analizan; la clase completa está en el archivo `graphs.py`.

### El constructor `__init__`: qué va en la firma y qué va en el cuerpo

```python
def __init__(self, index: int, label=None):
    self.index: int = index
    self.edges: dict = {}
    self.label = label
```

La firma de `__init__` indica lo que hay que dar al crear un nodo. El parámetro `index` va en la firma porque cada nodo tiene uno distinto, y es la posición del nodo dentro del grafo. El parámetro `label=None` tiene un valor por defecto, así que es opcional, y se puede escribir `Node(3)` o `Node(3, label="rojo")`. La etiqueta sirve para guardar una característica del nodo, como su color en un grafo coloreado.

En cambio, `edges` no aparece en la firma porque todo nodo nuevo empieza sin aristas, así que la llamada a `Node(...)` no necesita proporcionar ningún valor para ese atributo. El constructor crea un diccionario vacío y las aristas se agregan después, una por una, con `add_edge`.

Hay además una razón técnica para evitar `def __init__(self, index, edges={})`. Python evalúa el valor por defecto una única vez, al procesar la definición de la función, y no en cada invocación. En consecuencia, toda llamada que omita el argumento `edges` —es decir, que no lo pase explícitamente— recibe la misma instancia de diccionario creada en la definición, de modo que una arista agregada a un nodo aparecería en todos los demás:

```python
a = Node(1)          # no pasa `edges` → usa el diccionario compartido
b = Node(2)          # no pasa `edges` → usa el MISMO diccionario compartido
a.edges["x"] = 1
print(b.edges)       # {'x': 1}  ← a.edges y b.edges son el mismo objeto
```

Al instanciar `{}` dentro del cuerpo del constructor, cada nodo recibe su propio diccionario y el estado queda correctamente aislado entre instancias.

### El diccionario `edges`

```python
def add_edge(self, neighbor: int, weight: float):
    self.edges[neighbor] = Edge(self.index, neighbor, weight)

def get_edge(self, neighbor: int) -> Union[Edge, None]:
    if neighbor in self.edges:
        return self.edges[neighbor]
    return None
```

Cada entrada del diccionario asocia el índice de un nodo vecino con el objeto `Edge` que representa la arista dirigida desde este nodo hacia dicho vecino. La clave es el índice del nodo destino y el valor es la instancia de `Edge` correspondiente. Por ejemplo, si el nodo 0 tiene aristas hacia los nodos 3 y 4, su diccionario de adyacencia contiene:

```python
{3: Edge(0, 3, 1.0), 4: Edge(0, 4, 3.0)}   # representación conceptual
```

Indexar por el nodo vecino permite recuperar la arista hacia un destino específico mediante `self.edges[neighbor]` en tiempo constante, sin necesidad de recorrer el conjunto de aristas. Esta es la razón por la que `get_edge` y `remove_edge` resultan tan concisos.

Esta decisión de diseño tiene una consecuencia relevante: dado que las claves de un diccionario son únicas, invocar `add_edge` dos veces con el mismo vecino hace que la segunda arista sobrescriba a la primera:

```python
node = Node(0)
node.add_edge(3, 1.0)
node.add_edge(3, 5.0)
node.num_edges()          # 1
node.get_edge(3).weight   # 5.0
```

En otras palabras, esta estructura no admite aristas múltiples (paralelas) entre un mismo par de nodos.

### Anotaciones de tipo en la firma

Las firmas usan anotaciones de tipo tanto en los parámetros (`neighbor: int`) como en el valor de retorno (`-> int`). En `get_edge`, `-> Union[Edge, None]` documenta que el método devuelve un `Edge` o `None` cuando no existe arista hacia el vecino. De ahí que `Graph.is_edge` compare con `is not None`.  `Union` proviene de `typing`, lo que explica el `from typing import Union` al inicio del archivo (en Python reciente, la misma anotación admite la forma `Edge | None`). 

`add_edge` y `remove_edge` omiten la anotación de retorno porque no devuelven valor: mutan el nodo. 

Como en el resto de Python, estas anotaciones no se verifican en tiempo de ejecución; son documentación para el lector y para herramientas de análisis estático.

### Temas para explorar más adelante

- **`add_edge` construye el `Edge`.** El método recibe solo el vecino y el peso; el campo `from_node` lo completa el propio nodo con `self.index`. Por eso `add_edge(3, 1.0)` basta para crear `Edge(0, 3, 1.0)`. Se retoma en el programa de DFS, donde el recorrido itera sobre los `Edge` ya construidos.
- **`get_sorted_edge_list`.** El diccionario preserva el orden de inserción; la variante ordenada da un orden de visita predecible y reproducible. Se cubre en detalle en el programa de DFS, y se reutiliza en BFS y en Dijkstra.
- **La revisión en `remove_edge`.** El método revisa `if neighbor in self.edges` antes de borrar, porque `del` con una llave inexistente produce un error. Se retoma en el programa de BFS, que discute las operaciones de mutación sobre el grafo ya construido.
- **Validación de índices.** `Node` no valida el índice del vecino porque no conoce el tamaño del grafo; esa responsabilidad recae en `Graph`. Se retoma en el programa de Dijkstra, donde la validación de índices y la construcción del grafo son pasos explícitos del preprocesamiento.

---

## 3. La clase `Graph`

La clase `Graph` es la capa de composición del módulo: no reimplementa la adyacencia, sino que administra una lista de objetos `Node` en la que cada nodo conserva su propio diccionario de aristas. La estructura de datos completa es, por tanto, un `list[Node]` en el que cada `Node` mapea índices de vecinos a objetos `Edge`.

```python
class Graph:
    def __init__(self, num_nodes: int, undirected: bool=False):
        self.num_nodes: int = num_nodes
        self.undirected: bool = undirected
        self.nodes: list = [Node(j) for j in range(num_nodes)]
```

El constructor establece dos invariantes que el resto del módulo presupone. Primero, los nodos se indexan de `0` a `num_nodes - 1`, y la posición de un nodo en `self.nodes` coincide con su índice: `self.nodes[i].index == i`. Segundo, el grafo se crea sin aristas; toda adyacencia se introduce después mediante `insert_edge`. La lista se construye con una comprensión que asigna a cada posición su índice, de modo que el invariante se cumple desde el inicio.

### Grafo dirigido y grafo no dirigido

El parámetro `undirected` determina la política de inserción y eliminación de aristas. Con el valor por omisión (`undirected=False`), el grafo es dirigido: `insert_edge(u, v, w)` agrega únicamente la arista `u → v`, y `get_edge(v, u)` devuelve `None` salvo que esa dirección se haya insertado de forma explícita. Con `undirected=True`, una sola llamada a `insert_edge(u, v, w)` agrega la arista en ambas direcciones, y `remove_edge` las elimina de la misma manera. En ambos casos se llama a `insert_edge` una sola vez por arista; la diferencia es que, en el modo no dirigido, el método agrega internamente la arista inversa.

```python
# Grafo dirigido (undirected=False, valor por omisión)
g = Graph(5)
g.insert_edge(0, 3, 1.0)
g.get_edge(0, 3)     # Edge(0, 3, 1.0)
g.get_edge(3, 0)     # None
```

```python
# Grafo no dirigido (undirected=True)
g = Graph(5, undirected=True)
g.insert_edge(0, 3, 1.0)   # una sola llamada
g.get_edge(0, 3)           # Edge(0, 3, 1.0)
g.get_edge(3, 0)           # Edge(3, 0, 1.0)
```

Conviene subrayar que la simetría de un grafo no dirigido no la garantiza la estructura de datos, sino los métodos de `Graph`. La comprobación `if self.undirected` vive únicamente en `Graph.insert_edge`; `Node.add_edge` no conoce ese atributo y se limita a agregar una arista a su propio diccionario. Por eso, si se invoca `g.nodes[u].add_edge(v, w)` directamente, se omite la comprobación y se puede construir un grafo declarado como no dirigido que en realidad tiene una sola dirección, sin que el módulo lo detecte. Los métodos de `Graph` son, por diseño, el punto de entrada previsto.

Cabe señalar, además, que las dos aristas de un par no dirigido son objetos `Edge` distintos, con `from_node` y `to_node` intercambiados. En consecuencia, al recolectar todas las aristas con `make_edge_list`, un grafo no dirigido con `m` aristas produce `2m` entradas, una por cada orientación. Esta distinción es relevante al construir listas de aristas y se retoma en la página de Dijkstra.

### Validación de índices

La validación de índices corresponde a `Graph`, no a `Node`. `insert_edge`, `remove_edge` y `get_edge` verifican que ambos índices se encuentren en el rango `0 ≤ i < num_nodes` y lanzan `IndexError` en caso contrario. `Node` no realiza esta comprobación porque no conoce el tamaño del grafo: un nodo aislado no tiene forma de determinar si un índice de vecino es válido. Esta división de responsabilidades concentra la verificación en la única clase que dispone de la información necesaria.

### `insert_node`

El método `insert_node` extiende el grafo en tiempo de ejecución. Crea un `Node` cuyo índice es el valor actual de `num_nodes`, lo agrega a `self.nodes` e incrementa el contador, con lo cual preserva el invariante de que la posición coincide con el índice.

Los métodos de recorrido y los algoritmos que consumen esta estructura, como `get_edge_list`, `get_sorted_edge_list`, el recorrido en profundidad, el recorrido en anchura y la búsqueda de caminos mínimos, se desarrollan en las páginas correspondientes. Esta sección se limita a la estructura y a sus invariantes; el comportamiento de los métodos en el contexto de un recorrido se presenta allí donde se utilizan.

---

## 4. Composición de clases

> *Sección pendiente de desarrollo.*

---

## 5. El archivo `test.py` (prueba del módulo)

> *Sección pendiente de desarrollo.*

---

## 6. Lo que este módulo aún no cubre

> *Sección pendiente de desarrollo.*

---

## Resumen: diccionarios vs. clases

Una comparación rápida entre usar las estructuras básicas de la sección **2. Estructuras de datos > Grafos** y usar el módulo `graphs.py`:

| Operación | Con diccionario / lista | Con `graphs.py` |
|-----------|-------------------------|-----------------|
| ¿Hay arista entre A y B? | `B in graph[A]` | `g.is_edge(A, B)` |
| Agregar arista | `graph[A].append(B)` | `g.insert_edge(A, B, w)` |
| Ver vecinos de A | `graph[A]` | `g.nodes[A].get_edge_list()` |
| Eliminar arista | `graph[A].remove(B)` | `g.remove_edge(A, B)` |
| Ver el peso de una arista | *Debe guardarse como tupla* `(B, w)` | `g.get_edge(A, B).weight` |
| Recorrer todas las aristas | `for u in graph: for v in graph[u]: ...` | `g.make_edge_list()` |
| Copia profunda | `copy.deepcopy(graph)` | `g.make_copy()` |
| Agregar un nodo nuevo | `graph[new_id] = []` | `g.insert_node("label")` |