## Problema I

Es un problema de "traducción", aunque aquí usamos "traducir" en un sentido muy libre: solo es cambiar una letra por otra.

**El problema**

- Recibimos cierto número de traducciones de letras y las guardamos en un diccionario `t`. La clave es una letra, y el valor es la lista de letras a las que se traduce directamente.
- Recibimos cierto número de pares de palabras y los guardamos en una lista de tuplas `p`. Cada tupla tiene la palabra original y la palabra descifrada.
- El problema nos pide decidir, para cada par, si la palabra original se puede convertir en la descifrada usando esas traducciones.

Lo importante es que las traducciones se pueden encadenar. Si a se traduce a b, y b se traduce a c, entonces a también puede convertirse en c. Por eso este es un problema de grafos: las letras son nodos, las traducciones son aristas dirigidas, y lo que buscamos es la clausura transitiva, es decir, todas las letras a las que se puede llegar desde una letra.

**Cómo lo resolvemos**

Para cada par, empezamos con una revisión fácil: si las palabras no tienen la misma longitud, ya sabemos que la respuesta es "no", porque aquí solo cambiamos letras, no agregamos ni quitamos posiciones.

Si tienen la misma longitud, revisamos cada posición. Pasamos la letra de la palabra original a la función `find_letters()`, que encuentra todas las letras en las que se puede convertir.

La función usa dos listas, y la letra empieza en las dos:
- `found`, para las letras encontradas. La letra empieza aquí porque siempre puede quedarse igual.
- `to_check`, para las letras que todavía hay que revisar.

Mientras queden letras en `to_check`, sacamos una con `pop()`. `pop()` saca la última letra que entró, así que `to_check` funciona como una pila (*stack*), y eso hace que sea una búsqueda en profundidad, una DFS. Buscamos esa letra en el diccionario, y cada letra a la que se traduce, si todavía no está en `found`, la agregamos a `found` y a `to_check`. Así revisamos también sus traducciones, y así seguimos la cadena. Revisar que no esté ya en `found` es importante: si hay un ciclo, por ejemplo a → b y b → a, sin esa revisión el ciclo nunca terminaría. Cuando ya no hay más letras en `to_check`, la función devuelve `found`.

De vuelta en el ciclo principal, revisamos si la letra de la palabra descifrada en esta misma posición está en `found`. Si no está, marcamos `match` como falso. Hacemos lo mismo con cada posición, y al final, si todas las posiciones pasaron, imprimimos "yes", y si alguna falló, imprimimos "no".