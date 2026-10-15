---
layout: default
title: Problema G
grandparent: 4. Problemas
parent: ICPC 2017
nav_order: 7
---

# ICPC 2017 – Problema G: "traducción"

Se tiene una cuadrícula de celdas, donde el **w** y **h** son el ancho y la altura de la cuadrícula final. Cada celda está vacía (`.`) o llena (`#`), y hay al menos una celda llena en la primera renglón, en la última renglón, en la primera columna y en la última columna.

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

**Ejemplo 3**

```
cuadrícula final   quitar el error   deshacer el paso   salida
#....              .....             .....              #
..###              ..###             .....
..###              ..###             ...#.
..###              ..###             .....
```

**Límites**

- **Límite de tiempo:** 3 segundos
- 1 ≤ w ≤ 300, 1 ≤ h ≤ 300

## Panorama del código

### Pasos de la solución

1. Leer la cuadrícula y convertirla a 0 y 1.
2. Intentar deshacer un paso. **Deshacer** es encontrar la cuadrícula del paso anterior (ver *Cómo se deshace un paso*). **Revisar** es aplicar la regla a esa cuadrícula y compararla con la cuadrícula actual para contar las celdas diferentes.
   - **A. Deshacer sin arreglar nada:** deshacer y revisar. Pasa la revisión si hay 0 o 1 celdas diferentes:
     - **0 diferencias:** no hubo ningún error en este paso.
     - **1 diferencia:** esa celda es el error de este paso. La cuadrícula más pequeña es correcta, porque el error no se pasó a ella: al deshacer, el error se quitó.

     Si A pasa la revisión, se va directo al paso 3 y no se hace B.
   - **B. Arreglar un error:** si A no pasa, encontrar la celda candidata (el renglón más alto y la columna más a la izquierda con diferencias), cambiarla (de 0 a 1 o de 1 a 0), deshacer y revisar. Pasa la revisión si hay 0 celdas diferentes.
3. Si A o B pasa la revisión, quitar los bordes vacíos de la cuadrícula nueva y volver al paso 2 (solo si mide al menos 3 × 3).
4. Si ninguno pasa, terminar e imprimir la cuadrícula actual.

### Cómo se deshace un paso

Al deshacer, se busca la cuadrícula del paso anterior. Tiene 2 renglones y 2 columnas menos y está en el centro de la cuadrícula actual. Sus bordes están vacíos, porque en cada paso la figura crece una celda por cada lado.

Cada celda de la cuadrícula actual depende del área de 3 × 3 a su alrededor **en la cuadrícula anterior**. Por eso, para encontrar una celda de la cuadrícula anterior, se usa la celda de la cuadrícula actual que está en diagonal arriba a la izquierda. En el área de esa celda, la celda que se busca es la esquina inferior derecha, y las otras 8 ya se conocen.

- Si la celda actual está llena (`#`), el conteo del área debe ser impar.
- Si la celda actual está vacía (`.`), el conteo del área debe ser par.

En el código, esto es: `(valor actual + celdas llenas conocidas) % 2`.

Las celdas se encuentran una por una, de izquierda a derecha y de arriba abajo.

#### Ilustración: deshacer un paso

r = renglón, c = columna

```
cuadrícula actual      cuadrícula anterior
   c0 c1 c2 c3            c0 c1 c2 c3
r0 .  #  #  #          r0 .  .  .  .
r1 #  #  #  .          r1 .  ?  ?  .
r2 #  #  #  .          r2 .  ?  ?  .
r3 #  .  .  #          r3 .  .  .  .
```

**Paso 1:** usar (r0, c0) para encontrar (r1, c1).

(r0, c0) está vacía en la cuadrícula actual, así que el conteo de su área de 3 × 3 en la cuadrícula anterior debe ser par. Hay 0 celdas llenas conocidas, así que (r1, c1) debe quedar vacía.

```
área de 3 × 3 en la cuadrícula anterior
.  .  .    ← fuera de la cuadrícula
.  .  .    ← r0
.  .  ?    ← r1
```

```
cuadrícula actual      cuadrícula anterior
   c0 c1 c2 c3            c0 c1 c2 c3
r0 .  #  #  #          r0 .  .  .  .
r1 #  #  #  .          r1 .  .  ?  .
r2 #  #  #  .          r2 .  ?  ?  .
r3 #  .  .  #          r3 .  .  .  .
```

**Paso 2:** usar (r0, c1) para encontrar (r1, c2).

(r0, c1) está llena en la cuadrícula actual, así que el conteo de su área de 3 × 3 en la cuadrícula anterior debe ser impar. Hay 0 celdas llenas conocidas, así que (r1, c2) debe quedar llena.

```
área de 3 × 3 en la cuadrícula anterior
.  .  .    ← fuera de la cuadrícula
.  .  .    ← r0
.  .  ?    ← r1
```

