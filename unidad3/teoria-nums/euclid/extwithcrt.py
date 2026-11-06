# Extended Euclid - Recursive

def ext_euclid(a, b):
    if b == 0:
        return (a, 1, 0)
    g, x1, y1 = ext_euclid(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    return (g, x, y)

ext_euclid(48, 18)

print(ext_euclid(35, 3))
print(ext_euclid(21, 5))
print(ext_euclid(15, 7))

# Chinese Remainder Theorem

def crt(remainders, moduli):            # crt(r, m) x ≡ r (mod m), where r and m are corresponding lists
    M = 1                               # Initialize to 1, since x*1 = x
    for m in moduli:
        M *= m                          # M = product of all moduli

    total = 0                           # Running sum initialized at 0
    for r, m in zip(remainders, moduli):    # pairs up the items from each list
        Mi = M // m          # = product of every modulus except the current m
        g, inv, _ = ext_euclid(Mi, m)   # g = GCD, inv = inverse of Mi mod m, or x that ext_euclid returns, _ catches y returned from ext_euclid
        total += r * Mi * inv
    return total % M                    # makes it the smallest non-negative answer

print(crt([2, 3, 2], [3, 5, 7]))   # 23

"""
CRT solves for x:
x ≡ 2 (mod 3) | x % 3 == 2
x ≡ 3 (mod 5) | x % 5 == 3
x ≡ 2 (mod 7) | x % 7 == 2
"""

"""
# Extended Euclid - Iterative

def ext_euclid_it(a, b):
    old_r, r = a, b
    old_x, x = 1, 0
    old_y, y = 0, 1
    while r != 0:
        q = old_r // r
        old_r, r = r, old_r - q * r
        old_x, x = x, old_x - q * x
        old_y, y = y, old_y - q * y
    return (old_r, old_x, old_y)

# Extended Euclid - Recursive with print statements

def ext_euclid_print(a, b):
    print(f"called with ({a}, {b})")
    if b == 0:
        print(f"base case ({a}, {b}) returns {(a, 1, 0)}")
        return (a, 1, 0)
    g, x1, y1 = ext_euclid_print(b, a % b)
    print(f"({a}, {b}) received g={g}, x1={x1}, y1={y1}")
    x = y1
    y = x1 - (a // b) * y1
    print(f"({a}, {b}) returns {(g, x, y)}")
    return (g, x, y)

GOING DOWN
| Call | a | b | a//b | a%b |
| ---- | - | - | ---- | ---- |
| 1 | 48 | 18 | 2 | 12 |
| 2 | 18 | 12 | 1 | 6 |
| 3 | 12 | 6 | 2 | 0 |
| 4 | 6 | 0 | N/A | N/A |

gcd = 6

COMING UP
| Call | gets (x1, y1) | x=y1 | y = x1 − (a//b)·y1 | check |
| ---- | ------------- | ---- | ------------------ | ----- |
| 4 | N/A | 1 | 0 | 6*1 + 0*0 = 6 |
| 3 | (1, 0) | 0 | 1 = 1 - (12//6) * 0 | 12*0 + 6*1 = 6 |
| 2 | (0, 1) | 1 | -1 = 0 - (18//12) * 1 | 18*1 + 12*-1 = 6  |
| 1 | (1, -1) | -1 | 3 = 1 - (48//18) * -1 | 48*-1 + 18*3 = 6 |

returns 6, -1, 3

"""