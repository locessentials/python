# Euclid's algorithm
# For finding the greatest common divisor (GCD) of two numbers, written recursively
# used to calculate the lowest common multiple

a, b = map(int, input().split())

def euclid(a, b):
    if b == 0:
        return a
    return euclid(b, a % b)

def lcm(a, b):
    gcd = euclid(a, b)
    result = a * b // gcd
    print(f"Lowest common multiple: {a} * {b} // {gcd} = {result}")
    return result

lcm(a, b)