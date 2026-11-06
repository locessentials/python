# Problema 1: contar

# n = número de listas
# listas = lista con n listas

n = int(input())
listas = [input().split() for _ in range(n)]

# calcula el número de permutaciones posibles a mano

# m = número de elementos en una lista

def factorial(m):
    # devuelve m! – el número de permutaciones de una lista de m elementos
    total = 1
    for factor in range(1, m + 1):
        total *= factor
    return total

for lista in listas:
    print(factorial(len(lista)))

# usar la biblioteca math

import math

for lista in listas:
    print(math.factorial(len(lista)))

# Get-Content prob1-1.txt | python prob1-1.py