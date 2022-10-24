from arbol import *

arbol = Arbol("Luis")
arbol.agregar("María José")
arbol.agregar("Maggie")
arbol.agregar("Leon")
arbol.agregar("Cuphead")
arbol.agregar("Jorge")
arbol.agregar("Jack")
nombre = input("Ingresa algo para agregar al árbol: ")
arbol.agregar(nombre)
arbol.preorden()
arbol.inorden()
arbol.postorden()

#Busqueda
busqueda = input("Busca algo en el árbol: ")
nodo = arbol.buscar(busqueda)
if nodo is None:
    print(f"{busqueda} no existe")
else:
    print(f"{busqueda} sí existe")
    