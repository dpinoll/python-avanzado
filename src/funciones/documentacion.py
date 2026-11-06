# en la siguiente funcion deberan escribir la documentacion segun la convencion para el docstring de funciones 
def area_rectangulo(b,h):
    """
        Calcula el área de un rectángulo.
        args:
            b (int/float): La base del rectángulo.
            h (int/float): La altura del rectángulo.
        restricciones:
            los argumentos no podran ser igual o menores a cero.
        Returns:
            int/float: El área del rectángulo, que es el resultado de la multiplicacion de la base por la altura, que es el área del rectángulo.
    """
    return b*h

# funcion para hallar la potencia de un numero
def potencia(n:int, p:int)->int:
    """
        Calcula la potencia de un número.
        args:
            n (int): La base del número.
            p (int): El exponente al que se elevará la base.
        Returns:
            int: El resultado de elevar la base al exponente.
    """
    resultado:int=1
    for _ in range(p):
        resultado *= n
    return resultado    