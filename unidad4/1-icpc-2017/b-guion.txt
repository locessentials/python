## Problema B

En el juego Clue, hay tres cartas en un sobre secreto: una persona, un arma y una habitación, y el objetivo es deducir cuáles son. Las demás cartas se reparten entre cuatro jugadores, y sabemos las cartas del jugador 1. En su turno, cada jugador hace una sugerencia de tres cartas, empezando por el jugador 1, y los jugadores a su derecha responden en orden hasta que alguien muestra una carta. En la entrada, cada respuesta es un guion (-) si el jugador pasó porque no tiene ninguna de las tres cartas, un asterisco (\*) si mostró una carta en secreto y no vimos cuál, o la letra de la carta si la vimos. Si nadie muestra una carta, cada carta sugerida está en el sobre, o en la mano de quien hizo la sugerencia. Con las cinco cartas del jugador 1 y el registro de las *n* sugerencias, hay que deducir qué cartas del sobre se pueden identificar con certeza. La salida indica la persona, el arma y la habitación, con `?` para cualquiera que no se pueda determinar.

## Panorama del código

Para resolver este problema, seguimos una estrategia de propagación de restricciones (*constraint propagation*), en la que guardamos los hechos que conocemos y aplicamos reglas para deducir hechos nuevos, hasta que ya no se puede deducir nada más.

### Preparación: organizar las entradas
- `sugs`: una lista de listas, en donde cada lista contiene el contenido completo de una sugerencia
- `holder`: o sea, quién tiene cada carta, diccionario carta → jugador que la tiene; empieza con las cinco cartas de jugador 1.
- `lacks`: un diccionario con una llave para cada jugador, cuyo valor es la lista de cartas que ese jugador dijo no tener
- `unresolved`: una lista de tuplas (jugador, [tres cartas]), una por cada pista `*`: el jugador que mostró una carta que no vimos y las tres cartas sugeridas

### Procesamiento de las sugerencias
Con los datos preparados, procesamos cada uno de los turnos del juego. Para esto, con un ciclo `for`, recorremos la lista de sugerencias `sugs` y, para cada una, tomamos su posición (`i`) y su contenido (`sug`).

Primero, el código encuentra quién hizo la sugerencia. Como los jugadores se turnan del 1 al 4, podemos tomar `i` módulo cuatro, más uno, y esto nos da el jugador en turno. Después separa el renglón en dos partes: las tres primeras posiciones son las cartas sugeridas, y lo que sigue son las respuestas. Luego recorre las respuestas y, con cada una, avanza un jugador a la derecha, usando otra vez el módulo más uno.

Si el jugador pasa, agregamos las tres cartas a su lista en el diccionario `lacks` para las cartas que cada jugador no tiene. Si muestra una carta, pero no sabemos cuál, guardamos el jugador y las tres cartas en la lista `unresolved` para resolverla después. Y si responde con una letra, vimos la carta, así que la registramos en `holder` con el jugador que la tiene. 

Seguimos así hasta procesar todas las sugerencias.

### Reintentar las pistas '*' sin resolver
Después de procesar las sugerencias, nos quedan algunas pistas sin resolver que tal vez podemos deducir con toda la información que ahora tenemos. 

Entonces, volvemos a procesar estas pistas dentro de un ciclo `while`, que se repite mientras haya cambios. En cada vuelta, con un ciclo `for`, recorremos el jugador y las tres cartas de cada pista en la lista de pistas no resueltas (`unresolved`). 

Dentro de otro ciclo `for` anidado, revisamos cada una de las tres cartas: si otro jugador ya tiene la carta o si la carta está en la lista de cartas que este jugador dijo no tener (`lacks`), la ignoramos. Si no está en ninguno de estos dos lugares, la agregamos a una nueva lista de posibilidades. Después, si solo queda una carta en la lista de posibilidades, esa fue la carta que mostró el jugador, y la agregamos al diccionario de quién tiene cada carta (`holder`), pero solo si todavía no estaba ahí. Cuando sí agregamos una carta nueva, marcamos que hubo un cambio, porque esto cambia lo que sabemos, y repetimos todo el recorrido hasta que una vuelta ya no descubra nada nuevo.

### Determinar la respuesta
Después de deducir todo lo que podemos de las pistas sin resolver, podemos determinar la respuesta.

Tenemos tres bloques de código que funcionan exactamente igual para eso, pero con variables con nombres para su categoría (persona, arma, habitación). En cada bloque empezamos con una lista vacía de las cartas que quedan. Revisamos todas las cartas posibles de esta categoría, y si la carta no está en el diccionario de quién tiene cada carta (`holder`), la agregamos a la lista de cartas que quedan. Después, para esta categoría, la respuesta es ? a menos que pase una de dos cosas: que una carta de la lista esté en la lista de cartas que dijeron no tener los jugadores 2, 3 y 4 (`lacks`), porque entonces nadie la tiene y tiene que estar en el sobre; o que solo quede una carta en la lista de cartas que quedan.

Como dije, hacemos esto para cada categoría, y después imprimimos nuestra respuesta: la persona, el arma y la habitación donde ocurrió el crimen.