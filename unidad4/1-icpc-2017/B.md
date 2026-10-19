---
layout: default
title: Problema B
grandparent: 4. Problemas
parent: ICPC 2017
nav_order: 2
---

# ICPC 2017 - Problema B: juego de mesa Clue

Clue es un juego de mesa en el que hay que deducir quién cometió un asesinato, con qué arma y en qué habitación, llevando un registro cuidadoso de qué cartas tiene cada jugador. Al inicio se colocan tres cartas en un sobre secreto: una de las seis personas sospechosas, una de las seis armas y una de las nueve habitaciones. Las demás cartas se reparten entre los cuatro jugadores. En su turno, cada jugador hace una sugerencia (persona, arma y habitación), empezando por el jugador 1. La persona a su derecha debe mostrarle una carta de la sugerencia si tiene alguna; si no tiene ninguna, pasa, y le toca a la siguiente, hasta que alguien muestra una carta o nadie puede hacerlo. La carta se muestra en secreto, solo a quien hizo la sugerencia. El resto sabe que se mostró una carta, pero no cuál. Si nadie muestra una carta, cada carta sugerida está en el sobre o en la mano de quien hizo la sugerencia.

El problema que resolvemos aquí consiste en lo siguiente: dados el número de sugerencias *n*, nuestras cinco cartas como jugador 1 y el registro de las *n* sugerencias (las tres cartas sugeridas y la respuesta de cada jugador: un guion (-) si pasó, un asterisco (*) si mostró una carta que no vimos, o la letra de la carta si la vimos), hay que deducir qué cartas del sobre se pueden identificar con certeza. La salida indica la persona, el arma y la habitación, con `?` para cualquiera que todavía no se pueda determinar.

Por ejemplo, en el ejemplo 2 mis cartas incluyen A, B, C, D y H. La primera sugerencia es `F G M M`: yo sugiero F, G y M, y el jugador 2 me muestra M, así que sé que él la tiene. La segunda es `F H M - *`: el jugador 2 sugiere F, H y M; el jugador 3 pasa, así que no tiene ninguna de las tres; y el jugador 4 muestra una carta que no vemos. Pero yo tengo H y el jugador 2 tiene M, así que el jugador 4 tuvo que mostrar F.

---

## Panorama del código

Con seis personas, seis armas y nueve habitaciones, hay 6 × 6 × 9 = 324 combinaciones posibles para el sobre. No es un problema grande, pero sí requiere un registro cuidadoso de lo que pasa en el juego. Seguimos la estrategia de propagación de restricciones (*constraint propagation*): guardamos los hechos que conocemos y aplicamos reglas para deducir hechos nuevos, hasta que ya no se puede deducir nada más.

### Preparación: organizar las entradas
- `sugs`: una lista de listas, en donde cada lista contiene el contenido completo de una sugerencia
- `holder`: o sea, quién tiene cada carta, diccionario carta → jugador que la tiene; empieza con las cinco cartas de jugador 1. Ponemos la carta como clave y el jugador como valor porque el programa siempre busca por carta ("¿alguien tiene esta carta?"), y en un diccionario buscar por clave es inmediato
- `lacks`: o sea, las cartas que cada jugador no tiene, un diccionario con una llave para cada jugador, cuyo valor es la lista de cartas que ese jugador dijo no tener
- `unresolved`: una lista de tuplas (jugador, [tres cartas]), una por cada pista `*`: el jugador que mostró una carta que no vimos y las tres cartas sugeridas

### Paso 1: procesar cada sugerencia
Para saber quién responde en cada momento, usamos aritmética modular (*modular arithmetic*), como una flecha que gira sobre un tablero de cuatro jugadores:
- **Quién sugiere:** `suggester = i % 4 + 1`. El residuo de dividir la posición de la sugerencia entre 4 va de 0 a 3; al sumarle 1, da el jugador en turno (1 a 4). Las sugerencias van 1, 2, 3, 4, 1, 2...
- **Quién responde:** la flecha empieza en quien sugiere (`responder = suggester`), y con cada respuesta avanza a la derecha: `responder = responder % 4 + 1`. Después del 4 vuelve al 1. Por ejemplo, si sugiere el jugador 3, responden 4, luego 1, luego 2.

Cada respuesta se guarda según su tipo:
- `-` (no tiene ninguna de las tres cartas): agregar las tres a `lacks`
- `*` (mostró una carta que no vimos): guardar la pista en `unresolved`
- una letra (vimos la carta): registrarla en `holder`

### Paso 2: resolver las pistas `*`
Este paso solo revisa la lista `unresolved`, es decir, las pistas `*`: alguien mostró una carta, pero no vimos cuál. Para resolverlas, usamos los hechos que ya están en `holder` y `lacks`.

