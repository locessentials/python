# Organizar los datos de entradas

n = int(input())                    # Leer el número de sugerencias hechas
my_hand = input().split()           # Leer mis cinco cartas y separarlas en una lista

sugs = []                           # Crear una lista vacía para guardar cada sugerencia

for i in range(n):                  # Repetir n veces, una por sugerencia
    sug = input().split()           # Separar los elementos de la sugerencia en una lista
    sugs.append(sug)    # Agregar la sugerencia completa como un solo elemento (append, no extend),
                        # así sugs queda como lista de listas: [['F','G','M','M'], ['F','H','M','-','*']]

people = "ABCDEF"                   # Cartas de sospechosos, como cadena (string)
weapons = "GHIJKL"                  # Cartas de armas, como cadena
rooms = "MNOPQRSTU"                 # Cartas de habitaciones, como cadena

holder = {}                         # Diccionario carta : jugador que la tiene
                                    # (ej. tras la muestra 2: {'A': 1, 'B': 1, 'C': 1, 'D': 1, 'H': 1, 'M': 2, 'F': 4})
for card in my_hand:                # Para cada una de mis cartas
    holder[card] = 1                # Registrar que el jugador 1 (yo) la tiene

lacks = {1: [], 2: [], 3: [], 4: []}    # Cartas que cada jugador indicó no tener (respondió '-')
                                        # (ej. tras la muestra 2: {3: ['F', 'H', 'M']})
unresolved = []                         # Pistas '*': (jugador, [las tres cartas]) 
                                        # cuando alguien mostró una carta que no vimos
                                        # (ej. tras la muestra 2: [(4, ['F', 'H', 'M'])])

# Procesar cada sugerencia

for i, sug in enumerate(sugs):              # Recorrer las sugerencias 
                                            # con su posición (i) y su contenido (sug)
    suggester = i % 4 + 1                   # Jugador que hace la sugerencia: i módulo 4 da un residuo
                                            # entre 0 y 3; al sumarle 1 se obtiene el jugador en turno (1–4)
    cards = sug[:3]                         # Las tres cartas sugeridas (posiciones 0, 1 y 2)
    responder = suggester                   # Punto de partida para contar a los que responden
    for r in sug[3:]:                       # Recorrer cada respuesta (de la posición 3 en adelante)
        responder = responder % 4 + 1       # Avanzar al jugador de la derecha: él da la respuesta r
        if r == '-':                                # '-': no tiene ninguna de las tres cartas
            lacks[responder].extend(cards)          # Agregar las tres cartas, una por una, 
                                                    # a su lista de lacks
        elif r == '*':                              # '*': mostró una carta, pero no vimos cuál
            unresolved.append((responder, cards))   # Guardar (jugador, cartas) para resolverla después
        else:                                       # Una letra: vimos exactamente qué carta mostró
            holder[r] = responder                   # Registrar que este jugador tiene esa carta

# Reintentar las pistas '*' sin resolver

changed = True                                  # Empezar en True para que la primera pasada se ejecute
while changed:                                  # Repetir mientras la última pasada 
                                                # haya descubierto algo nuevo
    changed = False                             # Suponer que esta pasada no descubrirá nada
    for player, cards in unresolved:            # Recorrer cada pista: jugador que mostró 
                                                # y las tres cartas
        possible = []                           # Cartas que este jugador pudo haber mostrado
        for card in cards:                      # Revisar cada una de las tres cartas
            if card in holder and holder[card] != player:   # Si la carta ya está 
                                                            # en el diccionario de cartas
                                                            # asignada a otro jugador
                continue                        # Excluir de las posibilidades: la tiene otro jugador
            if card in lacks[player]:           # Si la carta aparece en la lista lacks de este jugador
                continue                        # Saltar a la siguiente carta sin agregar esta a possible
            possible.append(card)               # Si no se quitó, sigue siendo posible

        if len(possible) == 1:                  # Si solo queda una carta posible, esa fue la que mostró
            card = possible[0]                  # Tomar esa única carta
            if card not in holder:              # Solo cuenta si es un dato nuevo
                holder[card] = player           # Registrar que este jugador la tiene
                changed = True                  # Hubo un descubrimiento: hará falta otra pasada

# Determinar la respuesta para la persona asesina

left_people = []                                # Crear una lista vacía de personas sin ubicar
for card in people:                             # Para cada carta en people
    if card not in holder:                      # Si no está en holder (nadie la tiene registrada)
        left_people.append(card)                # Agregarla a left_people

person_answer = '?'                             # Valor predeterminado: '?' si no se puede determinar
for card in left_people:                        # Para cada carta sin ubicar
    if card in lacks[2] and card in lacks[3] and card in lacks[4]:
                                                # Si lxs jugadorxs 2, 3 y 4 dijeron no tenerla
        person_answer = card                    # Nadie la tiene: está en el sobre
if len(left_people) == 1:                       # Además, si solo queda una carta sin ubicar
    person_answer = left_people[0]              # Esa carta tiene que estar en el sobre

# Determinar la respuesta para la arma usada

left_weapons = []                               # Misma lógica que para la persona asesina
for card in weapons:
    if card not in holder:
        left_weapons.append(card)

weapon_answer = '?'
for card in left_weapons:
    if card in lacks[2] and card in lacks[3] and card in lacks[4]:
        weapon_answer = card
if len(left_weapons) == 1:
    weapon_answer = left_weapons[0]

# Determinar la respuesta para la habitación donde ocurrió el asesinato

left_rooms = []                                 # Misma lógica que para la persona asesina
for card in rooms:
    if card not in holder:
        left_rooms.append(card)

room_answer = '?'
for card in left_rooms:
    if card in lacks[2] and card in lacks[3] and card in lacks[4]:
        room_answer = card 
if len(left_rooms) == 1:
    room_answer = left_rooms[0]

print(person_answer + weapon_answer + room_answer)  # Imprimir la respuesta: persona, arma y habitación
                                                    # ('?' si no se puede determinar)

# Get-Content bsample1.txt | python b.py > AGM
# Get-Content bsample2.txt | python b.py > E??
# Get-Content bsample3.txt | python b.py > ???