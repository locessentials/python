# Euclid's algorithm
# For finding the greatest common divisor (GCD) of two numbers, written recursively
# with print statements so the program shows its work

a, b = map(int, input().split())

def euclid(a, b, call=1):
    if b == 0:                      # gcd(a, 0) = a; also avoids dividing by zero
        print(f"Call {call}: b = 0, so the greatest common divisor is {a}")
        return a

    quotient = a // b
    remainder = a % b
    print(f"Call {call}: a = {a}, b = {b}; quotient = {quotient}, remainder = {remainder}")

    if remainder == 0:
        print(f"Greatest common divisor: {b}")   # b divides a exactly, so b is the gcd
        return b
    else:
        print(f"Next: euclid(b, a % b) calls euclid({b}, {remainder})")
        return euclid(b, remainder, call + 1)

euclid(a, b)