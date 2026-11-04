---
layout: default
title: Clases y objetos
parent: 1. Cheat Sheets
nav_order: 7
---

# Cheat Sheet 7: clases y objetos

La **programación orientada a objetos (POO)** es un paradigma que organiza el código en torno a "objetos". Un objeto agrupa dos cosas: **datos** (variables) y **comportamiento** (funciones). 

Una **clase** es el molde o la plantilla que define cómo serán esos objetos. Un **objeto** (o instancia) es el elemento real creado a partir de ese molde. 

## Crear una clase y un objeto

Para definir una clase se usa la palabra reservada `class`. El método `__init__` (con doble guion bajo) es el **constructor**: la función que se ejecuta automáticamente cuando se crea un objeto nuevo.

```python
class Gato:
    def __init__(self, nombre, edad):
        self.nombre = nombre    # atributo (dato)
        self.edad = edad        # atributo (dato)

    def maullar(self):           # método (comportamiento)
        print(f"{self.nombre} dice: ¡Miau!")

# Crear objetos (instanciar la clase)
mi_gato = Gato("Oliver", 13)
tu_gato = Gato("Rex", 5)
```

**Nota sobre los guiones bajos dobles:** El método `__init__` lleva dos guiones bajos al inicio y al final (conocidos en inglés como *dunder*, por *double underscore*). En Python, esta convención se usa para identificar **métodos y variables especiales** que el lenguaje crea o utiliza automáticamente. No son simples guiones bajos, son exactamente dos en cada lado.

**Convención de nombres:** Por convención (PEP 8), los nombres de las clases se escriben en `CapWords` (la primera letra de cada palabra en mayúscula, sin guiones bajos), mientras que las variables y funciones se escriben en `snake_case` (todo en minúsculas, separado por guiones bajos). Por ejemplo: la clase `GrafoDirigido` crea el objeto `mi_grafo`.

## La palabra `self`

`self` es la referencia al **objeto actual**. Es el primer parámetro de todos los métodos de la clase, y se usa para acceder a los atributos y métodos de ese objeto específico. 

No se pasa como argumento al crear el objeto; Python lo hace automáticamente. En el fragmento anterior, `self` aparece en la definición del método `maullar`, donde `self.nombre` permite que el código lea el atributo del objeto correspondiente.

Cuando se invoca un método sobre un objeto, Python pasa ese objeto implícitamente como el primer argumento (`self`). Por lo tanto, la instrucción `mi_gato.maullar()` es equivalente internamente a `Gato.maullar(mi_gato)`.

```python
# Python pasa 'mi_gato' como el 'self' del método
mi_gato.maullar()               # Imprime: Oliver dice: ¡Miau!
tu_gato.maullar()               # Imprime: Michi dice: ¡Miau!
```

*Nota: aunque ambos gatos usan la misma definición de `maullar`, la referencia `self.nombre` se resuelve con los datos del objeto específico que ejecuta la llamada.*

## Acceder a atributos y métodos

Se usa el **operador punto** (`.`) para acceder a los elementos de un objeto.

```python
mi_gato.nombre                 # "Oliver"
mi_gato.edad = 14              # modificar un atributo
mi_gato.maullar()               # llamar a un método
```

## Diferencias con variables normales

```python
a = 10                          # variable normal (entero)
b = [1, 2, 3]                   # variable normal (lista)

p = Perro("Max", 2)             # objeto: agrupa variables y funciones
```

---

![Logo de Python en amarillo y rojo]({{ '/imagenes/python-logo.png' | relative_url }}){: .tip-circle }

A diferencia de las listas o los diccionarios (que ya traen métodos incorporados), las clases te permiten crear tus propios tipos de datos con sus propios métodos. Si quieres saber cómo guardar tus clases en archivos separados para reutilizarlas, revisa **Cheat Sheet 8: módulos e importaciones**.

<span class="clear"></span>

---

## Temas avanzados

Esta página cubre únicamente los fundamentos sintácticos de la programación orientada a objetos en Python. Para implementar estructuras de datos complejas o resolver problemas algorítmicos, es necesario profundizar en los siguientes conceptos:

- **Clases que contienen colecciones:** cómo definir atributos que son listas o diccionarios dentro de una clase
- **Almacenamiento de objetos:** cómo añadir objetos como valores o llaves dentro de diccionarios y listas
- **Clases frente a diccionarios:** diferencias estructurales entre usar una clase para garantizar atributos y métodos consistentes, frente a usar un diccionario como contenedor de datos
- **Composición de clases:** cómo una clase puede contener instancias de otras clases (por ejemplo, un grafo que contiene objetos de tipo nodo, los cuales a su vez contienen objetos de tipo arista).