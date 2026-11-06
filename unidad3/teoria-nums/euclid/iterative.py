# Euclid's algorithm
# For finding the greatest common divisor (GCD) of two numbers, written iteratively

a, b = map(int, input().split())

def euclid(a, b):
    while b != 0:
        residuo = a % b
        a = b
        b = residuo
    return a

print(euclid(a, b))