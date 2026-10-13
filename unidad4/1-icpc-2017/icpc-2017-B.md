---
layout: default
title: Problema B
grandparent: 4. Problemas
parent: ICPC 2017
nav_order: 2
---

# ICPC 2017 - Problema B: Juego de mesa Clue

Clue es un juego de mesa en el que hay que deducir quién cometió un asesinato, con qué arma y en qué habitación, llevando un registro cuidadoso de qué cartas tiene cada jugadorx. Al inicio se colocan tres cartas en un sobre secreto: una de las seis personas sospechosas, una de las seis armas y una de las nueve habitaciones. Las demás cartas se reparten entre lxs cuatro jugadorxs. En su turno, cada jugador hace una sugerencia (persona, arma y habitación), empezando por el jugador 1. La persona a su derecha debe mostrarle una carta de la sugerencia si tiene alguna; si no tiene ninguna, pasa, y le toca a la siguiente, hasta que alguien muestra una carta o nadie puede hacerlo. La carta se muestra en secreto, solo a quien hizo la sugerencia. El resto sabe que se mostró una carta, pero no cuál. Si nadie muestra evidencia, las cartas sugeridas deben estar en el sobre.

El problema que resolvemos aquí consiste en lo siguiente: dados el número de sugerencias *n*, nuestras cinco cartas como jugador 1 y el registro de las *n* sugerencias (las tres cartas sugeridas, si cada jugadorx pasó o mostró una carta, y si pudimos ver cuál), hay que deducir qué cartas del sobre se pueden identificar con certeza. La salida indica la persona, el arma y la habitación, con `?` para cualquiera que todavía no se pueda determinar.

## Panorama de la solución

Con seis cartas de personas, seis de armas y nueve de habitaciones el universo de posibles combinaciones de cartas en el sobre es 324. Entonces no es un problema de gran tamaño pero si requiere un registro cuidados de la información disponible del gameplay. Aquí seguimos la estrategía de propagación de restricciones: recordamos hechos y aplicamos reglas de...





[Ver el código completo en GitHub](https://github.com/locessentials/python/blob/main/unidad4/1-icpc-2017/b.py)

## What held me up

- Not knowing how to add an key:value pair to a list
- Coming into the realization of `responder = suggester` being used to start a pointer on a spin board that tracks the players taking turns within a single round of suggesting and presenting evidence
- Thinking about how this is related to python True/False being used as a switch
- while statements


