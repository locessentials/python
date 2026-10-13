---
layout: default
title: Tipos de datos y variables
parent: 1. Cheat Sheets
nav_order: 1
---

# Cheat Sheet 1: tipos de datos y variables

y = 5         # int (whole number)  
z = 5.0       # float, because the decimal point makes it one  

  total += total = total +  

- `float("inf")`: infinito positivo; cualquier número real es menor que él  
- `float("-inf")`: infinito negativo; cualquier número real es mayor que él  

## f-strings

```python
print(f"{lo:.9f}")
```

`f"..."` lets you put a variable inside { } and Python replaces it with its value.

In the example, the `:.9f` tells Python to print the variable to 9 decimal places and to show it as regular decimal number (instead of in scientific notation, for example)