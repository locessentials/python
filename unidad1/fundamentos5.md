---
layout: default
title: Funciones
parent: 1. Cheat Sheets
nav_order: 5
---

# Cheat Sheet 5: funciones

The whole expression len(nums) is a function call: you’re calling the function len and passing it nums.

The parts:

len: the function’s name, el nombre de la función
nums: the argument, el argumento, which is the value you give the function to work on
5: the value the function gives back, its return value, el valor de retorno

def doble(x):          # DEFINE la función: le dice a Python qué hacer cuando la llamen
    return x * 2

doble(5)               # LLAMA a la función: ahora sí se ejecuta, y regresa 10

in the definition, x is a parameter (parámetro), the name the function uses for whatever it receives
in the call, 5 is the argument (argumento), the actual value you pass in