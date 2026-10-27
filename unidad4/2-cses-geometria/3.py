# Polygon Area

n = int(input())

vertices = []

for i in range(n):
    vert = list(map(int, input().split()))
    vertices.append(vert)

def multaddx():
    total = 0
    for i in range(n):
        pos_x = i  
        pos_y = (i + 1) % n
        i = vertices[pos_x][0] * vertices[pos_y][1]
        total += i
    return total

def multaddy():
    total = 0
    for i in range(n):
        pos_y = i
        pos_x = (i + 1) % n
        y = vertices[pos_y][1] * vertices[pos_x][0]
        total += y
    return total

area2 = multaddx() - multaddy()
area2 = abs(area2)
print(area2)

# Get-Content 3test.txt | python 3.py > 16