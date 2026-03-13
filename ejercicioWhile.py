"""
i=0
while(i < 6):
    print(i)
    i+=1

num = int(input("Digite un numero: "))
i=1
while (i<=10):
    print(num * i)
    i+=1

# digitar notas hasta qsea -1    

notas=0
i=0
while(True):
    nota = int(input("Digite una nota entre (0-5): "))
    if (nota==-1):
        promedio = notas / i
        print(promedio)
        break
    else:
        notas = notas + nota
        i += 1

# invertir un numero con ciclo while

num = int(input("Ingrese un número a invertir: "))
invertido = 0

# Bucle while para invertir el número
while num > 0:
    digito = num % 10  # Obtiene el último dígito
    invertido = (invertido * 10) + digito  # Construye el número invertido
    num = num // 10  # Elimina el último dígito del número original

print("Número invertido:", invertido)
"""
mayor=0
while(True):
    numero = int(input("Digite un numero: "))
    if (numero==-1):
        print(mayor)
        break
    if numero>mayor:
        mayor=numero
        