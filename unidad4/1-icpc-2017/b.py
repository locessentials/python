# Organización de los datos de entrada

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

for i, sug in enumerate(sugs):          # 
    suggester = i % 4 + 1
    cards = sug[:3]
    responder = suggester
    for r in sug[3:]:
        responder = responder % 4 + 1   # current player
        if r == '-':                            # - no evidence was produced
            lacks[responder].extend(cards) 
        elif r == '*':                          # * hidden evidence was produced
            unresolved.append((responder, cards))
        else:
            holder[r] = responder

# Retry

changed = True
while changed:
    changed = False
    for player, cards in unresolved:
        possible = []
        for card in cards:
            if card in holder and holder[card] != player:
                continue
            if card in lacks[player]:
                continue                    
            possible.append(card)

        if len(possible) == 1:
            card = possible[0]
            if card not in holder:          
                holder[card] = player
                changed = True

# Determine answer for people

left_people = []
for card in people:
    if card not in holder:
        left_people.append(card)

person_answer = '?'
for card in left_people:
    if card in lacks[2] and card in lacks[3] and card in lacks[4]:
        person_answer = card                 # proven: nobody has it
if len(left_people) == 1:
    person_answer = left_people[0]           # only one card left

# Determine answer for weapons

left_weapons = []
for card in weapons:
    if card not in holder:
        left_weapons.append(card)

weapon_answer = '?'
for card in left_weapons:
    if card in lacks[2] and card in lacks[3] and card in lacks[4]:
        weapon_answer = card                 # proven: nobody has it
if len(left_weapons) == 1:
    weapon_answer = left_weapons[0]           # only one card left

# Determine answer for rooms

left_rooms = []
for card in rooms:
    if card not in holder:
        left_rooms.append(card)

room_answer = '?'
for card in left_rooms:
    if card in lacks[2] and card in lacks[3] and card in lacks[4]:
        room_answer = card                 # proven: nobody has it
if len(left_rooms) == 1:
    room_answer = left_rooms[0]           # only one card left

print(person_answer + weapon_answer + room_answer)

# Get-Content bsample1.txt | python b.py
# Get-Content bsample2.txt | python b.py
# Get-Content bsample3.txt | python b.py