# Triángulo de Pascal

# n = renglón
# k = posición en el renglón

n = 5
k = 2

def pascal(n, k):
    if k == 0 or n == k:
        return 1                                # pone los 1 en los dos lados (relativamente) verticales del triángulo
    return pascal(n-1, k-1) + pascal(n-1, k)    # pascal(n-1, k-1) = number up and to the left: one row up, one position left
                                                # pascal(n-1, k) = number up and to the right: one row up, same position

print(f"Recursive function: For row {n} position {k}, the value is {pascal(n, k)}")

# Lambda function

pascal = lambda n, k : 1 if k == 0 or n == k else pascal(n-1, k-1) + pascal(n-1, k)

print(f"Recursive lambda function: For row {n} position {k}, the value is {pascal(n, k)}")

# Programación dinámica

# Create the triangle
def triangle(n):

    A = []
    for renglon in range(n + 1):
        nuevo_renglon = [1] * (renglon + 1)
        for k in range(1, renglon):
            nuevo_renglon[k] = A[renglon - 1][k - 1] + A[renglon - 1][k] 
        A.append(nuevo_renglon)
    print(A)
    return A

# Look up a value in the triangle
def lookup(A, n, k):
    return A[n][k]

A = triangle(n)
print(f"Dynamic programming: For row {n} position {k}, the value is {lookup(A, n, k)}")