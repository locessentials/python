---
layout: default
title: Problema B
grandparent: 4. Problemas
parent: ICPC 2017
nav_order: 2
---

# ICPC 2017 - Problema B: juego de mesa Clue

Clue es un juego de mesa en el que hay que deducir quién cometió un asesinato, con qué arma y en qué habitación, llevando un registro cuidadoso de qué cartas tiene cada jugadorx. Al inicio se colocan tres cartas en un sobre secreto: una de las seis personas sospechosas, una de las seis armas y una de las nueve habitaciones. Las demás cartas se reparten entre lxs cuatro jugadorxs. En su turno, cada jugador hace una sugerencia (persona, arma y habitación), empezando por el jugador 1. La persona a su derecha debe mostrarle una carta de la sugerencia si tiene alguna; si no tiene ninguna, pasa, y le toca a la siguiente, hasta que alguien muestra una carta o nadie puede hacerlo. La carta se muestra en secreto, solo a quien hizo la sugerencia. El resto sabe que se mostró una carta, pero no cuál. Si nadie muestra evidencia, las cartas sugeridas deben estar en el sobre.

El problema que resolvemos aquí consiste en lo siguiente: dados el número de sugerencias *n*, nuestras cinco cartas como jugador 1 y el registro de las *n* sugerencias (las tres cartas sugeridas, si cada jugadorx pasó o mostró una carta, y si pudimos ver cuál), hay que deducir qué cartas del sobre se pueden identificar con certeza. La salida indica la persona, el arma y la habitación, con `?` para cualquiera que todavía no se pueda determinar.

## Panorama de la solución

Con seis personas, seis armas y nueve habitaciones, hay 6 × 6 × 9 = 324 combinaciones posibles para el sobre. No es un problema grande, pero sí requiere un registro cuidadoso de lo que pasa en el juego. Seguimos la estrategia de propagación de restricciones (*constraint propagation*): guardamos los hechos que conocemos y aplicamos reglas para deducir hechos nuevos, hasta que ya no se puede deducir nada más.

### Preparación: organizar las entradas
- `holder`: diccionario carta → jugador que la tiene; empieza con las cinco cartas de jugador 1. Ponemos la carta como clave y el jugador como valor porque el programa siempre busca por carta ("¿alguien tiene esta carta?"), y en un diccionario buscar por clave es inmediato
- `lacks`: para cada jugador, las cartas que dijo no tener
- `unresolved`: las pistas `*`, guardadas como (jugadorx, tres cartas), para resolverlas después

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

## Análisis
- **Variables y tipos de datos:** `n`, `suggester` y `responder` son `int`, porque son cantidades y números de jugadorx; las cartas y las respuestas son `str`; `changed` es `bool`, porque solo indica si hubo un descubrimiento
- **Estructuras de datos:** listas para las cartas de jugador 1 y las sugerencias (`sugs` es una lista de listas); un diccionario `holder` para encontrar rápido quién tiene cada carta; un diccionario de listas `lacks` con las cartas que niega cada jugador; una lista de tuplas `unresolved` con las pistas pendientes
- **Paradigma algorítmico:** propagación de restricciones: se aplican reglas a los hechos conocidos para deducir hechos nuevos, y se repite hasta que no cambia nada
- **Estilo de programación:** procedural e iterativo: ciclos que procesan los datos en orden, sin funciones propias. La lógica del paso 3 se repite para cada categoría; una función evitaría esa repetición

[Ver el código completo en GitHub](https://github.com/locessentials/python/blob/main/unidad4/1-icpc-2017/b.py)