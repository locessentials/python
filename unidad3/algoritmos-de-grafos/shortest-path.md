---
layout: default
title: Ruta más corta
parent: Algoritmos de grafos
grandparent: 3. Matemáticas y algoritmos
nav_order: 3
---

# Ruta más corta desde un origen, con pesos no negativos (algoritmo de Dijkstra)

Los algoritmos de la ruta más corta (*shortest path*) encuentran en un grafo con pesos la ruta de menor costo entre dos nodos o desde un nodo de inicio hasta todos los demás. El costo de una ruta es la suma de los pesos de sus aristas, y esos pesos pueden representar distancia, tiempo, dinero o cualquier otra cantidad que se quiera minimizar. Algunos ejemplos de su uso son las aplicaciones de mapas que buscan la ruta más rápida, el enrutamiento de datos por los routers en internet y la búsqueda de los vuelos más baratos, aunque tengan más escalas.

## Concepto clave: relajar aristas (Edge Relaxation)

En el algoritmo de Dijkstra, mantenemos una lista con el **costo acumulado mínimo conocido** para ir desde el nodo de origen hasta cada uno de los demás nodos. Al inicio, como no conocemos ninguna ruta, estos costos se consideran infinitos (infinito).

Para encontrar la ruta más corta, evaluamos constantemente las aristas entre nodos. **Relajar una arista** entre un nodo A y un nodo B consiste en hacer una comparación muy simple:

1. Calculamos cuánto costaría llegar a B **pasando por A**:

`Nuevo costo = (Costo acumulado para llegar a A) + (Peso de la arista A -> B)`

2. **Comparación**: Si este `Nuevo costo` es menor que el **costo mínimo que teníamos guardado para B**, actualizamos el registro de B con este nuevo valor más bajo.

En resumen: relajar una arista es simplemente **actualizar la distancia de un nodo destino si encontramos una ruta más corta a través de un nodo vecino**.

## Explicación del programa

Esta sección sigue el programa paso a paso con un ejemplo, para mostrar cómo cambian `heap`, `costs` y `previous` hasta encontrar la ruta más corta a cada nodo. Usaremos este grafo, con el nodo 1 como nodo de inicio.

```
            (2)
          /     \
      24 /       \ 5
        /         \
     (1)-----3-----(3)
        \         /
      20 \       / 12
          \     /
            (4)
```

La entrada del programa describe el mismo grafo. El primer renglón da el número de nodos y el número de aristas, cada renglón siguiente da una arista con sus dos nodos y su peso, y el último renglón da el nodo de inicio.

```
4 5
1 2 24
1 4 20
3 1 3
4 3 12
2 3 5
1
```

[Ver el código en GitHub](https://github.com/locessentials/python/blob/main/unidad3/algoritmos-de-grafo/shortest-path.py)