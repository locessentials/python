---
layout: default
title: Algoritmos aleatorizados
parent: 3. Matemáticas y algoritmos
nav_order: 4
has_children: true
---

# Algoritmos aleatorizados

Ya vimos un algoritmo aleatorizado en una de las versiones de **Quicksort** que exploramos en la sección *Ordenamiento y búsqueda* de esta unidad. La implementación `qsr` (*quicksort random*) selecciona el pivote de manera aleatoria mediante `random.choice(a)`, a diferencia de `qsf` (*quicksort fixed*), que usa un pivote fijo (el último elemento de la lista).

Un **algoritmo aleatorizado** es un algoritmo que toma decisiones aleatorias en puntos determinados de su ejecución, como lanzar una moneda o generar un número al azar. Es decir, **el azar es interno al algoritmo, no a los datos de entrada**, y son las decisiones aleatorias las que determinan el flujo de control de cada ejecución del algoritmo. Si se ejecuta dos veces con la misma entrada, puede seguir caminos de ejecución distintos, tardar tiempos distintos o, en algunos casos, producir respuestas distintas.

En general, un algoritmo aleatorizado garantiza una respuesta correcta o un tiempo máximo de ejecución, pero no ambas cosas. Los **algoritmos Las Vegas** siempre producen la respuesta correcta, pero su tiempo de ejecución es aleatorio. Los **algoritmos Monte Carlo**, en cambio, siempre terminan dentro de un tiempo máximo determinado, pero existe una probabilidad pequeña de que su respuesta sea incorrecta.

El azar puede usarse de dos maneras en estos algoritmos: 
1. Puede intervenir dentro del algoritmo, mientras este procesa la entrada. 
2. O puede aplicarse a la entrada misma, que se permuta aleatoriamente antes de procesarla.

Los algoritmos aleatorizados aparecen en áreas como el ordenamiento y la búsqueda, las estructuras de datos, el muestreo de grandes volúmenes de datos, la criptografía y los sistemas distribuidos. Con frecuencia son más sencillos que los algoritmos deterministas (los que no usan azar) que resuelven el mismo problema, y a veces también son más rápidos.