# Line Segment Intersection

t = int(input())

coords = []

for i in range(t):
    coord = list(map(int, input().split()))
    coords.append(coord)

def cross(a1, b1, a2, b2, a3, b3):
    product = (a2 - a1) * (b3 - b1) - (b2 - b1) * (a3 - a1)
    return product

pos = 0

def intersect(coords):
    x1, y1, x2, y2, x3, y3, x4, y4 = coords[pos]
    cross1 = cross(x1, y1, x2, y2, x3, y3)
    cross2 = cross(x1, y1, x2, y2, x4, y4)
    cross3 = cross(x3, y3, x4, y4, x1, y1)
    cross4 = cross(x3, y3, x4, y4, x2, y2)
    if cross1 * cross2 > 0:
        print("NO")
    elif cross3 * cross4 > 0:
        print("NO")
    elif cross1 == 0 and cross2 == 0 and (max(x1, x2) < min(x3, x4) or max(x3, x4) < min(x1, x2) or max(y1, y2) < min(y3, y4) or max(y3, y4) < min(y1, y2)):
        print("NO")
    else:
        print("YES")

for i in range(t):
    intersect(coords)
    pos += 1

# Get-Content 2test.txt | python 2.py > NO \nYES \nYES \nYES \nYES