#Leer la edad de x cantidad de personas
# y decir si es mayor o menor de edad
from faulthandler import cancel_dump_traceback_later


edades = []
"""cant=0
print("Cuantas edades?: ")
cant = int(input())
"""
cant = int(input("Cuantas edades?: "))
for i in range(cant):
    edad = int(input("Dime tu edad: "))
    edades.append(edad)

"""for i in range(cant):
    edad = edades[i]
    if edad >= 18:
        print("Edad: ", edad, ", es mayor de edad.")
    else:
        print("Edad: ", edad, ", es menor de edad.")
"""
for edad in edades:
    if edad >= 18:
        print("Edad: ", edad, ", es mayor de edad.")
    else:
        print("Edad: ", edad, ", es menor de edad.")

print("Tercera posicion ", edades[2])