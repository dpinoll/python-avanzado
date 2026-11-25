# MODULARIDAD

La `modularidad` consiste en dividir un programa grande en archivos pequeños y reutilizables llamados `modulos` cada modulo es simplemente un archivo `.py`

**VENTAJAS**

- `Reutilizacion:` escribes el codigo una vez y lo usas en muchos programas.
- `Organizacion:` cada archivo tiene una responsabilidad clara.
- `Mantenimiento:` es mas facil encontrar y corregir errores.
- `Trabajo en equipo:` cada persona puede desarrollar su propoio modulo.

## 1. CREAR UN MODULO

Basta con crear un archivo con la extencion `.py` por ejemplo `matematicas.py`.

## 2. IMPORTAR UN MODULO COMPLETO

La manera de como reutilizamos es haciendo uso de la palabra reservada `import` esto se debe declarar en el archivo donde reutilzaremos ciertas funciones o variables de un modulo .
Para importar un modulo completo usamos `import nombre_archivo`.

### EJEMPLOS

1. `matematicas.py`

```python
def suma (a,b):
    return a+b
def resta(a,b):
    return a-b
```

2. `main.py`

```python
import matematicas 

## Para hacer uso de una de las funciones tengo que acceder al archivo luego un punto y el nommbre de dato,funcion que deseamos utilizar

matematicas.resta(5,8)
```
## 3. Importar solo lo nesesario(from....import)
a veces es nesesario importar solo una parte del modulo, esto se usa cuando deseamos utilizar partes especificas de un modulo. para esto usamos `from nombre_modulo import parte_especifica`
`Matematica.py`
```python
def resta(a,b):
    return a-b
def suma (a,b)
    return a+b
PI=3.1415
```
`main.pi`

```python
from matematicas import PI
```
## PAQUETES (carpeta de modulos)
cuando el proyecto empieza a crecer los modulos se ordenan en carpetas