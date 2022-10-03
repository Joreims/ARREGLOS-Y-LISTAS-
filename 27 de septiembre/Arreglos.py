#Arreglos
edades = [15,18,27,15]
print(edades)
#Posición 
mi_edad = edades[2]
print("Mi edad es: "+ str(mi_edad))
#Editar un arreglo
edades[1] = 19
print(edades)
#LEN → saber la cantidad de elementos que tiene un arreglo
print("Cantidad de elementos que tiene el arreglo es: "+ str(len(edades)))
#APPEND → agregar un elemento al final del arreglo
edades.append(20)
print(edades)
#COUNT → contar la cantidad de veces que un elemento se repite en un arreglo
print("Veces que se repite el 15: "+ str(edades.count(15)))
#INDEX → devuelve la posición del elemento buscado
posicion = edades.index(19)
print("La posicion de 19 es: "+ str(posicion))
#Consulta de una edad por posición
mi_edad1 = edades[posicion]
print("Mi edad es: "+ str(mi_edad1))
#Insert → Insertar un numero en una posición determinada
numero = 99
edades.insert(3,numero)
print(edades)
# POP → Devuelve el ultimo elemento pero lo elimina
ultimo_elemento= edades.pop()
print("Ultimo elemento: "+ str(ultimo_elemento))
print(edades)
#Remove → Eliminar un elemento en especifico
edades.remove(99)
print(edades)
#Reverse → Cambia la posicion del ultimo elemento al primero
edades.append(35)
edades.reverse()
print(edades)
#SORT → Ordena todos los elementos repetidos y los ordena de mayor a menor
edades.sort()
print(edades)
# Para poner de mayor a menor
edades.sort(reverse=True)
print(edades)
#Recorrer el arreglo con for
#range
#range empieza en 0 y llega hasta el final del arreglo
#Imprime todos los elementos del arreglo con su posición
for i in range(len(edades)):
    print("La edad en la posicion: "+str(i)+" es: "+ str(edades[i]))
# Lo mismo pero ahora, le sumamos 5 a cada edad para saber cuanto
#será dentro de 5 años
for i in range(len(edades)):
    edad = edades[i]
    resultado = edad + 5
    print("La edad en la posicion: "+str(i)+" es: "+ str(edades[i]))
    print(" Esta edad en 5 años va ser: "+str(resultado))


