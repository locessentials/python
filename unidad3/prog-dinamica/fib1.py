# Fibonacci: recursión memoizada

t = [-1] * 100 # tabla de fibonacci
t[0], t[1] = 0, 1

def fib(n):
    if t[n] >= 0:
        return t[n]          # ← cache hit: skip the work
    t[n] = fib(n - 1) + fib(n - 2)   # ← compute once, store it
    return t[n]

print(fib(1))
print(fib(2))
print(fib(3))
print(fib(4))
print(fib(5))