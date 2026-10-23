---
layout: default
title: Complejidad
parent: 2. Estructuras de datos
nav_order: 1
---

# Complejidad (Big O)

La complejidad mide cómo crece el costo de un programa cuando crece la entrada (n). No mide segundos ni bytes exactos, porque eso depende de la computadora; mide cómo crece el costo.

## Temporal y espacial

- **Complejidad temporal:** cuántos pasos hace el programa según crece n
- **Complejidad espacial:** cuánta memoria tiene que guardar el programa según crece n: listas, diccionarios, tuplas, variables
- A veces solo se cuenta la memoria extra que el programa crea, sin contar la entrada; otras veces se cuenta todo lo que guarda, incluida la entrada
- Un programa puede ser rápido y usar mucha memoria, o lento y usar poca: por eso se miden por separado

## Notación O grande

O viene de "orden" (*order of*), y se llama notación O grande (*big O notation*). Cada complejidad de la lista dice qué tan rápido crece el costo. Se puede consultar "[Big-O Complexity Chart](https://www.bigocheatsheet.com)" (en inglés) para ver este crecimiento en forma gráfica.

### O(1), constante
El número de pasos no cambia con n; pueden ser varios pasos, pero siempre los mismos (ejemplos: sumar dos números, asignar una variable, comparar dos valores, `lista[5]`, `lista.append(x)`, `len(lista)`, buscar una clave en un diccionario).

### O(log n), logarítmica
`log n` es cuántas veces hay que dividir n entre 2 para llegar a 1: `log 16` = 4, porque 16 → 8 → 4 → 2 → 1, es lo contrario de una potencia: 2⁴ = 16, así que log de 16 = 4; crece muy despacio; si n se duplica, solo agrega un paso; ejemplo: búsqueda binaria: en una lista ordenada, se revisa el elemento de en medio y se quita la mitad donde no puede estar la respuesta; con 16 elementos son más o menos 4 pasos, y con 1,000,000, unos 20.

### O(n), lineal
El número de pasos crece igual que n, porque se visita cada elemento una vez; si n se duplica, los pasos se duplican (ejemplo: sumar todos los elementos de una lista con un `for`).

### O(n log n), lineal-logarítmica
Se hacen unos log n pasos por cada uno de los n elementos (en inglés: *for each of the n elements, you do about log n steps*), o sea, n × log n; crece un poco más rápido que lineal, pero mucho más despacio que n²; ejemplo: con 8 elementos, log 8 = 3 (8 → 4 → 2 → 1), así que 8 × 3 = 24 pasos; con 1,000,000: log 1,000,000 ≈ 20, así que 1,000,000 × 20 = unos 20,000,000 pasos (n² serían 1,000,000,000,000). Es la complejidad de los mejores algoritmos para ordenar comparando elementos.

- dividir y vencerás

### O(n²), cuadrática
Por cada uno de los n elementos, se revisan otra vez los n elementos, o sea, n × n. Para contar los pasos, se multiplica n por sí mismo: con 10 elementos son 10 × 10 = 100 pasos, y con 1,000 son 1,000 × 1,000 = 1,000,000. Por eso los pasos crecen mucho más rápido que la entrada: de 10 a 1,000 elementos, la lista se hizo 100 veces más grande, pero los pasos pasaron de 100 a 1,000,000, o sea, 10,000 veces más.

Un ejemplo de complejidad cuadrática: comparar cada elemento de una lista con todos los demás (para buscar repetidos), con un `for` dentro de otro `for` que recorren la misma lista.

### O(2ⁿ), exponencial
Se multiplica 2 por sí mismo n veces; se aplica cuando cada uno de los n elementos tiene dos opciones y se prueban todas las combinaciones; con 10 elementos son 2¹⁰ = 1,024 pasos, con 20 son más de 1,000,000, y con 50 son más de 1,000,000,000,000,000. Cada vez que n crece en 1, los pasos se duplican, porque cada combinación que ya había ahora se prueba dos veces: una con cada opción del elemento nuevo.

Por ejemplo: armar todos los subconjuntos posibles con A, B y C: A puede estar o no (2 opciones), B puede estar o no (2) y C puede estar o no (2), así que hay 2 × 2 × 2 = 8 grupos: ninguno, A, B, C, AB, AC, BC, ABC.

### O(n!), factorial
n! es multiplicar todos los números de n hasta 1: 4! = 4 × 3 × 2 × 1 = 24; cuando se ordenan n elementos, se multiplica así porque el primer lugar tiene n opciones, el segundo n − 1 (ya se usó una), el tercero n − 2, y así hasta 1; para ilustrar el crecimiento, con 10 elementos hay 3,628,800 pasos, y con 20 hay unos 2,400,000,000,000,000,000.

Un ejemplo: probar todos los órdenes posibles de n elementos; con 3 elementos (A, B, C) hay 3! = 6 órdenes: ABC, ACB, BAC, BCA, CAB, CBA

## Reglas para encontrarla

- **Pasos uno después de otro:** se queda solo la parte que crece más rápido, porque las demás casi no cuentan cuando n es grande: O(n) + O(n²) = O(n²) (el costo real es la suma de las partes)
- **Un ciclo dentro de otro:** se multiplican: un ciclo de n vueltas dentro de otro de m vueltas es O(n × m)
- **Se quitan las constantes:** O(3n) = O(n), porque las dos crecen igual
- **Se mide el peor caso:** la entrada que hace trabajar más al programa

## Costo de operaciones en Python

- `lista[i]`, `lista.append(x)`, `lista.pop()`: O(1)
- `lista.pop(0)`: O(n), porque recorre los demás elementos un lugar a la izquierda
- `x in lista`: O(n), porque revisa uno por uno
- `x in conjunto`, `diccionario[clave]`, `x in diccionario`: O(1) en promedio
- `sorted(lista)`, `lista.sort()`: O(n log n)

## ¿Cabe en el tiempo límite?

- Python hace más o menos 10⁷ operaciones simples por segundo (10,000,000)
- Para saber si una solución cabe, se ponen los límites del problema en la complejidad y se calcula el número de operaciones

## Para leer más

- Luis E. Vargas Azcona, [*Problemas y Algoritmos*](https://omegaup.com/docs/assets/libroluisvargas.pdf), capítulo 8 (libro de la Olimpiada Mexicana de Informática)
- Raúl Acosta Bermejo, CIC-IPN, [Conceptos básicos de análisis de algoritmos](https://www.cic.ipn.mx/~racostab/_downloads/c18afcb4aaeec821cd537fafae6b211a/ADA-U2-basics.pdf)
- [Tabla de complejidad de Python](https://wiki.python.org/moin/TimeComplexity) (en inglés)
