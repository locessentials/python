# Triángulo de Pascal

# n = renglón
# k = posición en el renglón

def pascal(n, k):
    if k == 0 or n == k:
        return 1                                # pone los 1 en los dos lados (relativamente) verticales del triángulo
    return pascal(n-1, k-1) + pascal(n-1, k)    # pascal(n-1, k-1) = number up and to the left: one row up, one position left
                                                # pascal(n-1, k) = number up and to the right: one row up, same position
# calcular hasta el cuatro, finding 5, 2

print(pascal(5, 2))

# 5 points for finishing the lambda

# pascal = lambda n, k : 


# 5 puntos for the programacion dinamica de esto