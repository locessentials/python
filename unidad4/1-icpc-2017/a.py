
# Collects the inputs
n = int(input())
vertices = []

for p in range(n):
    point = tuple(map(int, input().split())) 
    vertices.append(point)

print(vertices)

# Calculates the cross product for use in 
def cross(A, B, P):
    x1, y1 = A
    x2, y2 = B
    x3, y3 = P
    return (x2-x1) * (y3-y1) - (y2-y1) * (x3-x1)

lines = []

def crosses(A, B, C, D):
    return cross(A, B, C) * cross(A, B, D) < 0