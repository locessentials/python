---
layout: default
title: Problema E
grandparent: 4. Problemas
parent: ICPC 2017
nav_order: 5
---

# ICPC 2017 - Problema E: búsqueda binaria

Dado un viaje de **n** segmentos, cada uno con una distancia **d** y una lectura **s** de un velocímetro sin calibrar, y el tiempo total **t** que tomó el viaje completo, calcular la constante **c** que, sumada a cada lectura, da la velocidad real: **s + c**.

La constante debe cumplir dos condiciones:

1. La suma de los tiempos de todos los segmentos es igual al tiempo total:

```
  Σ d / (s + c) = t
```

2. La velocidad real de cada segmento es positiva: **s + c > 0**.

Las lecturas s pueden ser negativas, y c también puede serlo, pero no al mismo tiempo: la velocidad real, s + c, siempre tiene que ser positiva.

**Entrada**

- Primera línea: **n** (1 ≤ n ≤ 1000) y **t** (1 ≤ t ≤ 10⁶, es decir, 1000000).
- Siguientes **n** líneas: **d** (1 ≤ d ≤ 1000) y **s** (|s| ≤ 1000) de cada segmento.

**Salida**

- El valor de **c**, con un error absoluto o relativo menor que 10⁻⁶ (es decir, 0.000001).

---

## Idea principal
No hay una fórmula directa para calcular c (como c aparece dentro de cada denominador) de la ecuación directamente, pero el tiempo total siempre baja cuando c sube, así que usamos **búsqueda binaria sobre la respuesta**: probamos el punto medio del rango posible de c, calculamos el tiempo que daría y quitamos (*we discard*) la mitad donde c no puede estar. Repetimos hasta que el rango es mucho más pequeño que 10⁻⁶.
- `T(c)`: función de evaluación; calcula el tiempo total del viaje si la constante fuera c
- ciclo `for`: aquí está la búsqueda binaria; compara `T(mid)` con `t` y mueve `lo` o `hi` al punto medio

---

## Panorama de la resolución

### Establecer los límites de la búsqueda

#### Límite inferior de c (lo)

Para fijar el límite inferior, hay que tener en cuenta que la velocidad real tiene que ser mayor que cero, así que la regla es: s + c > 0

El límite inferior usa la lectura más baja de las entradas reales, así que buscamos la s más baja entre todos los segmentos y encontramos la c que haría que su velocidad real fuera exactamente 0:

low_s + c = 0, así que c = −low_s

Por ejemplo, en el ejemplo 1 la lectura más baja es −1, así que −1 + c = 0 y c = 1. La respuesta tiene que ser mayor que eso, así que lo = −low_s.

#### Límite superior de c (hi)

Calculamos el límite superior de c a partir de los rangos de las entradas n, d, t y s permitidos por el problema.

| Límite | Según el problema | Peor caso |
|---|---|---|
| n, número de segmentos | 1 ≤ n ≤ 1000 | 1000 segmentos |
| d, distancia por segmento | 1 ≤ d ≤ 1000 | 1000 millas cada uno |
| t, tiempo total | 1 ≤ t ≤ 10⁶ | 1 hora |
| s, lectura sin calibrar | \|s\| ≤ 1000 (es decir, entre −1000 y 1000) | −1000 |

Si juntamos los peores casos: 1000 segmentos × 1000 millas = 1,000,000 de millas, todo en 1 hora. Para lograrlo, las velocidades reales tienen que estar alrededor de 1,000,000 mph, ya que distancia 1,000,000 millas / 1 hora = velocidad 1,000,000 mph.

Para calcular el límite superior de c, usamos la lectura s = −1000, porque es la más baja y, por lo tanto, la que necesita la c más grande:

−1000 + c = 1,000,000, así que c = 1,001,000

Esa es la c más grande que la respuesta podría necesitar, así que cualquier hi mayor es seguro. Por eso iniciamos la búsqueda con hi = 1,001,001.

### Ejecutar el algoritmo de búsqueda binaria

#### Función T(c)

Definimos una función que calcula el tiempo total del viaje si la constante fuera c: para cada segmento, divide la distancia d entre la velocidad real s + c, y suma los tiempos de todos los segmentos.

#### Ciclo for

En el ciclo `for`, calculamos el punto medio entre `lo` y `hi`, lo evaluamos con `T`, y hay dos resultados posibles:

1. Si el tiempo que da es mayor que el tiempo total real del viaje, el viaje tarda demasiado y las velocidades son demasiado lentas. Como c tiene que ser más grande, quitamos todos los valores de c menores que el punto medio, así que `lo` pasa a ser el punto medio.
2. Si el tiempo que da es menor o igual que el tiempo total real, el viaje es demasiado corto y las velocidades son demasiado rápidas. Como c tiene que ser más pequeña, quitamos todos los valores de c mayores que el punto medio, así que `hi` pasa a ser el punto medio.

Repetimos 100 veces, hasta que el rango es mucho más pequeño que 10⁻⁶. Como cada iteración reduce el rango a la mitad, con unas 40 ya se llega a 10⁻⁶; usamos 100, un valor común en búsquedas binarias con decimales porque alcanza de sobra.

---

## Solución

Después de repetir esta operación 100 veces, `lo` y `hi` son prácticamente el mismo número dentro del rango. Ese valor es nuestra c: la constante que, con las entradas n, t, d y s, da el tiempo total del viaje.

[Ver el código completo en GitHub](https://github.com/locessentials/python/blob/main/unidad4/1-icpc-2017/e.py)

---

## Análisis del código

- **Construcción del algoritmo:** (1) leer `n`, `t` y los segmentos en `segmentos`; (2) encontrar `low_s`, la lectura más baja, y fijar `lo = -low_s` y `hi = 1001001`; (3) repetir 100 veces: calcular `mid`, evaluar `T(mid)` y mover `lo` o `hi` a `mid`; (4) imprimir `hi` con 9 decimales
- **Variables y tipos de datos:** `n`, `t`, `d` y `s` son `int`, porque la entrada son números enteros; `c`, `mid`, `lo`, `hi` y `running` son `float`, porque la respuesta es un número decimal y cada tiempo d / (s + c) también lo es; la precisión de `float` (unos 15 dígitos) alcanza de sobra para el error de 10⁻⁶ que pide el problema; `float("inf")` solo se usa como valor inicial de `low_s`, para que cualquier lectura real sea más baja
- **Estructuras de datos:** una lista de listas `segmentos`, porque `T(c)` necesita recorrer todos los segmentos en cada repetición; no hacen falta diccionarios, conjuntos, colas, montículos ni grafos, porque solo se recorre la lista completa
- **Paradigma algorítmico:** búsqueda binaria sobre la respuesta (*binary search on the answer*): no hay fórmula para encontrar c, pero `T(c)` siempre baja cuando c sube (cada s + c sube, así que cada d / (s + c) baja), así que comparar `T(mid)` con `t` dice en qué mitad está c, y se quita la otra mitad
- **Estilo de programación:** procedural, con una función `T(c)` para calcular el tiempo y un ciclo para la búsqueda
- **Iterativo o recursivo:** iterativo: un ciclo `for` de 100 repeticiones; no hace falta recursión, porque cada repetición solo cambia `lo` o `hi`
- **Complejidad:** temporal O(100 × n) (lineal): en cada una de las 100 repeticiones, `T(c)` recorre los n segmentos (como mucho 100 × 1000 = 100,000 divisiones); espacial O(n) (lineal), por la lista `segmentos`; la operación que determina la complejidad es la división d / (s + c) dentro de `T(c)`
