---
layout: default
title: Diccionarios
parent: Colecciones
grandparent: 1. Cheat Sheets
nav_order: 4
---

# Cheat Sheet 4: colecciones – diccionarios

A dictionary is a collection of keys and values. For example:

dict = {'datcat1': 'abc', 'datcat2': 'xyz', 'num': '123' }

print(dict['datcat1'])
> abc

new_points = dict['num']	# accessing an item in a dictionary
print("You just earned " + str(new_points) + " points!")

dict['x_position'] = 0		# adding a new item to a dictionary
dict['y_position'] = 25

dict = {} 			# initializing a dictionary

dict = {'num': 123}		# Changing a value in a dictionary
print("The number is " + dict['num'] + ".")
dict['num'] = 456
print("The number is now " + dict['num'] + ".")

del dict['num']			# Removing a key/value pair

favorite_languages = {		# Formatting for readability
 'jen': 'python',
 'sarah': 'c',
 'edward': 'ruby',
 'phil': 'python',
 }

for name in sorted(favorite_languages.keys()):		# Looping through a dictionary by keys
  print(name.title() + ", thank you for taking the poll.")
for lang in favorite_languages.values(): 		# Looping through a dictionary by values
for name, lang in sorted(favorite_languages.items())

favorite_languages = {'jen': 'python', 'sarah': 'tbd'}
favorite_languages.items()     # all key-value pairs → ('jen', 'python'), ('sarah', 'tbd')
favorite_languages.keys()      # just the keys → 'jen', 'sarah'
favorite_languages.values()    # just the values → 'python', 'tbd'
favorite_languages['jen']      # value for key 'jen' → 'python'; KeyError if key missing
favorite_languages.get('ed', 'none')   # value for 'ed', or 'none' if key missing
favorite_languages['ed'] = 'rust'      # add a new pair, or change an existing value
del favorite_languages['sarah']        # remove the pair with key 'sarah'
len(favorite_languages)                # number of key-value pairs

for name, lang in favorite_languages.items():   # loop over key AND value
for name in favorite_languages.keys():          # loop over keys only
for lang in favorite_languages.values():        # loop over values only
for name in sorted(favorite_languages.keys()):  # loop over keys alphabetically

## Tuplas como claves

A veces una clave necesita más de un dato. Por ejemplo, una posición en un tablero necesita una fila y una columna. Una tupla junta los dos datos en una sola clave:

```python
tablero = {(0, 0): "X", (1, 2): "O"}
tablero[(1, 2)]                 # "O"  (lo que hay en la fila 1, columna 2)
```

Una lista no puede ser clave, porque una lista puede cambiar: si una clave cambiara después de guardarla, el diccionario ya no podría encontrarla. Las tuplas no cambian, así que sí sirven como claves:

```python
{[0, 0]: "X"}                   # TypeError: unhashable type: 'list'  (Python no acepta una lista como clave)
```