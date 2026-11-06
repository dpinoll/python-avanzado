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
## Conociendo mas sobre funciones parametros y argumentos
sobre los parametros / argumentos nominales es ampliamente usado para distintaas configuraciones ya que se puede pasar solo loss argumentos que se usaran y dejar los parametros por defecto sino se van a modificar.
```python
# tenenmos un programa que me permite acceder a internet que tiene parametros por defecto, sin embargo si se actualiza uno de los accesos se podran modificar o actualizar el valor.
##primer caso accesos por defecto 
def config(user="admin",pass="1234",port="8080",bssid="wifi"):
    return"conectado a la red"
config()
## segundo caso 1 bssid cambio por el de "laboratorio"
def config(user="admin",pass="1234",port="8080",bssid="wifi"):
    return"conectado a la red"
config(bssid="laboratorio1")
## reyner desea conectarse al wifi de ana luz, pregunta como se llama tu wifi y cual es su contraseña. respuesta el wifi es a56 y su contraseña es 12345678
def config(user="admin",pass="1234",port="8080",bssid="wifi"):
    return"conectado a la red"
config(bssid="A56",pass="12345678")
```
## conociendo *args y **kargs (empaquetado y desempaquetado de argumentos posicionales)
### desempaquetando argumentos posicionales
esta tecnica nos permite empaquetar nuestros argumentos cuando no sabemos la cantidad de datos que vamos a pasar, imaginemos que nos piden una funcion para sumar n catidad de numeros la solucion seria empaquetar los argumentos y luego desenpaquetarlos para ello en la definicion de la funcion dentro de los parametros debemos usar el operador `*`delante del nombre del parametro posicional esto hara que todos los argumentos se almacenen en una tupla`()`(lista`[]`)esto nos permite recorrer dentro de sus elementos para poder desempaquetarlos y realizar las operaciones necesarias.
```python
# deseamos crear una funcion que nos permita sumar n cantidad de numeros 
# es un numero variable puede ser 3,7,8 ........n
def suma(*args):
    #*args = (2,5,7,8,9)
    acumulado=0
    for i in args:
        acumulado += 1
    return acumulado
print(suma(2,5,7,8,9))
```
#### desempaquetando argumentos nominales
en este caso como en el anterior utilizaremos el operador `*`la es el msimo sin embargo para desempaquetar argumentos nominales usaremos `**`delante del nombre del paramentro nominal diferencia del anterior esto se empaqueta en un diccionario (`{clave:valor}`)
```python
# debemos crear una funcion que me permita saber encontrar la persona con mayor calificacion.
def mejor_alumno(**kwargs):
    #**kwargs={'noemi':20,'eduardo':18,'david':19}
    nota_maxima=-1
    for alumno,nota in kwargs.items():
        if nota > nota_maxima:
            nota_maxima = nota
            mejor_alumno = alumno
    return mejor_alumno
mejor_alumno(noemi=20,eduardo=18,david=19)
```
## funciones anonimas
las funciones anonimas en python son llamadas `lambda`,estas funciones yienen las siguientes propiedades:
1. se escribe en una unica sentencia `(linea)`
2. no tiene nombre `(anonima)`.
3. su cuerpo conlleva un `return` implicito.
4. puede recibir cualquier numero de parametros.

la estrucutra para definir una funcion `lambda` es la siguiente:
1. escribir la palabra reservada `lambda` 
2. especificar la cantidad de parametros.
3. indicar los datos de retorno
```python
lambda a,b: a+b
```

> [!TIP]puesto que esta funcion de anonima para ejecutarla debemos almacenar la funcion en una variable 

```python
suma=lambda a,b: a+b
suma(3,6)
```
## documentacion 
python  nos permite documentar la funcion con el objetivo de explicar mejor determniadas zonas de nuestro codigo, para ello usamos una cadena de texto dspues de ka definicion de una funcion, a esta cadena de texto se le conoce como `docstring` y esta delimitado por triples `""" aqui el texto """`
```python
def suma(a,b):
    """
    funcion para realizar la suma de dos numeros 
    """
## los docstring tambien nos permite explicar los parametros que recibe y  los datos de salido
def resta(a,b):
    """
    a= a un numero entero
    b=a un numero entero
    en ambos casos a,b no deben recibir valores menores a 0.
    retornara un dato entero (int) positivo
    """
    return a-b
```
[!WARNING] en el proceso de documentacion tener en cuenta de incluir a lo menos lo siguiente: 
> 1. breve explicacion sobre que hace la funcion 
> 2. especificaciones y  caracterosticas de los parametros incluyendo sus tipos. 
> 3. restricciones de la funcion. 
> 4. el valor que retorna y sus caracteristicas 

## type-hints (anotaciones de tipo)
Nos permite indicar que tipo de datos recibira una variable, parametros y el valor que retorna de una funcion.
Para utilizarlos debemos indicar el tipo de dato despues del separador`:` en el caso del valor de retorno usaremos `->` luego el tipo de dato y finalmente el separador `:` que indica el inicio del bloque de codigo de la funcion.
Las anotaciones de tipo son una herramienta que nos permite complementar la documentacion de nuestro codigo
**tenemos lo siguiente**
- **Simple**
  - int -> numeros enteros
  - float -> numeros decimales 
  - bool -> datos boleanos(verdad o falso)
  - str -> datos de tipo texto o cadena
  - list -> listas `[]`
  - tuple -> tuplas `()`
  - dict -> diccionarios `{}`
- **compuestos**
  existen casos en los que nesecitamos mas expresividad en la
  *anotacion de tipos* ¿que ocurre si queremos indicar una *lista de cadenas* o un *conjunto de enteros*.?
  - list[str] -> lista de cadenas de texto
  - list[int] -> lista de numeros enteros
  - dict[str,float] -> diccionario donde las claves son cadenas de texto y los valores son flotantes*decimales
- **Multiles**
  