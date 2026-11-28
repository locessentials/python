# Fibonacci: tabulación

def fib(n):
  a, b = 0, 1
  for _ in range(n):
    a, b = b, a + b
  return a


for i in range(50):
  print(f"n={i} -> {fib(i)}")