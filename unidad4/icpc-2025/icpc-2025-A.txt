---
layout: default
title: Problem A
grandparent: 4. Problemas
parent: ICPC 2025
nav_order: 1
---

# ICPC 2025 - Problem A

## Resumen del problema

- **heap** – tree-based data structure in which every node's value is ordered relative to its children's (in a min-heap, each parent is less than or equal to its children), so the smallest (or largest) value is always at the root
- **skew heap** – self-adjusting heap stored as a binary tree with no shape or balance constraints, where merging two heaps swaps the children of nodes along the merge path to keep operations efficient over time
- **integer skew heap** – skew heap whose nodes store integer values
- **binary tree** – tree in which each node has at most two children, called the left child and the right child
- **complete binary tree** – tree in which all levels of the tree, except possibly the last one (deepest) are fully filled, and, if the last level of the tree is not complete, the nodes of that level are filled from left to right
- **perfect binary tree** – binary tree in which every internal node has exactly two children and all leaves are at the same depth, so a tree of height h has 2^(h+1) − 1 nodes

**Note:** the skew heap need not be a perfect binary tree; that is, the left and/or right subtree of any node may be empty.

Inserting a value x into a skew heap H is done using the following recursive procedure:
- If H is empty, make H a skew heap consisting of a single node containing x.
- Otherwise, let y be the value in the root of H.
    - If y < x, swap the two children of the root and recursively insert x into the new left subtree.
    - If y ≥ x, create a new node with value x and make H the left subtree of this node.

ℓi and ri (i < ℓi ≤ n or ℓi = 0; i < ri ≤ n or ri = 0)

Problems for practicing heaps

https://www.geeksforgeeks.org/dsa/heap-data-structure/

Advanced Data Structures

https://www.geeksforgeeks.org/dsa/advanced-data-structures/

https://www.cs.usfca.edu/~galles/visualization/SkewHeap.html
