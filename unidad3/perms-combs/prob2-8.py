import numpy as np

def det(A):
    n = A.shape[0]
    l = list(range(n))
    s = per(l)
    d = 0           
    for t in s:
        sign = sgn(t)
        product = 1
        for i in range(n):
            product = product * A[i, t[i]]
        d = d + (sign * product)
    return d

def sgn(b):         
    a = b.copy()    
    c = 0           
    i = 0           
    while True:
        if a[i] > a[i+1]:
            a[i], a[i+1] = a[i+1], a[i]
            c += 1
            i = 0
            continue
        i = i + 1
        if i >= (len(a) - 1): 
            break
    return (-1)**(c%2)

def insm(lst, x):
    result = []
    for i in range(len(lst) + 1): 
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

# --- TESTING AREA ---
if __name__ == "__main__":
    A = np.array([[1, 2], 
                  [3, 8]])
                  
    result = det(A)
    print("The determinant is:", result)

    # --- TESTING AREA ---
if __name__ == "__main__":
    # 1. Create your own 3x3 matrix
    A = np.array([[2, -3,  1], 
                  [2,  0, -1], 
                  [1,  4,  5]])
                  
    # 2. Calculate the determinant using your manual function
    manual_result = det(A)
    print("Manual determinant:", manual_result)

    # 3. Calculate it using NumPy's built-in linear algebra module
    numpy_result = np.linalg.det(A)
    print("NumPy determinant:", numpy_result)