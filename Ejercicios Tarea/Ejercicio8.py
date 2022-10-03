#Leer x cantidad de precios y mostrar el precio mas alto y el precio más bajo.
lista = []
cant = int(input("Cuantos productos desea ingresar?: "))
mayor = 0
menor = 0
i = 1

while(cant > 0):
    precio=float(input("Ingrese los precio # "+ str(i) + ": "))
    lista.append(precio)
    i = i + 1
    cant = cant - 1
mayor = max(lista)
menor = min(lista)

print("El precio mayor es: ",mayor)
print("El precio menor es: ",menor)
