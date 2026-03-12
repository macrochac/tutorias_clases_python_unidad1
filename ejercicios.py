"""
edad = int(input("Ingrese su edad: "))
for i in range(1, edad + 1):
    print(i)


numero = int(input("Ingrese un numero: "))
for i in range(1, numero + 1):
    impar = i % 2
    if(impar==1):
       print(i,end=',') 

numero = int(input("Ingrese un numero: "))
for i in range(numero, -1, -1):
    print(i,end=',')
"""
palabra = input("Ingrese una palabra: ")
invertida = ""
for letra in palabra:
    invertida = letra + invertida
for letra in invertida:
    print(letra)
