---
layout: default
title: Algoritmos de grafos
parent: 3. Matemáticas y algoritmos
nav_order: 4
has_children: true
---

# Algoritmos de grafos

- BFS (with connected components)
- DFS (with connected components)
- caminos más cortos
  - Dijkstra: caminos más cortos desde un origen, con pesos no negativos
  - Bellman-Ford: caminos más cortos desde un origen, con pesos negativos permitidos
  - Floyd-Warshall: caminos más cortos desde todos los orígenes (tabla completa), con pesos negativos permitidos
- árbol de expansión mínima - connecting all the nodes using the cheapest set of edges (greedy algorithm)
  - Prim: hace crecer el árbol desde un nodo, agregando cada vez la arista más barata que lo une con un nodo nuevo
  - Kruskal: revisa las aristas de la más barata a la más cara y agrega cada una que no forme un ciclo
- orden topológico: ordering tasks so each one comes after everything it depends on, in a directed graph with no cycles, the tasks have no times; built on DFS
- emparejamiento bipartito
