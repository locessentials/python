---
layout: default
title: Permutaciones y combinaciones
parent: 3. Matemáticas y algoritmos
nav_order: 3
has_children: true
---

# Permutaciones y combinaciones

El estudio de las permutaciones y la combinatoria constituye uno de los pilares fundamentales de la matemática discreta y tiene aplicaciones directas en el diseño de algoritmos, el análisis de complejidad y la resolución de problemas computacionales. Esta sección establece los conceptos esenciales que conectan la teoría matemática con su implementación práctica en Python.

---

## Permutaciones

Una permutación de un conjunto finito es una reorganización de sus elementos en una secuencia específica. Formalmente, una permutación del conjunto `X = {1, 2, ..., n}` se define como una función biyectiva `σ: X → X`, donde el dominio y el codominio son el mismo conjunto. Esto significa que cada elemento del dominio se asigna de manera única a un elemento del codominio, y como ambos conjuntos son idénticos, la función simplemente reordena los elementos dentro del mismo conjunto.

El conjunto de todas las permutaciones de `n` elementos forma un grupo bajo la operación de composición. En matemáticas, un grupo no es una colección cualquiera de objetos, sino una estructura que debe cumplir cuatro propiedades fundamentales.

1. **Clausura.** Al componer dos permutaciones cualesquiera, el resultado es otra permutación que ya pertenece al conjunto.
2. **Asociatividad.** El orden en que se agrupan tres permutaciones al componerlas no altera el resultado, es decir, `(σ ∘ τ) ∘ ρ = σ ∘ (τ ∘ ρ)`.
3. **Elemento identidad.** Existe una permutación que no altera ningún elemento y que actúa como neutro al componerse con cualquier otra.
4. **Elemento inverso.** Toda permutación posee una permutación inversa que deshace su efecto y devuelve el conjunto a su estado original.

Este grupo se denomina **grupo simétrico de grado n** y se denota como `Sₙ`. El número total de permutaciones distintas de n elementos viene dado por el factorial de n, es decir, `|Sₙ| = n!`.

### Notación de dos líneas

Una permutación puede representarse mediante la notación de dos líneas, en la cual la primera fila contiene los elementos en su orden original y la segunda fila indica la posición que ocupa cada elemento después de la permutación.

σ = ( 1  2  3  ...  n )  
    ( i₁ i₂ i₃ ...  iₙ )

En esta representación, cada columna indica que el elemento de la primera fila se transforma en el elemento correspondiente de la segunda fila. La condición de biyectividad exige que todos los elementos de la segunda fila sean distintos entre sí.

### Composición de permutaciones

La composición de dos permutaciones `σ` y `τ` se define como la aplicación sucesiva de ambas funciones. Primero se aplica una permutación y luego la otra. En general, el resultado depende del orden en que se apliquen, es decir, `σ ∘ τ ≠ τ ∘ σ`.

**Nota:** En el contexto de la teoría de grupos, se utiliza la letra griega **σ (sigma)** para denotar una permutación individual, en lugar de las letras habituales para funciones `f` o `g`. Cuando se requiere una segunda permutación, se utiliza la letra griega **τ (tau)**. Esta convención permite distinguir claramente las funciones que representan permutaciones de otras funciones matemáticas.

Para ilustrar esta propiedad, consideremos el conjunto [1, 2, 3] y dos permutaciones específicas. La permutación σ intercambia el primer y el segundo elemento, mientras que la permutación τ intercambia el segundo y el tercero.

| Aplicar τ y luego σ | Aplicar σ y luego τ |
| :--- | :--- |
| Inicio [1, 2, 3] | Inicio [1, 2, 3] |
| Aplicar τ (intercambiar posiciones 2 y 3) [1, 3, 2] | Aplicar σ (intercambiar posiciones 1 y 2) [2, 1, 3] |
| Aplicar σ (intercambiar posiciones 1 y 2) [3, 1, 2] | Aplicar τ (intercambiar posiciones 2 y 3) [2, 3, 1] |
| **Resultado [3, 1, 2]** | **Resultado [2, 3, 1]** |

Los resultados son distintos, lo que demuestra que el orden de aplicación altera el resultado final.

Es importante distinguir entre generar el conjunto completo de permutaciones y aplicar una secuencia de transformaciones. Si el objetivo es enumerar todas las permutaciones posibles de un conjunto, el orden en que se generan es irrelevante, pues al final se obtiene la colección completa. Sin embargo, cuando se aplican permutaciones como transformaciones sucesivas sobre un conjunto de datos, el orden sí altera el resultado final. Esta distinción resulta relevante en áreas como la criptografía y el procesamiento de datos, donde las transformaciones se encadenan y el orden de las operaciones determina el resultado del sistema.

---

## Paridad de permutaciones

Toda permutación puede descomponerse en una secuencia de transposiciones, donde una transposición es el intercambio de dos elementos. El número de transposiciones necesarias para construir una permutación determina su **paridad**.

