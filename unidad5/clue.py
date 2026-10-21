import random

print("WELCOME TO THE GAME OF CLUE")
print("You're player 1. The computer is players 2, 3 and 4.")
print("See if you can determine who did the murder, with what weapon and in what room before the computer!")

cards = {
    'people': ['Elena', 'Min', 'Olive', 'Phan', 'Hakeem', 'Noor'],
    'weapons': ['pistol', 'pipe', 'knife', 'plastic bag', 'poison', 'skillet'],
    'rooms': ['kitchen', 'office', 'library', 'bathroom', 'bedroom', 'living room', 'garage', 'basement', 'patio']
}

# Putting secret cards in the envelope

sobre = {}
sobre['people'] = random.choice(cards['people'])
sobre['weapons'] = random.choice(cards['weapons'])
sobre['rooms'] = random.choice(cards['rooms'])

print("The cards for the guilty person, their weapon, and the room in which they committed the murder have been placed in a secret envelop!")

# Dealing the remaining cards

remaining_cards = []
for category in cards.values():             # Getting cards not in the envelope
    for card in category:
        if card not in sobre.values():
            remaining_cards.append(card)

random.shuffle(remaining_cards)
player_cards = {1: [], 2: [], 3: [], 4: []}
player = 1

for card in remaining_cards:
    player_cards[player].append(card)
    player = player % 4 + 1
print(f"Your cards are: {', '.join(player_cards[1])}")


