# Problema C

El problema C es un problema de emparejamiento bipartito. Tenemos una cuadrícula de renglones y columnas, y en cada posición hay una pila de cajas, que puede tener altura cero. Sabemos a través de la entrada del problema los valores de todas las posiciones de la cuadrícula. Desde el frente se ve la altura máxima de cada columna, y desde el lado, la altura máxima de cada renglón. Desde arriba se ve qué posiciones tienen cajas y qué posiciones no. Dadas las dimensiones de la cuadrícula y la altura de cada posición, hay que encontrar el mayor número de cajas que se pueden quitar sin cambiar ninguna de las tres vistas.

La idea clave es que hay que dejar una caja en cada posición con cajas, y una pila máxima en cada renglón y en cada columna. Pero si un renglón y una columna tienen el mismo máximo, y la posición donde se cruzan tiene cajas, una sola pila sirve para los dos. Así ahorramos cajas.

Para encontrar el mayor número de estas posiciones compartidas, usamos un grafo bipartito. Los renglones son un conjunto de vértices y las columnas son el otro. Buscamos el mayor número de parejas renglón–columna.

**Preparación**

Primero guardamos la cuadrícula como una lista de listas donde cada lista es un renglón (rows). Luego calculamos el total de cajas (total), el máximo de cada renglón (max_rows) y el máximo de cada columna (max_columns). También contamos las posiciones distintas de cero (not_zero), porque cada una se queda con mínimo una caja.

**Emparejamiento**

Para el emparejamiento usamos un algoritmo de caminos de aumento.

Primero creamos una hoja de registro (match_col), con un lugar para cada columna. Cada lugar guarda el número del renglón que usa esa columna. Empieza con menos 1 en todos los lugares, que quiere decir que todas las columnas están libres.

Luego, un ciclo for revisa cada número de renglón. Para cada renglón, busca su máximo, y si el máximo es mayor que cero, creamos una lista de columnas revisadas (seen), con un falso para cada columna, porque todavía no revisamos ninguna. Después llamamos a la función que busca pareja para ese renglón (try_match).

La función tiene un ciclo que revisa cada columna y hace dos preguntas. Primero, ¿el renglón y la columna tienen el mismo máximo? Segundo, ¿la posición donde se cruzan tiene cajas? Si las dos respuestas son sí, pueden compartir una pila (can_share).

Si pueden compartir y todavía no revisamos esta columna, primero la marcamos como revisada. Luego hay dos casos. Si la columna está libre, el renglón la toma: escribimos su número en la hoja de registro, y la función regresa verdadero. Si la columna está ocupada, entra la recursión.

**La recursión**

La función se llama a sí misma con el renglón que ya usa esa columna. Así le pregunta: ¿te puedes cambiar a otra columna? Ese renglón busca otra columna con las mismas reglas. Si encuentra una, se cambia, y el renglón nuevo toma la columna que quedó libre. Así, un renglón que llegó primero se puede mover para dejarle lugar a otro.

La lista de columnas revisadas es importante aquí, ya que sin ella, el renglón 0 podría pedir la columna 0 otra vez, y los renglones se pedirían cambiar hasta el infinito.

Cada vez que un renglón encuentra pareja, sumamos su máximo menos 1 a las cajas contadas dos veces (counted_twice). Restamos 1 porque ya contamos una caja en cada posición distinta de cero (not_zero). Las demás cajas de la pila, el máximo menos 1, se cuentan dos veces: una vez para el renglón y otra para la columna. Por eso las guardamos en las cajas contadas dos veces (counted_twice), para restarlas al final.

**Cálculo final**

Las cajas que quedan (left) son las posiciones distintas de cero, más las cajas de los máximos de renglones y columnas, menos las cajas contadas dos veces. La respuesta es el total menos las cajas que quedan.

**Extensión**

Como extensión, agregué un mapa que muestra cuántas cajas quedan en cada posición.

**Complejidad**

La complejidad temporal es O de m por n al cuadrado. Si la cuadrícula es cuadrada, es cúbica. La complejidad espacial es O de m por n, que es lineal respecto al tamaño de la cuadrícula.