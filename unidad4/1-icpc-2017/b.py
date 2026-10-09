n = int(input())
my_hand = input().split()

sugs = []

for i in range(n):
    sug = input().split()
    sugs.append(sug)

people = "ABCDEF"
weapons = "GHIJKL"
rooms = "MNOPQRSTU"

holder = {}                 # {'A': 1, 'B': 1, 'C': 1, 'D': 1, 'H': 1, 'M': 2}
for card in my_hand:
    holder[card] = 1

# - no evidence was produced
# * hidden evidence was produced

lacks = {1: [], 2: [], 3: [], 4: []}
unresolved = []

for i, sug in enumerate(sugs):
    suggester = i % 4 + 1
    cards = sug[:3]
    responder = suggester
    for r in sug[3:]:
        responder = responder % 4 + 1   # move one player to the right
        if r == '-':
            lacks[responder].extend(cards) # Not sure how to get the responder number since, responder just got changed to the next person
        elif r == '*':
            unresolved.append((responder, cards))
        else:
            holder[r] = responder



Take the holder cards and cross them off the people, weapon and room strings


