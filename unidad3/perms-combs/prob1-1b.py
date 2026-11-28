import math

n = int(input())    # número de listas
ls = []             # listas

for l in range(n):
    ln = list(map(int, input().split()))    # lista nueva
    ls.append(ln)

for i, l in enumerate(ls, start=1):
    m = len(l)

    pos = 1                                 # posibilidades
    for i in range(1, m+1):
        pos *= i                              # posibilidades
    
    auto = math.factorial(m)
    
    print(f"Length of list {m}: Manually calculated factorial: {pos}; Built-in function: {auto}")


