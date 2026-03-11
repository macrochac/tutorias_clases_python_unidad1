"""
frutas=["Bananas","Fresa","Manzana"]
for x in range(len(frutas)):
    print(frutas[x])

frutas=["Bananas","Fresa","Manzana"]

for item in frutas:
    print(item)

palabra = input("Escriba una palabra: ")
for x in range(10):
    print(palabra)

frase = input("Escriba una frase: ")
letra = input("escriba la letra a buscar en la frase: ")
contador = 0
for x in frase:
   if(x==letra):
      contador += 1
print("la letra",letra,"aparece",contador,"veces en la frase",frase)
"""
frase = input("Escriba una frase: ")
contador = 0
for x in frase:
   if x.isupper():
      contador += 1
print("hay ",contador,"letras mayusculas en la frase",frase)