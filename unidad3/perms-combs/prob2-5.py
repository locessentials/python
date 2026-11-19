def tr(i, j, I):
    t = I.copy()
    t[i] = j
    t[j] = i
    return t

def trl(b):
    a = b.copy()
    l = []
    i = 0
    while True:
        if a[i] > a[i+1]:
            a[i], a[i+1] = a[i+1], a[i]
            I = ident(len(a))
            l.append(tr(i, i+1, I))
            i = 0
            continue
        i += 1
        if i == (len(a) - 1):
            break
    return l

ident = lambda n: list(range(n))

b = [3, 0, 2, 1]
h = trl(b)
print(h)

