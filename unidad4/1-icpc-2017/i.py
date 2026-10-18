# PREPARACIÓN: LEER LAS ENTRADAS

# m = número de traducciones de letras
# n = número de pares de palabras

m, n = map(int, input().split())

# t = traducciones
# cada letra guarda una lista con todas las letras a las que se puede traducir

t = {}
for _ in range(m):
    a, b = input().split()
    if a not in t:
        t[a] = []
    t[a].append(b)

# p = pares
# cada par guarda la palabra original y la palabra descifrada

p = []              # [('can', 'the'), ('work', 'people'), ('out', 'the')]
for _ in range(n):
    original, deciphered = input().split()
    p.append((original, deciphered))
    print(p)

# FUNCIÓN: PARA CADA LETRA, ENCONTRAR LA CADENA DE TODAS LAS LETRAS EN LAS QUE SE PUEDE TRADUCIR

def find_letters(letter, t):
    found = [letter]
    to_check = [letter]

    while len(to_check) > 0:
        current = to_check.pop()        # saca la última letra de la lista to_check
                                            # y la guarda en current para revisarla
        if current in t:                    # si current tiene traducciones
            for next in t[current]:         # para cada letra a la que se traduce current
                if next not in found:       # si esa letra todavía no está en la lista found
                    found.append(next)      # agregarla a la lista found
                    to_check.append(next)   # agregarla a la lista de letras por revisar
    return found

# RESOLUCIÓN: REVISAR CADA PAR DE PALABRAS

for original, deciphered in p:
    if len(original) != len(deciphered):    # si no tienen la misma longitud, no coinciden
        print("no")
    else:
        match = True                        # empezamos suponiendo que coinciden
        for position in range(len(original)):               # revisar cada posición de las palabras
            found = find_letters(original[position], t)     # ejecutar find_letters 
                                                            # para la letra en la que estamos
                                                            # y guardar la lista de letras 
                                                            # en las que se puede convertir
            if deciphered[position] not in found:
                match = False
        if match:
            print("yes")
        else:
            print("no")

# Get-Content isample1.txt | python i.py > yes \nno \nno \nyes \nyes
# Get-Content isample2.txt | python i.py > yes \nno \nyes