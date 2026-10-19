# Problema D

En este problema hay productores que venden un producto y compradores que lo compran, y tenemos que encontrar el productor y el comprador que juntos dan la mayor ganancia. Primero recibimos m productores, cada uno con un precio (p) y un día inicial (d), y n compradores, cada uno con el costo que paga (c) y un día final (z). La ganancia es lo que paga el comprador menos lo que cobra el productor, multiplicado por los días entre el día inicial del productor y el día final del comprador ((c - p) * (z - d)).

El reto es que m y n pueden llegar a quinientos mil, así que revisar todos los pares tardaría demasiado. Entonces, resolvemos el problema con dos técnicas: poda, y divide y vencerás usando monotonía.

**Idea principal**

Primero, la poda: un productor no sirve si otro empieza antes y cobra menos, y un comprador no sirve si otro termina después y paga más. Luego, la monotonía: después de la poda, los productores van del más temprano y caro al más tardío y barato, y los compradores van del que termina pronto y paga mucho al que termina tarde y paga poco. Así, cuando el productor avanza, su mejor comprador también avanza y nunca retrocede.

**La poda**

Ahora veamos el código. Primero, hacemos la poda de productores. Definimos una función, ordenar productores (ord_prod), que regresa una tupla con el día y el precio. Así ordenamos por día inicial de menor a mayor, y si dos empiezan el mismo día, primero va el más barato. Después creamos la lista de productores competitivos (prod_c) y el precio mínimo (min_precio), que empieza en infinito (float('inf')) para que el primer productor siempre se quede. Un ciclo for revisa cada productor en orden: si su precio es menor que el precio mínimo, lo agregamos y actualizamos el precio mínimo. Así, la lista guarda varios productores: cada uno empieza más tarde y cobra menos que el anterior.

Para los compradores hacemos lo mismo, pero al revés. La función ordenar compradores (ord_comp) los ordena por día final de mayor a menor. Luego un ciclo for revisa cada comprador en ese orden y lo agrega a la lista de compradores competitivos (comp_c) solo si paga más que todos los que terminan después de él. Para eso guardamos el costo más alto que hemos visto (max_costo). Por último volteamos la lista (comp_c.reverse()) para que quede de menor a mayor día final. Así, cada comprador termina más tarde y paga menos que el anterior.

**El mejor par**

Ahora que tenemos las dos listas, vamos a buscar el mejor par. Primero creamos una variable para la mejor ganancia total (mejor_total), que empieza en cero. Aquí guardamos la ganancia más alta que encontremos.

Para encontrarla, definimos la función buscar (buscar). La idea es esta: en vez de comparar cada productor con todos los compradores, tomamos el productor del medio y encontramos su mejor comprador. Ese comprador nos dice dónde hay que buscar los demás productores.

La función recibe el inicio y el fin del tramo de productores (p_ini, p_fin), y el inicio y el fin del tramo de compradores (c_ini, c_fin). Primero tomamos el productor del medio del tramo (mitad). Luego un ciclo for revisa cada comprador del tramo y calcula la ganancia de ese comprador con el productor del medio, usando la función ganancia (ganancia).

La función ganancia calcula la ganancia del par. Pero si el comprador paga menos de lo que cobra el productor y deja de comprar antes de que el productor empiece, regresa menos infinito (float('-inf')). Esto es porque negativo por negativo daría un número positivo, y parecería una ganancia aunque no lo es.

Mientras el ciclo revisa los compradores, guardamos la ganancia más alta (mejor) y la posición del comprador que la da, que es el mejor comprador del productor del medio (mejor_c). Si esa ganancia es mayor que la mejor ganancia total, la guardamos ahí. 

Ahora usamos ese mejor comprador para dividir. Los productores antes del medio tienen su mejor comprador antes de ese comprador o en él, y los productores después del medio lo tienen en él o después. Por eso buscar se llama a sí misma dos veces: una vez para la primera mitad de los productores, solo con los compradores hasta ese mejor comprador, y otra vez para la segunda mitad, solo con los compradores desde ahí. La función sigue dividiendo hasta que el tramo de productores queda vacío, es decir, cuando la posición de inicio es mayor que la posición final, y ahí termina.

**Resultado**

Para empezar todo, el programa llama a buscar una sola vez, con todos los productores y compradores competitivos, y esa llamada hace todas las divisiones. Cuando termina, la mejor ganancia total es la respuesta; si no hubo ningún par válido, sigue en cero. Por último, imprimimos la mejor ganancia total.

**Complejidad**

Hay dos variables, m y n. Ordenar cuesta O de m log m más n log n (O(m log m + n log n)), que es lineal-logarítmica. La poda cuesta O de m más n, que es lineal. Buscar cuesta O de m más n, por log m (O((m + n) log m)), también lineal-logarítmica, porque la recursión tiene unos log m niveles y en cada nivel cada comprador se revisa pocas veces. La complejidad espacial es O de m más n, lineal, por las listas.

**Posibles respuestas para preguntas**

La mejor ganancia total es una variable global (global), porque buscar se llama muchas veces y todas guardan el resultado en el mismo lugar.