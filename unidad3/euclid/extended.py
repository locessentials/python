# a * x + b * y = mcd(a, b)
# 48 * (-1) + 18 * 3 = 6

a, b = map(int, input().split())

def eux(a, b):
    if b == 0:
        return (a, 1, 0)
    g, x1, y1 = eux(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    return (g, x, y)

print(eux(a, b))