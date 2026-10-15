# LEER LAS ENTRADAS

def read_input():
    # Leer el primer renglón: n (el largo de la secuencia escondida) y s (cuántos patrones siguen)
    first_line = input().split()
    sequence_length = int(first_line[0])
    pattern_count = int(first_line[1])

    # Leer los s patrones, uno por renglón, y guardarlos en una lista
    # Se guardan en el orden de la entrada, porque si dos patrones empatan, deben quedar en ese orden
    patterns = []
    for pattern_number in range(pattern_count):
        pattern = input().strip()
        patterns.append(pattern)

    return sequence_length, patterns

# Z-FUNCTION

def z_function(pattern):
    pattern_length = len(pattern)

    # match_lengths guarda, para cada posición, cuántas letras seguidas coinciden con el inicio del patrón
    match_lengths = [0] * pattern_length

    # La ventana es el tramo más a la derecha que ya sabemos que coincide con el inicio del patrón
    # Va de window_start hasta window_end, sin incluir window_end
    window_start = 0
    window_end = 0

    for position in range(1, pattern_length):
        match_length = 0

        # Si la posición está dentro de la ventana, aprovechar lo que ya se calculó en el inicio del patrón
        if position < window_end:
            matching_position_at_start = position - window_start
            letters_left_in_window = window_end - position
            match_length = min(match_lengths[matching_position_at_start], letters_left_in_window)

        # Seguir comparando letra por letra mientras coincidan y no se llegue al final del patrón
        while position + match_length < pattern_length and pattern[match_length] == pattern[position + match_length]:
            match_length = match_length + 1

        match_lengths[position] = match_length

        # Si esta coincidencia llega más lejos que la ventana, mover la ventana aquí
        if position + match_length > window_end:
            window_start = position
            window_end = position + match_length

    return match_lengths

# OVERLAP FLAGS

def overlap_flags(pattern, sequence_length):
    pattern_length = len(pattern)
    match_lengths = z_function(pattern)

    # flags guarda un 1 si el patrón se encima consigo mismo en ese paso, y un 0 si no
    flags = []

    for shift in range(1, pattern_length):
        # Si las dos copias del patrón no caben en la secuencia escondida, este paso y los siguientes no importan
        if pattern_length + shift > sequence_length:
            break

        # El patrón se encima en este paso si la coincidencia llega hasta el final del patrón
        if shift + match_lengths[shift] == pattern_length:
            flags.append(1)
        else:
            flags.append(0)

    return flags

# ORDENAR

def get_flags(pattern_with_flags):
    # Regresar solo las banderas, para que el ordenamiento compare solo eso
    return pattern_with_flags[0]

def sort_patterns(patterns, sequence_length):
    # Calcular las banderas de cada patrón una sola vez y guardarlas junto al patrón
    patterns_with_flags = []
    for pattern in patterns:
        flags = overlap_flags(pattern, sequence_length)
        patterns_with_flags.append((flags, pattern))

    # Ordenar por las banderas: Python compara las listas de izquierda a derecha y se detiene en la primera diferencia
    # sorted() es estable: si dos patrones empatan, quedan en el orden de la entrada
    sorted_pairs = sorted(patterns_with_flags, key=get_flags)

    # Quedarse solo con los patrones, ya ordenados
    sorted_patterns = []
    for pair in sorted_pairs:
        sorted_patterns.append(pair[1])

    return sorted_patterns

# IMPRIMIR LA SALIDA

def main():
    sequence_length, patterns = read_input()
    sorted_patterns = sort_patterns(patterns, sequence_length)
    for pattern in sorted_patterns:
        print(pattern)

main()

# Get-Content ksample1.txt | python k.py > PS \nPP \nRR \nSS
# Get-Content ksample2.txt | python k.py > PRSPS \nPPSPP \nSSSSS




