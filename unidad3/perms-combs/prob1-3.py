import itertools, math

lista = list(map(int, input().split()))

perms = list(itertools.permutations(lista))
for perm in perms:
    print(perm)

def verify(lista, perms):
    elementos = len(lista)
    expected_perms = math.factorial(elementos)
    if expected_perms == len(perms):
        return "Verified!"
    else:
        return "Unverified."

print(verify(lista, perms))