```
cuadrícula actual      cuadrícula anterior
   c0 c1 c2 c3            c0 c1 c2 c3
r0 .  #  #  #          r0 .  .  .  .
r1 #  #  #  .          r1 .  .  #  .
r2 #  #  #  .          r2 .  ?  ?  .
r3 #  .  .  #          r3 .  .  .  .
```

**Paso 3:** usar (r1, c0) para encontrar (r2, c1).

(r1, c0) está llena en la cuadrícula actual, así que el conteo de su área de 3 × 3 en la cuadrícula anterior debe ser impar. Hay 0 celdas llenas conocidas, así que (r2, c1) debe quedar llena.

```
área de 3 × 3 en la cuadrícula anterior
.  .  .    ← r0
.  .  .    ← r1
.  .  ?    ← r2
```

```
cuadrícula actual      cuadrícula anterior
   c0 c1 c2 c3            c0 c1 c2 c3
r0 .  #  #  #          r0 .  .  .  .
r1 #  #  #  .          r1 .  .  #  .
r2 #  #  #  .          r2 .  #  ?  .
r3 #  .  .  #          r3 .  .  .  .
```

**Paso 4:** usar (r1, c1) para encontrar (r2, c2).

(r1, c1) está llena en la cuadrícula actual, así que el conteo de su área de 3 × 3 en la cuadrícula anterior debe ser impar. Ya hay 2 celdas llenas conocidas, (r1, c2) y (r2, c1). Como 2 es par, (r2, c2) debe quedar llena para que el conteo sea 3.

```
área de 3 × 3 en la cuadrícula anterior
.  .  .    ← r0
.  .  #    ← r1
.  #  ?    ← r2
```

```
cuadrícula actual      cuadrícula anterior
   c0 c1 c2 c3            c0 c1 c2 c3
r0 .  #  #  #          r0 .  .  .  .
r1 #  #  #  .          r1 .  .  #  .
r2 #  #  #  .          r2 .  #  #  .
r3 #  .  .  #          r3 .  .  .  .
```

Para encontrar la cuadrícula anterior solo se usaron 4 celdas de la cuadrícula actual: (r0, c0), (r0, c1), (r1, c0) y (r1, c1). Las otras 12 se usan después, al revisar con `step_forward` y `find_differences`.

### Ilustración: encontrar y arreglar el error

| | A. con error | B. paso 2A: deshacer sin arreglar | C. paso 2B: cambiar la candidata y deshacer |
| --- | --- | --- | --- |
| cuadrícula | .###<br>#.#.<br>###.<br>#..# | .###<br>#.#.<br>###.<br>#..# | .###<br>###.<br>###.<br>#..# |
| step_backward | | ....<br>..#.<br>.#..<br>.... | ....<br>..#.<br>.##.<br>.... |
| conteo | | 0 1 1 1<br>1 2 2 1<br>1 2 2 1<br>1 1 1 0 | 0 1 1 1<br>1 3 3 2<br>1 3 3 2<br>1 2 2 1 |
| step_forward | | .###<br>#..#<br>#..#<br>###. | .###<br>###.<br>###.<br>#..# |
| diferencias | | ....<br>..XX<br>.XXX<br>.XXX | ....<br>....<br>....<br>.... |
| resultado | | más de 1 diferencia: no pasa | 0 diferencias: pasa |
| candidata | | la esquina superior izquierda del área con X en la cuadrícula de diferencias | se cambia la candidata (de `.` a `#`) antes de deshacer |

- Si se deshace el paso empezando por la esquina superior izquierda, las diferencias se extienden hacia la derecha y hacia abajo desde el error, así que el error está en la esquina superior izquierda del área con diferencias.
- Si se empezara por la esquina inferior derecha, las diferencias se extenderían hacia la izquierda y hacia arriba, y el error estaría en la esquina inferior derecha del área con diferencias.

La regla es: el error está donde empiezan las diferencias, del lado donde se empezó a deshacer.

### Funciones auxiliares

- `read_grid`: convierte las líneas de `.` y `#` en una lista de listas de 0 y 1
- `step_backward`: deshace un paso, encontrando las celdas una por una desde la esquina superior izquierda; devuelve una cuadrícula 2 más pequeña en cada dirección
- `step_forward`: aplica la regla una vez a la cuadrícula que devuelve `step_backward`; devuelve una cuadrícula 2 más grande en cada dirección, que `find_differences` compara con la cuadrícula que se deshizo para revisar si el paso hacia atrás es correcto
- `find_differences`: compara dos cuadrículas del mismo tamaño y devuelve las celdas diferentes
- `find_candidate`: con las celdas diferentes, devuelve la celda candidata (renglón más alta, columna más a la izquierda)
- `trim_grid`: quita las renglones y columnas vacías de los bordes
- `print_grid`: convierte 1 y 0 en `#` y `.` e imprime la cuadrícula

