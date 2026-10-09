
# Collects the inputs
n = int(input())
vertices = []

for p in range(n):
    point = tuple(map(int, input().split())) 
    vertices.append(point)

# Returns a number whose sign says which side of the line AB the point P is on
def cross(A, B, P):
    x1, y1 = A
    x2, y2 = B
    x3, y3 = P
    return (x2-x1) * (y3-y1) - (y2-y1) * (x3-x1)

# crossing test: returns True if wall CD crosses the line AB (its ends are on opposite sides)
def crosses(A, B, C, D):
    return cross(A, B, C) * cross(A, B, D) < 0

# returns t: where wall CD hits the line AB (0 at A, 1 at B, >1 past B, <0 behind A)
def crossing_t(A, B, C, D):
    a = cross(C, D, A)
    b = cross(C, D, B)
    return a / (a - b)

# returns True if point P lies on wall CD (allowing for tiny rounding errors)
def on_wall(C, D, P):
    x1, y1 = C
    x2, y2 = D
    x, y = P
    length = ((x2 - x1)**2 + (y2 - y1)**2) ** 0.5
    if abs(cross(C, D, P)) > 1e-7 * length:   # not on the wall's line
        return False
    # on the line: is it between C and D?
    return min(x1, x2) - 1e-7 <= x <= max(x1, x2) + 1e-7 and \
           min(y1, y2) - 1e-7 <= y <= max(y1, y2) + 1e-7

# ray casting: returns True if P is inside the polygon or on its border
def inside(P):
    x, y = P
    result = False
    for i in range(n):
        C = vertices[i]
        D = vertices[(i + 1) % n]          # % n wraps the last vertex back to the first
        if on_wall(C, D, P):
            return True                    # on the border counts as inside
        x1, y1 = C
        x2, y2 = D
        if (y1 > y) != (y2 > y):           # wall reaches across P's height
            x_hit = x1 + (y - y1) * (x2 - x1) / (y2 - y1)
            if x_hit > x:                  # hit is to the right of P
                result = not result        # each crossing flips inside/outside
    return result

# returns the point at position t on the line AB
def point_at(A, B, t):
    x1, y1 = A
    x2, y2 = B
    return (x1 + t * (x2 - x1), y1 + t * (y2 - y1))

# checks whether the piece of line AB between t1 and t2 is inside
def piece_inside(A, B, t1, t2):
    return inside(point_at(A, B, (t1 + t2) / 2))

best = 0.0

for i in range(n):
    for j in range(i + 1, n):
        A = vertices[i]
        B = vertices[j]
        dx = B[0] - A[0]
        dy = B[1] - A[1]
        ab_length = (dx**2 + dy**2) ** 0.5

        # 1. every t where the border touches the line AB
        ts = []
        for V in vertices:                       # vertices lying on the line
            if cross(A, B, V) == 0:
                ts.append(((V[0] - A[0]) * dx + (V[1] - A[1]) * dy) / (dx**2 + dy**2))
        for k in range(n):                       # walls cutting across the line
            C = vertices[k]
            D = vertices[(k + 1) % n]
            if crosses(A, B, C, D):
                ts.append(crossing_t(A, B, C, D))

        # 2. sort them; they cut the line into pieces
        ts.sort()
        start = ts.index(0.0)                    # position of A in the list
        end = ts.index(1.0)                      # position of B in the list

        # 3a. every piece between A and B must be inside, or skip this pair
        ok = True
        for k in range(start, end):
            if not piece_inside(A, B, ts[k], ts[k + 1]):
                ok = False
                break
        if not ok:
            continue

        # 3b. extend backward past A while the pieces stay inside
        lo = start
        while lo > 0 and piece_inside(A, B, ts[lo - 1], ts[lo]):
            lo -= 1

        # 3c. extend forward past B while the pieces stay inside
        hi = end
        while hi < len(ts) - 1 and piece_inside(A, B, ts[hi], ts[hi + 1]):
            hi += 1

        # 4. runway length = (fraction of AB) × length of AB
        best = max(best, (ts[hi] - ts[lo]) * ab_length)

print(f"{best:.9f}")

# Get-Content asample1.txt | python a.py