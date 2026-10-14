---
layout: default
title: Problema G
grandparent: 4. Problemas
parent: ICPC 2017
nav_order: 7
---

# ICPC 2017 – Problema G: Replicate Rfplicbte

## Problema

Se tiene una cuadrícula de celdas, donde el **w** y **h** son el ancho y la altura de la cuadrícula final. Cada celda está vacía (`.`) o llena (`#`), y hay al menos una celda llena en la primera fila, en la última fila, en la primera columna y en la última columna.

Una figura inicial cambia por pasos. En cada paso, todas las celdas cambian al mismo tiempo según estas reglas:

1. Cada celda cuenta cuántas celdas llenas hay entre ella misma y sus 8 celdas vecinas (arriba, abajo, izquierda, derecha y las 4 diagonales). En total revisa 9 celdas.
2. Si el número es impar (1, 3, 5, 7 o 9), la celda queda llena al terminar el paso.
3. Si el número es par (0, 2, 4, 6 u 8), la celda queda vacía al terminar el paso.

Después de cada paso, **como máximo una** celda puede cambiar de estado por error, de vacía a llena o de llena a vacía. También es posible que en un paso no haya ningún error.

Dada la cuadrícula final, hay que encontrar la figura inicial más pequeña (y no vacía) que pudo haber producido esa cuadrícula. Es decir, hay que:

1. Empezar con la cuadrícula final.
2. Deshacer un paso a la vez. En cada paso, muchas celdas cambian por la regla de par e impar. Además, después de cada paso, como máximo una celda pudo haber cambiado por error. Al deshacer un paso, hay que tomar en cuenta ese posible error.
3. Repetir hasta que ya no se pueda deshacer otro paso.
4. Imprimir la figura que queda.

### Ejemplo 3

```
cuadrícula final   quitar el error   deshacer el paso   salida
#....              .....             .....              #
..###              ..###             .....
..###              ..###             ...#.
..###              ..###             .....
```

### Límites

- **Límite de tiempo:** 3 segundos
- 1 ≤ w ≤ 300, 1 ≤ h ≤ 300

## Panorama del código

### Pasos de la solución

1. Leer la cuadrícula y convertirla a 0 y 1.
2. Intentar deshacer un paso:
   - **A. Deshacer sin arreglar nada:** deshacer y revisar. Si A pasa la revisión, se va directo al paso 3 y no se hace B. Pasa la revisión si hay 0 o 1 celdas diferentes:
     - **0 diferencias:** no hubo ningún error en este paso.
     - **1 diferencia:** esa celda es el error de este paso. La cuadrícula más pequeña es correcta, porque el error no se pasó a ella: al deshacer, el error se quitó.
   - **B. Arreglar un error:** encontrar la celda candidata (la fila más alta y la columna más a la izquierda con diferencias), cambiarla (de 0 a 1 o de 1 a 0), deshacer y revisar. Pasa la revisión si hay 0 celdas diferentes.
3. Si A o B pasa la revisión, quitar los bordes vacíos de la cuadrícula nueva y volver al paso 2 (solo si mide al menos 3 × 3).
4. Si ninguno pasa, terminar e imprimir la cuadrícula actual.

| antes | actualización | con error |
| ----- | ------------- | --------- |
| .#<br>## | .####<br>###.<br>###.<br>#..# | .####<br>#.#.<br>###.<br>#..# |
| | | |




### Funciones auxiliares

- `read_grid`: convierte las líneas de `.` y `#` en una lista de listas de 0 y 1
- `step_backward`: deshace un paso, encontrando las celdas una por una desde la esquina superior izquierda; devuelve una cuadrícula 2 más pequeña en cada dirección
- `step_forward`: aplica la regla una vez a la cuadrícula que devuelve `step_backward`; devuelve una cuadrícula 2 más grande en cada dirección, que `find_differences` compara con la cuadrícula que se deshizo para revisar si el paso hacia atrás es correcto
- `find_differences`: compara dos cuadrículas del mismo tamaño y devuelve las celdas diferentes
- `find_candidate`: con las celdas diferentes, devuelve la celda candidata (fila más alta, columna más a la izquierda)
- `trim_grid`: quita las filas y columnas vacías de los bordes
- `print_grid`: convierte 1 y 0 en `#` y `.` e imprime la cuadrícula
