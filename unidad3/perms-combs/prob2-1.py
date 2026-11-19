identidad = lambda n: list (range(n))

I = identidad(5)

def tr(i, j, I):        # transposición
    t = I.copy()        
    t[i] = j
    t[j] = i
    return t

print(tr(1,3,I))
