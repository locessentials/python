---
layout: default
title: Módulos e importaciones
parent: 1. Cheat Sheets
nav_order: 8
---

# Cheat Sheet 8: módulos e importaciones

Un **módulo** es simplemente un archivo de Python (con extensión `.py`) que contiene código (variables, funciones o clases). 

La **importación** es el mecanismo que permite utilizar el código de un módulo dentro de otro archivo. Esta separación permite organizar proyectos grandes en archivos más pequeños y reutilizar código sin tener que copiarlo y pegarlo.

## Importar un módulo completo

Si se tiene un archivo llamado `gatos.py` que contiene una clase `Gato`, desde otro archivo en la misma carpeta se puede importar de la siguiente manera:

```
# Archivo: gatos.py
class Gato:
    def __init__(self, nombre):
        self.nombre = nombre
    
    def maullar(self):
        print(f"{self.nombre} dice: ¡Miau!")
```

```
# Archivo: main.py
import gatos

mi_gato = gatos.Gato("Oliver")  # Se usa el nombre del módulo como prefijo
mi_gato.maullar()               # Imprime: Oliver dice: ¡Miau!
```

Al usar `import gatos`, Python carga todo el archivo. Para acceder a sus elementos, se utiliza el nombre del módulo seguido de un punto (`gatos.Gato`). Esto evita conflictos si hay funciones o clases con el mismo nombre en diferentes archivos.

## Importar elementos específicos

Si solo se necesita una parte del módulo, se puede usar la palabra reservada `from` para importar elementos específicos directamente al espacio de nombres actual:

```
from gatos import Gato

mi_gato = Gato("Michi")         # Ya no se necesita el prefijo 'gatos.'
mi_gato.maullar()
```

También es posible importar múltiples elementos o renombrarlos para evitar conflictos:

```Python
from gatos import Gato, Gatito
from gatos import Gato as GatoDomestico
```

## Importar todo el contenido (no recomendado)

El operador asterisco (`*`) importa todos los nombres del módulo directamente:

```
from gatos import *
```

> **Nota:** Esta práctica no es recomendada en proyectos grandes, ya que puede sobrescribir variables o funciones sin que sea evidente de dónde provienen.

---

![Logo de Python en amarillo y rojo]({{ '/imagenes/python-logo.png' | relative_url }}){: .tip-circle }

**Módulos de la biblioteca estándar:** Python incluye una gran cantidad de módulos integrados (como `math`, `random` o `sys`). Para usarlos, no es necesario crear el archivo, simplemente se importan directamente (por ejemplo, `import math`). Se pueden consultar todos los módulos disponibles en la documentación oficial de Python.

<span class="clear"></span>

---

## Ejecutar un módulo como programa principal

Cuando Python importa un módulo, ejecuta todo el código que esté en el nivel superior (fuera de funciones o clases). Para evitar que cierto código (como pruebas o inicializaciones) se ejecute al importar el archivo, se utiliza la siguiente estructura:

```
# Archivo: gatos.py
class Gato:
    pass

if __name__ == "__main__":
    # Este bloque solo se ejecuta si se corre 'python gatos.py' directamente,
    # pero NO se ejecuta si se hace 'import gatos' desde otro archivo.
    mi_gato = Gato()
    print("Prueba local")
```

La variable especial `__name__` toma el valor `"__main__"` cuando el archivo se ejecuta directamente, y toma el nombre del módulo cuando se importa.

## Estructura de paquetes (carpetas)

Para proyectos más grandes, se pueden agrupar varios módulos dentro de una carpeta. A esto se le llama **paquete**. Para que Python reconozca una carpeta como un paquete, esta debe contener un archivo llamado `__init__.py` (puede estar vacío).

```text
mi_proyecto/
├── main.py
└── animales/
    ├── __init__.py
    └── gatos.py
```

Con esta estructura, la importación se realiza de la siguiente forma:

```
from animales import gatos
# o también:
from animales.gatos import Gato
```