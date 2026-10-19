# Problema L

Recibimos el número de rectángulos, n, y las coordenadas de sus esquinas: n esquinas de arriba a la izquierda y n de abajo a la derecha, cada una con su renglón y su columna. Sin saber cuál va con cuál, tenemos que emparejarlas para que cada dos rectángulos queden uno dentro del otro o separados, sin que sus bordes se crucen ni se encimen. Como n puede llegar a cien mil, usamos una línea de barrido y búsqueda binaria para resolver el problema, en vez de comparar todas las parejas posibles.

**Idea clave**

La línea de barrido es una línea imaginaria que baja por la cuadrícula. Revisamos las esquinas en el orden en que la línea las toca, y solo guardamos los rectángulos que ya se abrieron y todavía no se cierran.

**El código**

Primero, leemos la entrada y guardamos las esquinas en dos listas: una de esquinas de arriba a la izquierda (top_left_corners) y otra de esquinas de abajo a la derecha (bottom_right_corners).

Luego, la función de emparejar las esquinas (match_corners) hace el primer barrido. Para eso juntamos todas las esquinas en una lista de eventos (events). Cada evento guarda el renglón, el tipo de esquina, la columna y la posición de la esquina en su lista de entrada (corner_number). Después ordenamos los eventos por renglón, y en el mismo renglón quedan primero las esquinas de abajo a la derecha. Así una esquina de abajo no cierra un rectángulo que se abrió en su mismo renglón, que no tendría altura.

Después creamos una lista de esquinas abiertas (open_corners), ordenada de izquierda a derecha por columna, y una lista de parejas (partner_of). Un ciclo for recorre los eventos en orden. Si el evento es una esquina de arriba a la izquierda, se abre un rectángulo, y metemos la esquina en su lugar en las esquinas abiertas (insort). Si es una esquina de abajo a la derecha, se cierra un rectángulo, y buscamos su pareja: la esquina abierta más cercana a su izquierda. Para encontrarla usamos búsqueda binaria (bisect_left): como la lista está ordenada, en cada paso miramos la esquina del centro y seguimos solo en la mitad donde puede estar. Elegimos la más cercana porque, si un rectángulo está dentro de otro, el de adentro empieza más a la derecha y se cierra primero. Al encontrar la pareja, la sacamos de las esquinas abiertas (pop) y la guardamos en la lista de parejas. Si no hay ninguna esquina abierta a su izquierda, la función regresa nada (None), y la función principal (main) imprime un error de sintaxis (syntax error).

Pero aunque cada esquina tenga pareja, los rectángulos todavía se pueden cruzar o encimar. Por eso definimos una función de verificar los rectángulos (check_rectangles). La idea es esta: si dos rectángulos se cruzan o se enciman, un borde horizontal de uno toca un lado vertical del otro. Entonces basta revisar cada borde horizontal y contar cuántos lados verticales lo tocan. Deben ser exactamente 2: el lado izquierdo y el lado derecho de su propio rectángulo.

Para saber qué lados verticales hay en el renglón de cada borde, hacemos un segundo barrido. La línea baja otra vez, y guardamos en una lista de columnas activas (active_columns) las columnas de los lados verticales que la línea está cruzando. Un lado vertical va del renglón de arriba de su rectángulo al renglón de abajo, así que su columna entra a la lista en el renglón de arriba y sale en el renglón de abajo.

Para eso, cada rectángulo produce cuatro eventos, es decir, cuatro cosas que pasan cuando la línea llega a cierto renglón. En su renglón de arriba, agregamos sus dos columnas a la lista y revisamos su borde de arriba. En su renglón de abajo, revisamos su borde de abajo y quitamos sus dos columnas de la lista. Ordenamos todos los eventos por renglón. En el mismo renglón, primero agregamos, luego revisamos y al final quitamos, para que al revisar un borde, los lados de su propio rectángulo estén en la lista.

Luego un ciclo for recorre los eventos en orden. Para revisar un borde, contamos cuántas columnas activas hay entre su columna izquierda y su columna derecha. Como la lista está ordenada, no hace falta revisarla toda: con búsqueda binaria encontramos la posición donde empieza ese tramo y la posición donde termina (bisect_left y bisect_right), y la resta de las dos posiciones es cuántas columnas hay en medio. Si no son exactamente 2, otro rectángulo toca este borde, la función regresa falso (False), y la función principal (main) imprime un error de sintaxis (syntax error).

**El resultado**

Por último, si cada esquina encontró pareja y ningún borde toca otro rectángulo, la función principal (main) llama a la función de imprimir los resultados (print_results). 

**Complejidad**

Ordenar cuesta O de n log n, que es cuasilineal, y cada búsqueda binaria cuesta O de log n, que es logarítmica. Pero insort y pop mueven elementos de la lista, y cada uno cuesta O de n. Por eso, en el peor caso, el tiempo es O de n al cuadrado, que es cuadrática. El espacio es O de n, que es lineal.

**Posibles preguntas**

Antes de las funciones, importamos tres herramientas de la biblioteca estándar de Python, bisect, que trabajan con listas ordenadas: insertar en orden (insort) mete un valor en su lugar sin desordenar la lista, y bisect izquierdo y bisect derecho (bisect_left y bisect_right) encuentran en qué posición iría un valor.

Cada esquina es una tupla con su renglón, su columna y su posición en su lista (corner_number), empezando en 0, porque la salida pide la posición de cada pareja.

El tipo vale 0 para las esquinas de abajo a la derecha y 1 para las de arriba a la izquierda.

Una esquina abierta en la misma columna no cuenta (column, -1), porque formaría un rectángulo sin ancho. 

Si hubo un problema, la función principal ya imprimió un error de sintaxis (syntax error) y terminó, así que no imprime ninguna pareja.

Un ciclo for recorre la lista de parejas. Para cada esquina de arriba a la izquierda, esa lista guarda la posición de su pareja en la lista de esquinas de abajo a la derecha. Imprimimos cada posición más uno (bottom_right_number + 1), cada una en su propio renglón, porque en el código las posiciones empiezan en 0 y la salida empieza a contar en 1.

