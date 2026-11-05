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
- **`: int` y `: float`** son anotaciones de tipo. Son documentación para quien lee el código y para herramientas externas; Python no las verifica al ejecutar el programa. En este módulo aparecen tanto en la firma como en la línea del atributo, algo que parece redundante, pero cada anotación sirve a una herramienta distinta: la de la firma alimenta el autocompletado del editor cuando alguien llama a `Edge(...)`, y la del atributo permite que verificadores de tipos como `mypy` sepan qué contiene `e.from_node` sin rastrear el constructor. Sin embargo, se pueden omitir y el comportamiento no cambia.

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

> *Sección pendiente de desarrollo.*

---

## 3. La clase `Graph`

> *Sección pendiente de desarrollo.*

---

## 4. Composición de clases

> *Sección pendiente de desarrollo.*

---

## 5. El archivo `main.py` (prueba del módulo)

> *Sección pendiente de desarrollo.*

---

## 6. Lo que este módulo aún no cubre

> *Sección pendiente de desarrollo.*

---

## Resumen: diccionarios vs. clases

Una comparación rápida entre usar las estructuras básicas de la sección **2. Estructuras de datos > Grafos** y usar el módulo `graphs.py`:

| Operación | Con diccionario / lista | Con `graphs.py` |
|---|---|---|
| ¿Hay arista entre A y B? | `B in graph[A]` | `g.is_edge(A, B)` |
| Agregar arista | `graph[A].append(B)` | `g.insert_edge(A, B, w)` |
| Ver vecinos de A | `graph[A]` | `g.nodes[A].get_edge_list()` |
| Eliminar arista | `graph[A].remove(B)` | `g.remove_edge(A, B)` |
| Ver el peso de una arista | *Debe guardarse como tupla* `(B, w)` | `g.get_edge(A, B).weight` |
| Recorrer todas las aristas | `for u in graph: for v in graph[u]: ...` | `g.make_edge_list()` |
| Copia profunda | `copy.deepcopy(graph)` | `g.make_copy()` |
| Agregar un nodo nuevo | `graph[new_id] = []` | `g.insert_node("label")` |
```