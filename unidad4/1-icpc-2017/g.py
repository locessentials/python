# LEER LA ENTRADA

# w = ancho
# h = altura
# . = celda vacía
# # = celda no vacía

w, h = map(int, input().split())

lines = []
for _ in range(h):
    lines.append(input())

# Convertir cada línea en una lista de 0 y 1 (0 = celda vacía, 1 = celda llena)
grid = []
for line in lines:
    row = []
    for character in line:
        if character == "#":
            row.append(1)
        else:
            row.append(0)
    grid.append(row)





# Get-Content gsample1.txt | python g.py > .# \n##
# Get-Content gsample2.txt | python g.py > #### \n#..# \n#.## \n###.
# Get-Content gsample3.txt | python g.py > #