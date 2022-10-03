#Mostrar el total a pagar por la compra de n cantidad de productos a un precio desconocido
nombre = (input("Producto: "))
cant = int(input("Cuantos productos lleva?: "))
precio = int(input("Precio: "))

total = precio * cant
print("Total a pagar: ", total)