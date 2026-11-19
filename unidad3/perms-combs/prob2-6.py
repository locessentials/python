# Sign of the permutation
# sgn(σ) = sgn(A) = (-1)^n = (-1)^(number of transpositions)

def sgn(b):         # b = list to permute
    a = b.copy()    #
    c = 0           # counter
    i = 0           # index
    while True:
        if a[i] > a[i+1]:
            a[i], a[i+1] = a[i+1], a[i]
            c += 1
            i = 0
            continue
        i = i + 1
        if i == (len(a) - 1):
            break
    print("Sorted:", a)
    print("Count:", c)
    return (-1)**(c%2)

b = [6, 3, 1, 5, 4, 2]
print("Sign:", sgn(b))
