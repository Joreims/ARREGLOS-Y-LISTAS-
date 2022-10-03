#Calcular la media de las estaturas de una clase.
#Deducir cuantos son mas altos que la media y mas bajos

alumnos = []

n = int(input("Inserte el número de alumnos: "))

for i in range(n):
    print("Ingresa el la altura ",i+1, " : ")
    altura = float(input())
    alumnos.append(altura)

suma = 0
for i in alumnos:
    suma = suma+1

mediaDeAltura = suma/n
altos=0
bajos=0
x = 0

for x in alumnos:
    if x <= mediaDeAltura:
        bajos = bajos + 1
    elif x >= mediaDeAltura:
        altos = altos + 1   

print("La media de altura de los alumnos: ", mediaDeAltura)
print("Los alumnos altos son: ", altos)
print("Los alumnos bajos son: ", bajos)
