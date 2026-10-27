# Point in Polygon

# n = número de vertices
# m = número de puntos

n, m = map(int, input().split())

vertices = []

for i in range(n):
    vert = list(map(int, input().split()))
    vertices.append(vert)

print(vertices)

puntos = []

for i in range(m):
    punto = list(map(int, input().split()))
    puntos.append(punto)

print(puntos)

# Get-Content 4test.txt | python 4.py > INSIDE \nOUTSIDE \nBOUNDARY