## Análisis

### Construcción del algoritmo

1. Leer `w`, `h` y la cuadrícula, y convertir `.` y `#` a 0 y 1.
2. Mientras la cuadrícula mida al menos 3 × 3, intentar deshacer un paso:
   - **A:** deshacer y revisar. Pasa si hay 0 o 1 diferencias.
   - **B:** si A no pasa, cambiar la celda candidata, deshacer y revisar. Pasa si hay 0 diferencias.
3. Si A o B pasa, quitar los bordes vacíos y volver al paso 2.
4. Si ninguno pasa, imprimir la cuadrícula actual.

La idea clave: la regla solo depende de si el conteo es par o impar. Por eso, al deshacer, las celdas se pueden encontrar una por una: en el área de 3 × 3 de cada celda solo falta una celda por conocer.

### Variables y tipos de datos

- `w`, `h` (`int`): el ancho y la altura de la cuadrícula; se leen de la primera línea.
- cada celda (`int`, 0 o 1): se usa `int` en vez de `str` porque hay que sumar las celdas llenas y usar `% 2`. Con `.` y `#` no se puede sumar directamente.
- el conteo de celdas llenas (`int`, de 0 a 9): con `% 2` se sabe si es par o impar.
- la candidata (tupla de dos `int`): el renglón y la columna de la celda que se cambia en B.
- el resultado de la revisión (`bool`): si A o B pasa, se sigue deshaciendo; si no, se termina.
- las líneas de entrada y salida (`str`): solo al leer y al imprimir.
- No se usa `float`, porque no hay divisiones ni decimales.

### Estructuras de datos

- **Lista de listas (matriz)** para la cuadrícula: se llega a cualquier celda directamente con `grid[renglón][columna]`, en tiempo constante. Es la forma natural de guardar una cuadrícula.
- **Lista de tuplas** para las celdas diferentes: solo hay que contarlas (0, 1 o más) y encontrar el renglón más alto y la columna más a la izquierda. Para eso basta una lista.
- **Tupla** para la candidata: son dos valores que van juntos y no cambian.
- No se necesitan diccionarios, conjuntos, colas, montículos ni grafos: no hay que buscar por clave, quitar repetidos, procesar por orden de llegada o de prioridad, ni guardar conexiones. Las vecinas de cada celda ya se conocen por su posición en la matriz.

### Paradigma algorítmico

- El problema es un **autómata celular** (*cellular automaton*) con una regla de paridad. La solución es una **simulación hacia atrás**: se deshacen los pasos uno por uno.
- La decisión en cada paso es **voraz** (*greedy*): se toma la primera opción que pasa la revisión (A antes que B) y no se vuelve atrás. Cada paso deshecho hace la figura más pequeña, y el problema pide la más pequeña, así que conviene deshacer todos los pasos que se puedan.
- No es fuerza bruta: probar a cambiar cada celda serían `w × h` intentos en cada paso. Con la candidata solo se hace un intento, porque el error está donde empiezan las diferencias.

### Estilo de programación

Procedural (imperativo), con funciones pequeñas que hacen una sola tarea cada una: `read_grid`, `step_backward`, `step_forward`, `find_differences`, `find_candidate`, `trim_grid` y `print_grid`. Así es fácil probar cada parte por separado y explicar el algoritmo paso a paso. No hace falta programación orientada a objetos: solo hay un tipo de dato, la cuadrícula, y las funciones trabajan sobre ella.

### Iterativo o recursivo

Iterativo:

- un ciclo `while` que deshace pasos mientras A o B pasen
- dos ciclos `for` (renglones por fuera, columnas por dentro) para recorrer la cuadrícula

El orden importa: cada celda usa las que ya se encontraron (arriba y a la izquierda), y los ciclos recorren la cuadrícula justo en ese orden. La recursión no ayuda aquí, porque no hay un árbol ni un grafo, solo una cadena de pasos.

### Complejidad

- **Temporal:** en cada paso se recorre la cuadrícula unas pocas veces: deshacer, aplicar la regla, comparar, y lo mismo otra vez si se hace B. Eso cuesta O(w · h) por paso. Como la cuadrícula pierde 2 renglones y 2 columnas en cada paso, hay como máximo min(w, h) / 2 pasos, es decir, 150. En total: O(w · h · min(w, h)). Como la cuadrícula se hace más pequeña en cada paso, en el peor caso (300 × 300) son unos 4.5 millones de celdas por tipo de recorrido, sumando todos los pasos.
- **La operación que más pesa** es `step_forward`, porque para cada celda cuenta las 9 celdas de su área.
- **Espacial:** O(w · h), porque solo se guardan unas pocas cuadrículas a la vez: la actual, la anterior, la que devuelve `step_forward` y las diferencias.
