# Euclid's algorithm
# For finding the greatest common divisor (GCD) of two numbers, written recursively

a, b = map(int, input().split())

def euclid(a, b):
    if b == 0:              # Fin de la cadena. Pregunta: ¿He terminado?
        return a            # Si es así, regresa el b que está en la posición a
    return euclid(b, a % b)

print(euclid(a, b))

# euclid(48, 18)   48 % 18 = 12
# euclid(18, 12)   18 % 12 = 6
# euclid(12, 6)    12 % 6  = 0
# euclid(6, 0)     b is 0 → return 6