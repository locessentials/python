---
layout: default
title: Introducción
parent: Algoritmos de grafos
grandparent: 3. Matemáticas y algoritmos
nav_order: 1
---

# Introducción

## El problema de los siete puentes de Königsberg

El problema de los siete puentes de Königsberg es considerado el origen de la **Teoría de Grafos**. A principios del siglo XVIII, la ciudad de Königsberg (actualmente Kaliningrado, Rusia) estaba dividida por el río Pregel en cuatro zonas de tierra, conectadas por siete puentes. El problema consistía en encontrar una ruta para caminar por la ciudad cruzando **cada uno de los siete puentes exactamente una vez**. 

En 1736, Leonhard Euler demostró que esto era imposible, no por falta de ingenio, sino porque la estructura matemática de la red lo impedía. Para demostrarlo, hizo un proceso de **abstracción** en que ignoró las distancias y los tamaños, y solo conservó lo esencial (las zonas de tierra y los puentes).

```
                MAPA                                GRAFO

                A                              (A)
  ~~~~~~~║~~~~~║~~~~~~~~~~║~~~~~             //   \
  ~~┌─────────────┐~~~┌─────────           //       \
  ~~│      B      ╞═══╡    D              (B)───────(D)
  ~~└─────────────┘~~~└─────────           \\       /
  ~~~~~~~║~~~~~║~~~~~~~~~~║~~~~~             \\   /
                C                              (C)
```

*El grafo de Königsberg es un **multigrafo**: hay dos puentes que conectan B y D, y dos que conectan B y C.*

---

## Definiciones básicas

Para resolver el problema, Euler definió los siguientes conceptos que aún usamos hoy:

- **grafo formal:** grafo se define matemáticamente como un par ordenado **G = (V, E)**, donde **V** es el conjunto de vértices (nodos) y **E** es una colección de aristas; en un grafo simple, cada arista es un par de vértices (**E ⊆ V × V**), pero en un multigrafo puede haber múltiples aristas entre el mismo par
- **nodo / vértice:** entidad; en el problema de los siete puentes, las cuatro zonas de tierra (A, B, C, D)
- **arista / lado:** conexión entre dos nodos; en el problema, los puentes
- **grado (*degree*):** número de aristas que tocan (inciden, consulta *incidencia* abajo) en un nodo; por convención, un bucle cuenta como dos aristas para el grado
- **incidencia (*incidence*):** cuando una arista toca a un nodo
- **adyacencia (*adjacency*):** dos nodos son adyacentes (o vecinos) si están unidos por la misma arista
- **bucle (*self-loop*):** arista que conecta un nodo consigo mismo, de la forma `(A, A)`
- **peso (*weight*):** número asociado con una arista que representa su costo, distancia o tiempo

*(Nota: Para ver los tipos de grafos como dirigidos, no dirigidos, simples o multigrafos, y cómo se implementan en código, visita la sección **2. Estructuras de datos > Grafos**).*

---

## El lema del apretón de manos (*Handshaking Lemma*)

Al observar el grafo de Königsberg y sumar los grados de todos sus nodos (2+5+3+3 = 13), obtenemos un número impar. Esto nos lleva a un lema fundamental de los grafos no dirigidos:

**La suma de los grados de todos los vértices de un grafo no dirigido (simple o multigrafo) es igual al doble del número de aristas.**

A esta equivalencia fundamental se le denomina el lema del apretón de manos (*Handshaking Lemma*), y la analogía que da origen a su nombre ilustra su demostración: cada arista equivale a un apretón de manos entre dos personas (los nodos), de modo que cada interacción contribuye con dos unidades al total de los grados.

En notación matemática: **Σ grado(v) = 2\|E\|** (Traducción: la suma de los grados de todos los vértices es igual al doble del número de aristas)

### Demostración por Inducción

Podemos demostrar que esto se cumple para cualquier grafo no dirigido usando inducción sobre el número de aristas *e*.

- **Caso base (*e* = 0):** Un grafo sin aristas tiene todos sus nodos con grado 0. La suma de los grados es 0, y 2(0) = 0. Se cumple.
- **Paso inductivo:** Supongamos que la fórmula se cumple para cualquier grafo con *k* aristas (Hipótesis de Inducción). 
  Ahora tomemos un grafo *G* con *k* + 1 aristas. Si quitamos una arista *a* = (*u*, *v*), donde *u* y *v* son los dos nodos que conecta esa arista, el grafo restante *G'* tiene *k* aristas. Por la hipótesis, la suma de los grados en *G'* es 2*k*.
  Al volver a agregar la arista *a*, ambos extremos (*u* y *v*) aumentan su grado en 1. Por lo tanto, la suma total de los grados aumenta en 2.
  Así que la suma para *G* es 2*k* + 2 = 2(*k* + 1). La fórmula se cumple.

---

## Número máximo de aristas en un grafo simple

En un **grafo simple** con *n* nodos, el número máximo de aristas se alcanza cuando todos los nodos están conectados entre sí (un **grafo completo**). La fórmula para el número de aristas es:

**\|E\| = n(n - 1) / 2**

### Demostración por Inducción
Vamos a demostrar que un grafo completo de *n* nodos tiene *n*(*n*-1)/2 aristas.

- **Caso base (*n* = 1):** Un grafo con 1 solo nodo no tiene aristas. Evaluando la fórmula: 1(1-1)/2 = 0. Se cumple.
- **Paso inductivo:** Supongamos que un grafo completo de *k* nodos tiene *k*(*k*-1)/2 aristas. 
  Para construir un grafo completo de *k* + 1 nodos, tomamos el grafo de *k* nodos y agregamos un nodo nuevo. Este nodo nuevo debe conectarse a todos los *k* nodos existentes para que el grafo sea completo. Por lo tanto, agregamos *k* aristas nuevas.
  El número total de aristas será el anterior más las nuevas:
  
  *k*(*k* - 1)/2 + *k* = (*k*² - *k* + 2*k*)/2 = (*k*² + *k*)/2 = *k*(*k* + 1)/2
  
  Y como *k* + 1 es nuestro nuevo *n*, la fórmula se cumple para *n*.