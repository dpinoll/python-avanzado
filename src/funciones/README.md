# funciones en python
las funciones no permiten ordenar mejor el codigo y reutilizarlo cuando sea necesario.
```python
# ejemplo deseamos crear un programa en python que nos permite sumar dos numeros
numero_uno:int=45
numero_dos:int=70
numero_tres:int=78
numero_cuatro:int=20
suma:int=numero_uno+numero_dos
suma_dos:int=numero_tres+numero_cuatro
print(suma)
print(suma_dos)
```
como hacemos reutilizable del ejercicio anterior y mas lejible.
para eso utilizaremos funciones.
la caracteristica de una funcion en python es la siguiente:

1. debe comenzar con la palabra reservada `def`
2. debe tener un nombre que de a entender que realizara la funcion.
3. debera tener parametros y estos estaran enserrados en parentesis `()`. no todas las funciones resibiran.
4. las funciones deberan retornar datos a travez de la ´palabra recervada `return`.
   
 ```python
# crear un programa que me permita sumar dos numeros
def sumar(a,b):
    return a+b
print(sumar(78,56))
print(sumar(45,5))
 ```
 ## funciones avanzadas
 existes tres grandes conseptod para poder entender el uso abanzado de laqs funciones:
 1. argumentos, parametrosposicionales y nominales, *args y +kargs.
 2. anotaciones en la salida de una funcion.
 3. recurcividad.
```python
# anotaciones en una funcion
def suma(a:int,b:float)->int:
    return a+b
# crear solo las notaciones de una funcion que reciba 4 numeros enteros y como salida que me muestre los 4 numeros enteros en una lizta.
def numeros_listas(a:int,b:int,c:int,d:int,)->list[int]:
    return [a,b,c,d]
```
**argumentos parametros**
- **parametros** - son las variables que se declaran en la definicion de la funcion 
- **argumentos** - es el dato concreto enviado en el llamada de la funcion 
**nota** en ambos casos tenemos los posicionales/nominales 
```python
# parametro
def suma (a.b): # en este caso tenemos una funcion suma que recibe dos parametros: a,b
suma(34,45) # en este caso estoy llamando a la funcion pasandole como argumento los datos 
# en este caso inconcreto podemos decir que estamos frente a una funcion que tiene parametros posicionales eso significa que cada valor reemplazara en el orden que le pasemos a las variables. 34->a , 45->b

def login(usuario="",pasword=""):
    return "acceso correcto"
login(password="12345678",usuario="tupapi")
# esta funcion es una funcion nominal por que para pasar los valores tengo que indicar la variablea la que se le va asociar en el parametro de la funcion.
``` 