Una permutación se denomina **par** si puede expresarse como el producto de un número par de transposiciones y su signo es `+1`. Se denomina **impar** si requiere un número impar de transposiciones y su signo es `−1`. Esta clasificación se formaliza mediante la función signo, denotada como `sgn(σ)`.

El conjunto de todas las permutaciones pares de `n` elementos forma un subgrupo de `Sₙ` denominado **grupo alternante** y se denota como `Aₙ`. Dado que las permutaciones pares e impares se distribuyen en partes iguales, el orden de `Aₙ` es exactamente la mitad del orden de `Sₙ`, es decir, `n!/2`.

La paridad de una permutación tiene una aplicación directa en el diseño de algoritmos de búsqueda y verificación. Su valor principal es que actúa como una suma de comprobación de un solo bit para el orden de una secuencia. Si se conoce la paridad esperada de una configuración, cualquier estado con la paridad opuesta es matemáticamente inalcanzable. Esto permite descartar exactamente la mitad de todos los estados posibles antes de iniciar una búsqueda costosa. En un sistema con diez elementos, por ejemplo, existen 3,628,800 ordenaciones posibles. Si la paridad esperada es par, 1,814,400 de esas ordenaciones son imposibles y pueden ignorarse sin examinarlas. 

La paridad no resuelve el problema por sí sola, pero reduce el espacio de búsqueda a la mitad con una operación de costo mínimo, es decir, la complejidad.

---

## Combinaciones

Mientras que las permutaciones consideran el orden de los elementos, las combinaciones se ocupan de la selección de un subconjunto de elementos sin importar su orden. Una combinación de `k` elementos tomados de un conjunto de `n` elementos es una selección de `k` elementos distintos sin considerar la secuencia en que se eligen.

El número de combinaciones posibles se calcula a partir del número de permutaciones dividiendo por las posibles ordenaciones de los `k` elementos seleccionados. La fórmula es la siguiente, donde `C` representa el número posible de combinaciones.

C(n, k) = n! / (k! × (n − k)!)

La fórmula calcula cuántos subconjuntos distintos de `k` elementos se pueden formar a partir de un conjunto de n elementos. El numerador `n!` representa todas las formas posibles de ordenar los `n` elementos. El denominador elimina los casos que no nos interesan mediante dos factores. El factor `(n − k)!` cancela las ordenaciones de los elementos que no fueron seleccionados. El factor `k!` elimina las permutaciones duplicadas que contienen los mismos elementos en distinto orden de las que sí fueron seleccionados (por ejemplo: [A, B], [B, A]), ya que en una combinación el orden no importa. El resultado final es el número de grupos únicos que se pueden formar.

Esta relación establece que las combinaciones son un caso derivado de las permutaciones y permite comprender por qué ambos conceptos se agrupan bajo el término general de combinatoria.

---

## Combinatoria

La **combinatoria** es la rama de la matemática que estudia la enumeración, la construcción y la existencia de configuraciones de elementos que satisfacen determinadas condiciones. Tanto las permutaciones como las combinaciones son objetos de estudio de la combinatoria, junto con otros conceptos como el teorema del binomio, el triángulo de Pascal y los principios de conteo.

En el contexto de la programación, la combinatoria proporciona las bases teóricas para el diseño de algoritmos de búsqueda exhaustiva, la generación de casos de prueba y el análisis de la complejidad de determinados problemas. Su dominio resulta esencial para abordar de manera rigurosa los desafíos computacionales que involucran la exploración sistemática de un espacio de soluciones.

---

## Implementación en Python

El módulo `itertools` de la biblioteca estándar de Python proporciona herramientas para la generación de permutaciones y combinaciones de manera eficiente. El siguiente ejemplo ilustra su uso.

```python
import itertools

elementos = [1, 2, 3]

# Permutaciones, el orden es relevante
permutaciones = list(itertools.permutations(elementos))

# Combinaciones de dos elementos, el orden no es relevante
combinaciones = list(itertools.combinations(elementos, 2))
```

La función `permutations` genera todas las ordenaciones posibles de los elementos de entrada, mientras que `combinations` genera todos los subconjuntos de un tamaño especificado sin considerar el orden. Ambas funciones constituyen el punto de partida para abordar problemas más complejos que requieren la manipulación explícita de permutaciones y combinaciones.

---

## Organización de esta sección

Los contenidos de esta sección se organizan en las siguientes páginas.

- **Teoría matemática**. Profundiza en la notación de ciclos, la descomposición en transposiciones y la función signo.
- **Implementación y ejercicios en Python**. Presenta la construcción de una clase Permutation, la generación de permutaciones mediante recursión y la resolución de problemas clásicos como la siguiente permutación.
- **Combinatoria avanzada**. Aborda el teorema del binomio, el triángulo de Pascal y los principios fundamentales de conteo.