# funciones en python
las funciones nos permiten ordenar mejor el codigo y reutilizarlo cuando sea necesario.
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
  En el caso que queramos indicar un determinado parametro puede ser de un `tipo o de otro` tenemos que especificarlo el operador `|`
  - tuple/dict -> puede ser de tipo tupla o diccionario
  - list[str|int] -> lista cuyos elementos pueden ser cadena de texto o enteros 
  - dict[str|int,float|int] ->
## closure
una closure o `clausura` sin funciones que establecen una funcion interior, o retornan una funcion, estas funciones se caracterisan por recrear el valor de los argumentos que se le pasa.
```python
def multiplicacion(n):
    def multiplicacion(m):
        return n*m
    return multiplicacion
```
## programacion funcional 
python es un leguaje de programacion multiparadigma, y uno de sus paradigmas que mejor funcion tienen es la `funcional`.
python usa tres`map()`,`filter()`,`reduce()`,pero nosotros solo usamos `map(),filter()`.
estas funciones integradas de python sirven para procesar y transformar colecciones de datos(listas,diccionarios) de manera muy eficiente y segunda el iterable en que va acutuar. la funcion que recibe como parametro puede ser normal `def` o puede ser anonima `lambda`. 

> [!tip]importante:
> las funciones `map()` y `filter()` reciben dos parametros primero la funcion a ejecutar 
### 1. map()
map aplica una funcion especifica a cada uno de los elementos de una coleccion y devuelve un nuevo iterable con los resultados
```python
# de una lista de numeros deseamos calcular la potencia de cada numero 
numeros:list[int]=[2,4,6,8,7]
## cuando deseamos trabajar con una funcion anonima tenemos que declarar primero la funcion antes de pasarla por parametro
def f(x):
    return x**2
## una vez creada pasamos la funcion como parametro
map(f, numeros)
## cuando deseamos trabajar con funcion anonimas usamos lambda dentro del parametro
map(lambda x:x**2, numeros)
```
### 2. filter()
filter pasa cada elemento de una coleccion por una funcion y solo se queda con aquellos elementos donde la funcion devuelva true (es decir filtra los datos segun una condicion).
```python
# imagina que tienes una lista de numeros y solo quieres quedarte con los numeros pares
numeros:list[int]=[2,7,8,20,4,3,9,12,11,16,17]
filter(lambda n:n % 2 ==0, numeros)
```
> [!WARNING]Nota importante
> tanto `map()` coomo `filter()` no devuleven listas directamente, sino iteradores. esto es para ahorrar memoria(evaluacion perezosa o lazy evaluacion). si quieres ver el resultado como una lista tradicional, siempre debes envolver en `list()`.

## comprension de lista
1. Comprensión de Listas (List Comprehensions)
La comprensión de listas te permite crear una lista nueva aplicando una operación o un filtro a los elementos de otra secuencia, de forma mucho más corta que usando un ciclo for tradicional.

Estructura básica:
Python
nueva_lista = [expresion for elemento in iterable if condicion]
expresion: Lo que quieres hacer con cada elemento (ej. multiplicarlo por 2).

for elemento in iterable: El ciclo que recorre los elementos.

if condicion (opcional): Un filtro para incluir solo los elementos que cumplan una regla.

Ejemplo práctico:
Imagina que quieres obtener los cuadrados de los números del 0 al 4:

```Python
# Forma tradicional con un ciclo for
cuadrados = []
for x in range(5):
    cuadrados.append(x ** 2)

# Forma elegante con comprensión de listas
cuadrados = [x ** 2 for x in range(5)]
print(cuadrados)  # Salida: [0, 1, 4, 9, 16]
Ejemplo con filtro (if): solo los números pares del 0 al 9.
```
```Python
pares = [x for x in range(10) if x % 2 == 0]
print(pares)  # Salida: [0, 2, 4, 6, 8]}
```
## diccionarios por comprension
2. Comprensión de Diccionarios (Dictionary Comprehensions)
Funcionan exactamente igual que las listas, pero están diseñadas para crear diccionarios. Por eso, en lugar de una sola expresión, debes definir la clave y el valor separados por dos puntos (:).

Estructura básica:
```Python
nuevo_diccionario = {clave: valor for elemento in iterable if condicion}
Ejemplo práctico:
Crear un diccionario donde las claves sean números del 1 al 4 y los valores sean esos números al cubo:
```
```Python
cubos = {x: x ** 3 for x in range(1, 5)}
print(cubos)  # Salida: {1: 1, 2: 8, 3: 27, 4: 64}
También puedes transformar diccionarios existentes, por ejemplo, convirtiendo las calificaciones de un diccionario a mayúsculas o invirtiendo claves y valores:
```
```Python
precios = {"manzana": 2, "pera": 3, "uva": 5}
# Duplicar los precios
precios_inflados = {k: v * 2 for k, v in precios.items()}
print(precios_inflados)  # Salida: {'manzana': 4, 'pera': 6, 'uva': 10}
```