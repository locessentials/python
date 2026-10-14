---
layout: default
title: Problema D
grandparent: 4. Problemas
parent: ICPC 2017
nav_order: 4
---

# ICPC 2017 - Problema D: poda y monotonía

## Problema
- Entrada: m productores (p = precio, d = día inicial) y n compradores (c = costo, z = día final)
- Elegir un productor y un comprador para maximizar ganacias: (c − p) × (z − d)
- Solo cuentan los pares donde c > p y z > d; si no hay ninguno, la respuesta es 0
- Límites: m, n ≤ 500,000; valores ≤ 10⁹

## Idea principal
Revisar todos los pares productor–comprador tardaría demasiado (hasta 500,000 × 500,000 = 250 mil millones de pares), así que usamos **divide y vencerás**.
- `buscar()`: aquí está el divide y vencerás; busca el mejor comprador para el productor del medio, divide los productores en dos mitades y divide los compradores en el mejor comprador encontrado
- `ganancia()`: calcula la ganancia de cada par que `buscar()` compara

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
- Descarta los pares donde (c − p) y (z − d) son negativos, porque negativo × negativo da positivo y parecería una ganancia; ej.: p=10, d=8, c=4, z=3 → (−6) × (−5) = 30

**Conclusión**
- Al terminar, `mejor_total` es la respuesta. Gracias a la poda y a la monotonía, cada producto se compara solo con una parte de los compradores, y el programa hace unas (m + n) × log m comparaciones en vez de m × n, lo suficiente para el límite de 5 segundos.

[Ver el código completo en GitHub](https://github.com/locessentials/python/blob/main/unidad4/1-icpc-2017/d.py)