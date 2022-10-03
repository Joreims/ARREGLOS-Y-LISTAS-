from math import prod
from os import system
from Clases import Producto as prot, ListaProd as lst

ltProd = lst()

def menu():
    print("1. Agregar Producto")
    print("2. Editar Producto")
    print("3. Eliminar Producto")
    print("4. Buscar por Codigo")
    print("5. Buscar por Precio")
    print("6. Buscar por Nombre")
    print("7. Mostrar Productos")
    print("10. Salir")
    op = int(input("Escriba su opción: "))
    return op

def agregarProducto():
    print("Agregar Datos del Producto")
    codigo = input("Código: ")
    nombres = input("Nombres: ")
    precio = int(input("Precio: "))
    descripcion = input("Descripcion: ")
    exmin = int(input("Digite la existencia minima: "))
    existencia =int(input("digite la existencia del producto: "))
    ltsProductos = prot(codigo, nombres, precio, descripcion, exmin, existencia)
    if existencia<exmin :
        print("La existencia es menor que la minima")
        print("Por favor rellene el stock para que sea mayor al minimo de seguridad")
        print(ltsProductos)
    else :
        print("El stock es mayor que la minima")

    ltProd.agregarProducto(ltsProductos)
    print("Producto guardado...")
    system("pause")

def modificarProducto():
    print("Editar Registro ")
    cod = input("Código: ")
    pro, pos = ltProd.buscarCod(cod)
    print(f"""Nombre Actual: {pro.Producto}
Precio actual: {pro.Precio}
Descripcion actual: {pro.Descripcion}""")

    print("Nuevos Datos")
    nuevoNombre = input("Nombres: ")
    nuevoPrecio = int(input("Precio: "))
    nuevoDescripcions = input("Descripcion: ")
    nuevaExistencia= int(input("Existencia: "))
    nuevaMin= int(input("Minimo: "))
    newInv = prot(pro.Codigo,nuevoNombre,nuevoPrecio,nuevoDescripcions,nuevaExistencia,nuevaMin)
    ltProd.editarProd(newInv, pos)

def eliminarProducto():
    print("Eliminar Producto")
    cod = input("Codigo del Producto a Eliminar:")
    prod, pos = ltProd.buscarCod(cod)
    print(f"""Desea eliminar el Producto {prod}""")
    r = input("SI/NO")
    if r.upper()== "SI":
        ltProd.eliminarProd(prod)
    else:
        print("No se eliminará el elemento")

def buscarporNombre():
    print("Buscar Registro")
    prod = input("Nombre: ")
    try:
        prod1, pos = ltProd.buscarNom(prod)
 
        if prod1.Producto != None:
            print(prod1)
    except:
        print("Todo bien piola, segui adelante")

def buscarCodigo():
    cod = input("Codigo del producto: ")
    try:
        prod, pos = ltProd.buscarCod(cod)

        if prod.Codigo != None:
            print(prod)
        else:
            print("No se encontro nada")
    except Exception as ex:
        print("Error")

def buscarporPrecio():
    print("Buscar Registro")
    precio = int(input("Precio: "))
    try:
        prod, pos = ltProd.buscarPrecio(precio)
 
        if prod.Precio != None:
            print(prod)
    except:
        print("Todo bien segui adelante")

def mostrarRegistro():
    for productos in ltProd.listap:
        print(productos)
        print("="*30)
        system("pause")

def main():
    op = 0
    while(op!=10):
        op = menu()
        if op == 1: agregarProducto()
        elif op == 2: modificarProducto()
        elif op == 3: eliminarProducto()
        elif op == 4: buscarCodigo()
        elif op == 5: buscarporPrecio()
        elif op == 6: buscarporNombre()
        elif op == 7: mostrarRegistro()
        elif op == 10: print("Ciao, ciao")
        else: print("Opcion no valida")

main()

        