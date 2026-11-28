# Fibonacci: fórmula cerrada de teoría de números (sin PD)

import math

fi = (1 + math.sqrt(5)) / 2
fi_c = (1 - math.sqrt(5)) / 2

fn = lambda n: ((fi**n) - (fi_c**n)) / math.sqrt(5)

for i in range(50):
  print(f"n={i} -> {round(fn(i))}")