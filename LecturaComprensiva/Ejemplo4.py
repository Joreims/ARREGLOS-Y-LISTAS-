"""Se tiene un array Coches de nueve elementos de 
contiene siete marcas de automóviles en orden
 alfabético y se desea
insertar dos nuevas marcas: Opel y Citroën."""
coches = ["AlfaRomero","Fiat","Ford","Lancia","Renault", "Seat"]

print(coches)

a=input("Escriba la marca de coche que desea agregar al arreglo: ")

b=input("Escriba la marca de coche que desea agregar al arreglo: ")

coches.insert(4,a)
coches.insert(1,b)
print(coches)