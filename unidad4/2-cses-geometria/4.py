# Point in Polygon

# n = número de vertices
# m = número de puntos

n, m = map(int, input().split())

vertices = []

for i in range(n):
    vert = list(map(int, input().split()))
    vertices.append(vert)

puntos = []

for i in range(m):
    punto = list(map(int, input().split()))
    puntos.append(punto)

# Check if the points are on a border of the polygon

def cross(vertices, punto):
    for vertice in range(len(vertices)):
        x1, y1 = vertices[vertice]
        x2, y2 = vertices[(vertice + 1) % n]
        x3, y3 = punto
        product = (x2 - x1) * (y3 - y1) - (y2 - y1) * (x3 - x1)
        if product == 0:
            return True
    return False

## Do the ray casting

def ray(vertices, punto):
    x3, y3 = punto
    result = False
    for vertice in range(len(vertices)):
        x1, y1 = vertices[vertice]
        x2, y2 = vertices[(vertice + 1) % n]
        if (y1 > y3) != (y2 > y3):
            x_hit = x1 + (y3 - y1) * (x2 - x1) / (y2 - y1)
            if x_hit > x3:
                result = not result
    return result

for punto in puntos:
    if cross(vertices, punto):
        print("BOUNDARY")
    elif ray(vertices, punto):
        print("INSIDE")
    else:
        print("OUTSIDE")

# Get-Content 4test.txt | python 4.py > INSIDE \nOUTSIDE \nBOUNDARY