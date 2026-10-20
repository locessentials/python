# Problema E

En el problema E recibimos los datos de un viaje: **n** segmentos, cada uno con una distancia **d** y una lectura **s** de un velocímetro sin calibrar, y el tiempo total **t** que tomó el viaje completo. Con estos datos tenemos que encontrar una constante c que, sumada a cada lectura, da la velocidad real: s más c (s + c).

La constante tiene que cumplir dos condiciones. Primero, si dividimos la distancia de cada segmento entre su velocidad real y sumamos todos esos tiempos, el resultado tiene que ser el tiempo total **t**. Segundo, la velocidad real de cada segmento tiene que ser positiva, es decir, s más c tiene que ser mayor que cero (s + c > 0).

No hay una fórmula directa para encontrar c, porque c está dentro de cada división. Pero sí sabemos algo útil: cuando c sube, todas las velocidades suben y el tiempo total baja. Por eso seguimos una estrategia de búsqueda binaria sobre la respuesta. Probamos el punto medio del rango posible de c, calculamos el tiempo total que daría y quitamos la mitad donde c no puede estar. Repetimos hasta que el rango es mucho más pequeño que una millonésima (10⁻⁶), que es la precisión que pide el problema.

Primero establecemos los límites de la búsqueda. Para el límite inferior usamos la lectura más baja de todos los segmentos, que llamamos la s más baja (low_s), porque la velocidad real tiene que ser mayor que cero. Si a la lectura más baja le sumamos su opuesto, el resultado es cero. Por eso el límite inferior de c es menos la s más baja (−low_s), y la respuesta tiene que ser mayor que ese valor.

Para el límite superior usamos los límites que da el problema y pensamos en el peor caso: mil segmentos de mil millas cada uno, o sea, un millón de millas en una sola hora. Para eso, la velocidad real tendría que ser de alrededor de un millón de millas por hora. Además, el valor absoluto de s es menor o igual que mil (|s| ≤ 1000), es decir, s está entre menos mil y mil. En el peor caso, s vale menos mil, y menos mil más c tiene que dar un millón. Entonces la c más grande es un millón mil (1,001,000). Para tener margen, en el código usamos un millón mil uno (1,001,001) como límite superior.

Con estos dos límites, menos la s más baja como límite inferior y un millón mil uno como límite superior para c, podemos ejecutar la búsqueda binaria.

Primero definimos una función, T de c (T(c)), que calcula el tiempo total del viaje si la constante fuera c. Para cada segmento, divide la distancia d entre la velocidad real, s más c, y suma los tiempos de todos los segmentos.

Luego, en un ciclo for, calculamos el punto medio (mid) entre el límite inferior (lo) y el límite superior (hi). Lo evaluamos con la función T, y hay dos resultados posibles.

Si el tiempo que da es mayor que el tiempo total real, el viaje tarda demasiado y las velocidades son demasiado lentas. Como c tiene que ser más grande, quitamos todos los valores menores que el punto medio, así que el límite inferior pasa a ser el punto medio.

Si el tiempo que da es menor o igual que el tiempo total real, el viaje dura muy poco y las velocidades son demasiado rápidas. Como c tiene que ser más pequeña, quitamos todos los valores mayores que el punto medio, así que el límite superior pasa a ser el punto medio.

Repetimos esto cien veces. Como cada repetición reduce el rango a la mitad, con unas cuarenta ya llegamos a una millonésima. Usamos cien porque es un valor común en búsquedas binarias con decimales y alcanza de sobra.

Después de las cien repeticiones, el límite inferior y el límite superior son prácticamente el mismo número. Ese valor es nuestra c: la constante que, con las distancias y lecturas de cada segmento, da el tiempo total del viaje. Al final imprimimos el límite superior con nueve decimales.

## Complejidad
La complejidad temporal es o de cien por n (O(100 × n)), que es lineal porque cien es una constante. En cada una de las cien repeticiones, la función T de c (T(c)) recorre los n segmentos, así que como mucho hace cien por mil, es decir, cien mil divisiones. La complejidad espacial es o de n (O(n)), también lineal, por la lista de segmentos (segmentos). La operación que determina la complejidad es la división de d entre s más c (d / (s + c)), dentro de la función T de c.