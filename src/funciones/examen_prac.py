## 1. Funciones Básicas Crea una función llamada calcular_area_rectangulo que reciba la base y la altura de un rectángulo (números enteros o flotantes) y retorne su área calculada. Pruébala llamándola con dos valores distintos e imprime el resultado. 
def calcular_area_rectangulo(base: float, altura: float) -> float:
    return base * altura
area1 = calcular_area_rectangulo(5, 3)
area2 = calcular_area_rectangulo(10.5, 4.2)
print(f"Área del rectángulo 1: {area1}")
print(f"Área del rectángulo 2: {area2}")

## 2. Parámetros Nominales y por Defecto Crea una función llamada calcular_precio_final que calcule el precio de un producto aplicando un impuesto y un descuento opcional. ● Parámetros por defecto: impuesto = 0.18 (18%) y descuento = 0.0. ● Utiliza argumentos nominales en su llamada para aplicar solo un descuento del 0.05 (5%) manteniendo el impuesto por defecto. 
def calcular_precio_final(precio: float, impuesto: float = 0.18, descuento: float = 0.0) -> float:
    precio_con_impuesto = precio * (1 + impuesto)
    precio_final = precio_con_impuesto * (1 - descuento)
    return precio_final 
precio_final = calcular_precio_final(precio=100, descuento=0.05)
print(f"Precio final: {precio_final}")

## 3. Type-hints (Anotaciones de tipo) Diseña una función llamada obtener_promedio que reciba una lista de números enteros (list[int]) y retorne un número flotante (float) que represente el promedio de los valores. Incluye las anotaciones de tipo estrictas vistas en el apunte.
def obtener_promedio(n: list[int]) -> float:
    if not n:
        return 0.0
    return sum(n) / len(n)
print(obtener_promedio([5, 8, 15, 43, 99]))

## 4. Empaquetado Posicional (*args) Crea una función llamada unir_frases(*args) que reciba una cantidad variable de cadenas de texto (str) y las una en una sola oración separadas por un espacio, retornando el resultado final. 
def unir_frases(*args: str) -> str:
    return ' '.join(args)
print(unir_frases("Hola", "me", "llamo", "terreneitor"))

## 5. Empaquetado Nominal (**kwargs) Diseña una función llamada generar_perfil_usuario(**kwargs) que reciba datos arbitrarios en formato clave-valor (como nombre, edad, país, profesión) y devuelva una cadena de texto descriptiva que recorra el diccionario armado e imprima cada característica del usuario. 
def generar_perfil_usuario(**kwargs) -> str:
    perfil = []
    for clave, valor in kwargs.items():
        perfil.append(f"{clave}: {valor}")
    return ', '.join(perfil)
print(generar_perfil_usuario(usuario="Alice", edad=30, país="Estados Unidos", profesión="Ingeniera"))

## 6. Funciones Anónimas (lambda) Crea una función anónima (lambda) asignada a una variable llamada es_par que reciba un número entero y devuelva True si es par y False en caso contrario. Pruébala pasando un número par y uno impar. 
def es_par(numero: int) -> bool:
    return (lambda x: x % 2 == 0)(numero)
print(es_par(4)) 
print(es_par(5)) 

## 7. Documentación (docstring) Crea una función llamada calcular_potencia(base: float, exponente: float) -> float que eleve un número a su potencia. Añade un docstring completo que cumpla estrictamente con la advertencia del apunte: 1. Breve explicación. 2. Especificación y tipos de los parámetros. 3. Restricciones (ej. el exponente no debe ser negativo). 4. Características del valor que retorna. 
def calcular_potencia(base: float, exponente: float) -> float:
    """
    Calcula la potencia de un número.
    Args:
        base (float): La base que se elevará a la potencia.
        exponente (float): El exponente al que se elevará la base. Debe ser un número no negativo.
    Restricciones:
        - El exponente no debe ser negativo.
    Returns:
        float: El resultado de elevar la base al exponente.
    """
    if exponente < 0:
        raise ValueError(f"El exponente no debe ser negativo.")
    return base ** exponente
print(calcular_potencia(2, 3))

## 9. Programación Funcional (map()) Dada una lista de precios en dólares: precios: list[float] = [10.5, 20.0, 50.0, 5.99], utiliza la función integrada map() combinada con una función lambda para incrementar todos los precios en un 10% (multiplicarlos por 1.10). Recuerda envolver el resultado en list() para visualizarlo. 
precios: list[float] = [10.5, 20.0, 50.0, 5.99]
precios_incrementados: list[float] = list(map(lambda precio: precio * 1.10, precios))
print(precios_incrementados)

## 10. Programación Funcional (filter()) Dada una lista de palabras: palabras: list[str] = ["sol", "computadora", "luz", "programacion", "ia", "python"], utiliza la función integrada filter() y una función lambda para filtrar y quedarte únicamente con aquellas palabras que tengan más de 4 caracteres. Muestra el resultado convertido en lista. 
palabras: list[str] = ["sol", "computadora", "luz", "programacion", "ia", "python"]
palabras_filtradas: list[str] = list(filter(lambda palabra: len(palabra) > 4, palabras))
print(palabras_filtradas)