1. Empezar con `changed = True`, para que la primera vuelta por la lista se ejecute
2. Al inicio de cada vuelta, poner `changed = False`: suponemos que esta vuelta no descubrirá nada
3. Para cada pista (jugador que mostró la carta y las tres cartas), revisar cada carta y decidir si sigue siendo posible:
   - **Primero, `holder`:** si la carta ya está registrada a nombre de otro jugador, no puede ser la que mostró, porque cada carta está en una sola mano
   - **Segundo, `lacks`:** si ese jugador dijo no tener la carta en otra sugerencia, tampoco puede ser. Por ejemplo, si el jugador 3 respondió `-` a F, H y M, y en otra sugerencia mostró una carta de F, G y N, esa carta no puede ser F
   - Si la carta pasa las dos revisiones, se agrega a la lista `possible`
4. Si en `possible` queda una sola carta, esa fue la que mostró. Si todavía no estaba en `holder`, la registramos y ponemos `changed = True`
5. Si en esta vuelta por la lista `unresolved` se registró alguna carta nueva, se revisan todas las pistas otra vez; si no, el ciclo termina

El ciclo `while changed` es el centro de la propagación de restricciones: cada carta que se registra en `holder` en el punto 4 se convierte en un hecho nuevo para la revisión del punto 3, y puede dejar otra pista con una sola carta posible.

### Paso 3: determinar las cartas del sobre
Para cada categoría, buscamos las cartas que no están en `holder`. Hay dos formas de saber con certeza que una carta está en el sobre:
1. **Nadie más la tiene:** cada carta está en la mano de alguien o en el sobre. Si no es del jugador 1 y los jugadores 2, 3 y 4 dijeron no tenerla, el único lugar que queda es el sobre.
2. **Solo queda una sin ubicar:** el sobre tiene exactamente una carta de cada categoría. Si todas las demás ya están en la mano de alguien, la que queda tiene que ser la del sobre, aunque nadie haya dicho que no la tiene.

Si ninguna de las dos se cumple, la respuesta para esa categoría es `?`.

---

## Análisis del código

- **Construcción del algoritmo:** (1) leer la entrada y registrar en `holder` las cartas del jugador 1; (2) procesar cada sugerencia: calcular quién sugiere y quién da cada respuesta, y guardar cada guion en `lacks`, cada letra en `holder` y cada asterisco en `unresolved`; (3) revisar las pistas sin resolver una y otra vez hasta que una vuelta no descubra nada nuevo; (4) en cada categoría, encontrar la carta del sobre: la única que no está en `holder`, o una que los jugadores 2, 3 y 4 dijeron no tener; (5) imprimir la respuesta, con `?` donde no hay certeza
- **Variables y tipos de datos:** `n`, `suggester` y `responder` son `int`, porque son cantidades y números de jugadorx; las cartas y las respuestas son `str`; `changed` es `bool`, porque solo indica si hubo un descubrimiento
- **Estructuras de datos:** listas para las cartas del jugador 1 y las sugerencias (`sugs` es una lista de listas), porque solo se recorren en orden; un diccionario `holder` (carta → jugador), porque siempre buscamos por carta y en un diccionario esa búsqueda es inmediata; un diccionario de listas `lacks`, para llegar directo a la lista de cada jugador; una lista de tuplas `unresolved`, porque cada pista es un dato fijo que no cambia. `lacks` podría usar conjuntos en vez de listas: buscar una carta en un conjunto es inmediato, mientras que en una lista hay que revisarla completa. No hacen falta grafos, colas ni montículos, porque no hay relaciones entre elementos ni un orden de prioridad
- **Paradigma algorítmico:** propagación de restricciones: se aplican reglas a los hechos conocidos para deducir hechos nuevos, y se repite hasta que no cambia nada. Sirve aquí porque cada regla solo agrega hechos seguros, así que la respuesta nunca es una suposición, y un hecho nuevo puede resolver una pista que antes no se podía resolver
- **Estilo de programación:** procedural e imperativo: ciclos que procesan los datos en orden, sin funciones propias. Conviene porque el programa es corto y sigue los pasos del juego en orden; pero la lógica del paso 4 se repite para cada categoría, y una función evitaría esa repetición
- **Iterativo o recursivo:** iterativo: ciclos `for` para recorrer los datos y un ciclo `while` para repetir la revisión hasta que no haya cambios. No hace falta recursión porque no hay árboles ni grafos que recorrer, y "repetir hasta que no cambie nada" se escribe directo con un `while`
- **Complejidad:** temporal O(n²) (cuadrática), con n el número de sugerencias. En cada vuelta del ciclo `while`, recorremos la lista `unresolved`, que puede tener hasta n pistas, y para cada pista buscamos cartas en la lista `lacks` del jugador (`card in lacks[player]`), que puede tener hasta 3n cartas: n pistas por n cartas da n². El ciclo `while` da como máximo una vuelta por cada carta descubierta, y solo hay 21 cartas, así que el número de vueltas no cambia la complejidad. Espacial O(n), por las sugerencias, las listas de `lacks` y las pistas. Con conjuntos en `lacks`, cada búsqueda sería inmediata y el tiempo bajaría a O(n) (lineal)

[Ver el código completo en GitHub](https://github.com/locessentials/python/blob/main/unidad4/1-icpc-2017/b.py)