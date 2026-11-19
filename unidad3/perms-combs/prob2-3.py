# Compose

a = [2, 3, 0, 1]
b = [3, 2, 0, 1]

compose = lambda a,b: [b[a[i]] for i in range(len(a))]

print(compose(a, b))

# Compose - long form

def compose(a, b):
    result = []
    for position in range(len(a)):
        where_a_sends_it = a[position]
        where_b_sends_that = b[where_a_sends_it]
        result.append(where_b_sends_that)
    return result

# Identidad

identidad = lambda n: list (range(n))

print(identidad(5))

