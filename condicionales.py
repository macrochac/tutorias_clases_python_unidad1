# Escribir un programa que pregunte la edad y muestre por pantalla si es mayor de edad o no.

# ESTRUCTURACION DE DESARROLLO DE SOFTWARE

# necesidad: saber si el numero que ingresa el usuario corresponde a la mayoria de edad (mayoria)
# verficacion de la edad (entrada) vs mayoria de edad
# variable  de mayoria de edad, variable dato introducido por usuario

"""
numero = int(input("Ingrese su edad en numero: "))
mayoria = 18

if numero>=mayoria:
    print("Mayor de edad")
else:
    print("Menor de edad")


puntuacion = float(input("Ingrese la puntuacion del usuario (0.0, 0.4, 0.6 o Mayor): "))
dinero = 2400
if puntuacion == 0.0:
    print("Su nivel de rendimiento es Inaceptable")
    dinero *= puntuacion
    print("El dinero recibido por su nivel de puntuacion es: ",dinero)
elif puntuacion == 0.4:
    print("Su nivel de rendimiento es Aceptable")
    dinero *= puntuacion
    print("El dinero recibido por su nivel de puntuacion es: ",dinero)
elif puntuacion < 0.6:
    print("El nivel de rendimiento digitado es incorrecto")  
elif puntuacion >= 0.6:
    print("Su nivel de rendimiento es Meritorio")
    dinero *= puntuacion
    print("El dinero recibido por su nivel de puntuacion es: ",dinero)
"""
edad = int(input("Ingrese su edad en numeros: "))

if edad<4:
    print("Tiene",edad,"Años por lo tanto es GRATIS")
elif edad >= 4 and edad < 18:    
     print("Tiene",edad,"Años por lo tanto es debe pagar 5 Euros")
elif edad >= 18:    
     print("Tiene",edad,"Años por lo tanto es debe pagar 10 Euros")
