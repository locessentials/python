def insm(lst, x):
    # lst is a single list (one permutation)
    # x is the element to insert
    # This should return a list of lists, where x is inserted into every position
    
    result = []
    for i in range(len(lst) + 1): # +1 to include the position at the very end
        # Create a copy of the list, insert x at index i
        new_perm = lst[:i] + [x] + lst[i:] 
        result.append(new_perm)
        
    return result

def per(l):
    if l == []:
        return [[]]
    s = []
    for t in per(l[1:]):
        s = s + insm(t, l[0])
    return s

#Valores:
l = [1, 2, 3]
resultado = per(l)
print(resultado)
