#Concatenación de cadenas
print("Concatenación de cadenas")
cadena1 = "Hola"
cadena2 = "Mundo"

cadena3= cadena1 + " " + cadena2

print(cadena3)

print("")

# Imprimir caracteres de una posición
print("Imprimir caracter de una posición")
#Hola mundo
elemento=3
print(cadena3[elemento-1])

print("Imprimir caracteres de una posición")
elementoFinal= 6

for i in range (elemento-1,elementoFinal):
    print(cadena3[i-1], end="")
    i+=1
print("")

print("")

#Encontrar el número de letras
print("Encontrar el número de letras")
letra = "a"
print(cadena3.count(letra))
print("")

#InsertarCadena
print("InsertarCadena")
cadena4 = "Hola Mundo"
cadena5="Insertada"
posicion= 3

for i in range (1,posicion+1):
    print(cadena4[i-1], end="")
    i+=1

print(cadena5, end="")

for i in range (3,len(cadena4)+1):
    print(cadena4[i-1], end="")
    i+=1

print("")

print("")

#Cambiar elementos de una cadena
print("Cambiar elementos de una cadena")
print(cadena3)
print(cadena3.replace("o", ","))

print("")

#Eliminar elementos de una cadena
print("Eliminar elementos de una cadena")
print(cadena3)
print(cadena3.replace("o", ""))

print("")

#Numero ascii de un caracter
print("Numero ascii de un caracter")
print(ord("ñ"))