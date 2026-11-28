# Prueba de memoría

def triangle(n):

    A = []
    for renglon in range(n+1):
        nuevo_renglon = [1] * (renglon + 1)
        for k in range(1, renglon):
            nuevo_renglon[k] = A[renglon - 1][k - 1] + A[renglon - 1][k] 
        A.append(nuevo_renglon)
    return A

def lookup(A, n, k):
    return A[n][k]

n=10
k=3

A = triangle(n)
print(lookup(A, n, k))
