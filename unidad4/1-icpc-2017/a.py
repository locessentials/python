

n = int(input())
vertices = []

for p in range(n):
    point = tuple(map(int, input().split())) 
    vertices.append(point)

print(vertices)

def cross(x, y):
    