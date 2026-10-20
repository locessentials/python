# Problema F

El problema F es un problema de programación dinámica.

Tenemos una imagen, y solo usamos el canal rojo. Cada píxel tiene una intensidad de rojo, que es un entero entre 0 y 255. La entrada nos da d intensidades distintas, en orden creciente. Para cada intensidad r, nos da p, el número de píxeles que tienen esa intensidad. También nos da k, el número de valores que podemos usar en la imagen posterizada.

Posterizar quiere decir usar menos valores de rojo. Solo podemos usar k valores. Cada píxel cambia su intensidad al valor permitido más cercano. Ese cambio produce un error: la diferencia entre la intensidad original, r, y el nuevo valor, v, elevada al cuadrado. Elevamos al cuadrado por dos razones: quita el signo, para que los errores negativos no se resten, y castiga más los errores grandes. Queremos que la imagen nueva se parezca lo más posible a la original. Por eso hay que encontrar la suma mínima de todos los errores.

El reto es que tenemos que decidir dos cosas a la vez. Primero, cómo dividir las intensidades en k grupos de intensidades vecinas. Segundo, a qué valor se cambia cada grupo.

**El mejor valor para un grupo**

Empecemos con la segunda decisión: ¿a qué valor se cambia cada grupo? El mejor valor es el promedio ponderado. Cada píxel jala a v hacia su propia intensidad, y el mejor valor está donde los dos lados jalan igual.

**Table de errores**

Ahora veamos el código. Un grupo es un tramo de intensidades vecinas, que empieza en una posición (start) y termina en otra (end). Primero creamos una tabla de errores (error_table), con un espacio para cada grupo posible. Para llenar cada espacio, llamamos a una función que calcula el error de ese grupo (group_error). 

**Error de un grupo**

Para eso, definimos una función que calcula el error de un grupo (group_error). Usa el promedio ponderado para encontrar el mejor valor del grupo, y regresa su error a la tabla de errores. Esta función hace tres cosas.

Primero, encuentra el mejor valor para el grupo, que es el promedio ponderado. En un ciclo, suma el total de píxeles del grupo (total_pixels) y la suma ponderada de sus intensidades (weighted_sum), que es cada intensidad por su número de píxeles. Luego divide la suma ponderada entre el total de píxeles.

Segundo, el promedio puede tener decimales, pero v tiene que ser un entero. Por eso probamos los dos enteros más cercanos: el de abajo (v_low) y el de arriba (v_high).

Tercero, en otro ciclo, calcula el error del grupo con cada uno de estos dos valores. Al final regresa el error más pequeño de los dos, y ese error se guarda en la tabla.

Así, la tabla guarda el error de cada grupo posible, calculado una sola vez. El siguiente paso solo tiene que consultarlo.

**Programación dinámica**

Por último, creamos una tabla de mejores errores (best_error). Cada renglón es un número de grupos (num_groups), en orden: cero grupos, un grupo, dos grupos, hasta k. Cada columna es cuántas intensidades cubrimos, contando desde la primera (covered). Cada espacio guarda el menor error para esas intensidades con ese número de grupos.

La tabla empieza llena de infinito, que quiere decir "todavía no se puede". Solo el primer espacio empieza en cero, porque cero intensidades con cero grupos no tienen error. Ese es el punto de partida.

Llenamos la tabla renglón por renglón: primero con un grupo, luego con dos, hasta k. Para cada espacio, probamos cada lugar donde puede empezar el último grupo (last_start). Es decir, probamos dónde va el último corte.

Cada corte divide el problema en dos partes. La parte de la izquierda es el mejor error antes del corte, con un grupo menos (error_before). Ya está guardado en el renglón de arriba. La parte de la derecha es el error del último grupo (error_last), que sacamos de la tabla de errores. Sumamos las dos partes y guardamos la suma más pequeña.

Esta es la idea de la programación dinámica: cada respuesta se construye con respuestas más pequeñas que ya están guardadas, sin volver a calcularlas.

Al final, la respuesta está en el último espacio de la tabla: todas las d intensidades con k grupos.

**Complejidad**

La complejidad temporal es O de d al cubo, que es cúbica, por la tabla de errores. La complejidad espacial es O de d al cuadrado, que es cuadrática, por las dos tablas.