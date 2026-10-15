import sys
from bisect import bisect_left, bisect_right, insort

# LEER LA ENTRADA

def read_input():
    # Leemos el número de rectángulos
    n = int(sys.stdin.readline())

    # Guardamos cada esquina de arriba a la izquierda con su número original
    top_left_corners = []
    for corner_number in range(n):
        row, column = map(int, sys.stdin.readline().split())
        top_left_corners.append((row, column, corner_number))

    # Guardamos cada esquina de abajo a la derecha con su número original
    bottom_right_corners = []
    for corner_number in range(n):
        row, column = map(int, sys.stdin.readline().split())
        bottom_right_corners.append((row, column, corner_number))

    return n, top_left_corners, bottom_right_corners

# EMPAREJAR LAS ESQUINAS

BOTTOM_RIGHT = 0
TOP_LEFT = 1

def match_corners(n, top_left_corners, bottom_right_corners):
    # Juntamos todas las esquinas en una sola lista
    events = []
    for row, column, corner_number in top_left_corners:
        events.append((row, TOP_LEFT, column, corner_number))
    for row, column, corner_number in bottom_right_corners:
        events.append((row, BOTTOM_RIGHT, column, corner_number))

    # Ordenamos por renglón; en el mismo renglón, primero las de abajo a la derecha
    events.sort()

    # Esquinas abiertas, ordenadas por columna: (columna, número de esquina)
    open_corners = []
    partner_of = [-1] * n

    for row, corner_type, column, corner_number in events:
        if corner_type == TOP_LEFT:
            # Abrimos un rectángulo: guardamos la esquina en su lugar por columna
            insort(open_corners, (column, corner_number))
        else:
            # Buscamos la esquina abierta más a la derecha que esté a la izquierda de esta
            position = bisect_left(open_corners, (column, -1))
            if position == 0:
                # No hay ninguna: no se puede formar el rectángulo
                return None
            open_column, top_left_number = open_corners.pop(position - 1)
            partner_of[top_left_number] = corner_number

    return partner_of

# VERIFICAR LOS RESULTADOS

ADD = 0
CHECK = 1
REMOVE = 2

def check_rectangles(top_left_corners, bottom_right_corners, partner_of):
    # Armamos los eventos de cada rectángulo
    events = []
    for top_row, left_column, top_left_number in top_left_corners:
        bottom_row, right_column, bottom_right_number = bottom_right_corners[partner_of[top_left_number]]
        # En el renglón de arriba: abrimos los dos lados verticales y revisamos el borde de arriba
        events.append((top_row, ADD, left_column, right_column))
        events.append((top_row, CHECK, left_column, right_column))
        # En el renglón de abajo: revisamos el borde de abajo y cerramos los lados verticales
        events.append((bottom_row, CHECK, left_column, right_column))
        events.append((bottom_row, REMOVE, left_column, right_column))

    # Ordenamos por renglón; en el mismo renglón: primero abrir, luego revisar, al final cerrar
    events.sort()

    # Columnas de los lados verticales abiertos, en orden
    active_columns = []

    for row, event_type, left_column, right_column in events:
        if event_type == ADD:
            insort(active_columns, left_column)
            insort(active_columns, right_column)
        elif event_type == CHECK:
            # Contamos los lados verticales que tocan este borde horizontal
            count = bisect_right(active_columns, right_column) - bisect_left(active_columns, left_column)
            # Solo deben tocarlo los dos lados de su propio rectángulo
            if count != 2:
                return False
        else:
            active_columns.pop(bisect_left(active_columns, left_column))
            active_columns.pop(bisect_left(active_columns, right_column))

    return True

# IMPRIMIR LOS RESULTADOS

def print_results(partner_of):
    # Sumamos 1 porque la salida empieza a contar en 1
    output_lines = []
    for bottom_right_number in partner_of:
        output_lines.append(str(bottom_right_number + 1))
    print("\n".join(output_lines))


def main():
    n, top_left_corners, bottom_right_corners = read_input()

    partner_of = match_corners(n, top_left_corners, bottom_right_corners)
    if partner_of is None:
        print("syntax error")
        return

    if not check_rectangles(top_left_corners, bottom_right_corners, partner_of):
        print("syntax error")
        return

    print_results(partner_of)

main()

# Get-Content lsample1.txt | python l.py > 2 \n1
# Get-Content lsample2.txt | python l.py > 1 \n2
# Get-Content lsample3.txt | python l.py > syntax error
# Get-Content lsample4.txt | python l.py > syntax error