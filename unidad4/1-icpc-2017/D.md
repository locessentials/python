---
layout: default
title: Problema D
grandparent: 4. Problemas
parent: ICPC 2017
nav_order: 4
---

# ICPC 2017 - Problema D: poda y monotonía

- Entrada: m productores (p = precio, d = día inicial) y n compradores (c = costo, z = día final)
- Elegir un productor y un comprador para maximizar ganancias: (c − p) × (z − d)
- Solo cuentan los pares donde c > p y z > d; si no hay ninguno, la respuesta es 0
- Límites: m, n ≤ 500,000; valores ≤ 10⁹

---

## Idea principal
Revisar todos los pares productor–comprador tardaría demasiado (hasta 500,000 × 500,000 = 250 mil millones de pares), así que usamos **divide y vencerás**.
- `buscar()`: aquí está el divide y vencerás; busca el mejor comprador para el productor del medio, divide los productores en dos mitades y divide los compradores en el mejor comprador encontrado
- `ganancia()`: calcula la ganancia de cada par que `buscar()` compara

---

## Implementación

### 1. Poda (*pruning*)
- **Productores:** ordenar por día inicial y precio más bajo, menor a mayor; quitar los productores que no sean competitivos, es decir, los que tienen otro productor que empieza antes y cobra menos
- **Compradores:** ordenar por día final y precio más alto, mayor a menor; quitar los compradores que no sean competitivos, es decir, los que tienen otro comprador que termina después y paga más

### 2. Monotonía (*monotonicity*): optimización con divide y vencerás

**Lógica**
- Productores: los primeros son caros, los posteriores son baratos
- Compradores: los primeros pagan mucho pero terminan pronto, los posteriores pagan menos pero duran más
- Un productor temprano y caro necesita un comprador que pague mucho, y solo los primeros compradores lo hacen. Un productor tardío necesita un comprador que siga comprando cuando empieza, y solo los compradores posteriores lo hacen.
- Así, el mejor comprador avanza cuando el productor avanza, y nunca retrocede

**`buscar()`, paso a paso**
1. Tomar el productor del medio (`mitad`)
2. Comparar ese productor con cada comprador de su tramo, usando `ganancia()`, y guardar el mejor (`mejor_c`)
3. Si esa ganancia es la mejor hasta ahora, guardarla en `mejor_total`
4. Dividir:
   - productores antes del medio → compradores hasta `mejor_c`
   - productores después del medio → compradores desde `mejor_c`
5. Repetir con cada mitad hasta que no queden productores

**`ganancia()`**
- La llama `buscar()` en el paso 2 para cada par
- Calcula (c − p) × (z − d)
- Quita los pares donde (c − p) y (z − d) son negativos, porque negativo × negativo da positivo y parecería una ganancia; ej.: p=10, d=8, c=4, z=3 → (−6) × (−5) = 30

**Conclusión**
- Al terminar, `mejor_total` es la respuesta. Gracias a la poda y a la monotonía, cada productor se compara solo con una parte de los compradores, y el programa hace unas (m + n) × log m comparaciones en vez de m × n, lo suficiente para el límite de 5 segundos.

[Ver el código completo en GitHub](https://github.com/locessentials/python/blob/main/unidad4/1-icpc-2017/d.py)

---

## Análisis del código

- **Construcción del algoritmo:** (1) leer `m`, `n`, los productores en `prod` y los compradores en `comp`; (2) ordenar `prod` por día inicial y quedarse en `prod_c` solo con los productores más baratos que todos los anteriores; (3) ordenar `comp` por día final de mayor a menor, quedarse en `comp_c` solo con los compradores que pagan más que todos los que terminan después, y voltear la lista; (4) llamar a `buscar()` con todos los productores y compradores competitivos; (5) imprimir `mejor_total`
- **Variables y tipos de datos:** `m`, `n`, los precios y días (`p`, `d`, `c`, `z`) y las posiciones (`p_ini`, `p_fin`, `c_ini`, `c_fin`, `mitad`, `pos_c`, `mejor_c`) son `int`; `float('inf')` y `float('-inf')` solo se usan como valores iniciales (infinito), para que cualquier precio o ganancia real sea mejor; la ganancia puede llegar a 10¹⁸ (10⁹ × 10⁹), y los `int` de Python no tienen límite, así que no hay desbordamiento (*overflow*)
- **Estructuras de datos:** `prod` y `comp` son listas de listas, para leer la entrada; `prod_c` y `comp_c` son listas de tuplas (precio, día), porque los pares no cambian y la lista permite llegar a cada uno por su posición, que es lo que necesita `buscar()` para dividir; `ord_prod()` y `ord_comp()` regresan tuplas, porque Python compara las tuplas por el primer valor y, si empatan, por el segundo; no hacen falta diccionarios, conjuntos, colas, montículos ni grafos, porque solo se recorren listas ordenadas por posición
- **Paradigma algorítmico:** poda (*pruning*) para quitar los productores y compradores que nunca pueden ser la mejor opción, y luego **divide y vencerás** con monotonía (*divide and conquer optimization*): como el mejor comprador avanza cuando el productor avanza, se busca el mejor comprador del productor del medio y ese comprador divide a los compradores en dos partes, una para cada mitad de productores
- **Estilo de programación:** procedural, con una función para cada tarea (`ord_prod()`, `ord_comp()`, `ganancia()`, `buscar()`); `mejor_total` y `mejor_par` son variables globales (`global`), para que todas las llamadas de `buscar()` guarden el mejor resultado en el mismo lugar
- **Iterativo o recursivo:** iterativo en la lectura y la poda; recursivo en `buscar()`, porque cada llamada divide el problema en dos mitades del mismo tipo; como los productores se dividen a la mitad cada vez, la recursión tiene unos log m niveles (unos 20 con 500,000 productores), así que no pasa el límite de recursión de Python
- **Complejidad:** temporal O(m log m + n log n) para ordenar, O(m + n) para la poda, y O((m + n) × log m) para `buscar()`, porque en cada uno de los log m niveles se revisa cada comprador como mucho unas pocas veces; espacial O(m + n), por las listas de productores y compradores; la operación que determina la complejidad es el ordenamiento y las llamadas a `ganancia()` dentro de `buscar()`