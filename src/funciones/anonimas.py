# haciendo uso de lambda crear una funcion que me muestre un mensaje personalizado
mostrar_mensaje = lambda mensaje: print(mensaje)
mostrar_mensaje("¡Hola, mundo!")

#crar una funcion para calcular el area de un rectangulo, siendo la siguiente formula: base*altura
calcular_area = lambda base, altura: base * altura
print(calcular_area(5, 3))  

# crear una funcion que verifique si un numero es par o impar
# primera forma
par_impar = lambda numero: "Par" if numero % 2 == 0 else "Impar"
print(par_impar(4))
print(par_impar(9))
print(par_impar(12))
#segunda forma
es_par= lambda numero: numero % 2 == 0
if es_par(10):
    print(" es par")
else:
    print("es impar")
