factorial = lambda n: 1 if n <= 1 else n * factorial(n - 1)

print(factorial(0))   # 1
print(factorial(1))   # 1
print(factorial(4))   # 24
print(factorial(5))   # 120
print(factorial(10))