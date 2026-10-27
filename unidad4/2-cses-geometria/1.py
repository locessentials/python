# Point Location Test

num = int(input())
coords = []

for i in range(num):
    coord = list(map(int, input().split()))
    coords.append(coord)

pos = 0

def cross(coords):
    x1, y1, x2, y2, x3, y3 = coords[pos]
    product = (x2 - x1) * (y3 - y1) - (y2 - y1) * (x3 - x1)
    if product > 0:
        return("LEFT")
    elif product < 0:
        return("RIGHT")
    else:
        return("TOUCH")

for i in range(num):
    print(cross(coords))
    pos += 1

# Get-Content 1test.txt | python 1.py > LEFT \nRIGHT \nTOUCH