from Clases import Estudiante as est, ListadoEst as lst

listaEst = lst()

def menu():
    print("1. Agregar Registro")
    print("2. Editar Registro")
    print("3. Eliminar Registro")
    print("4. Buscar Registros")
    print("5. Mostrar Registros")
    print("10. Salir")
    op = int(input("Escriba su opción: "))
    return op

def agregarRegistro():
    print("Agregar Datos del Estudiante")
    codigo = input("Código: ")
    nombres = input("Nombres: ")
    apellidos = input("Apellidos: ")
    carrera = input("Carrera: ")
    resp = input("Posee beca? SI -NO: ")
    if(resp.upper() == "SI"): beca = True
    else: beca = False
    estudiante = est(codigo, nombres, apellidos, carrera, beca)
    print(estudiante)
    listaEst.agregarElemento(estudiante)

def modificarRegistro():
    print("Editar Registro ")
    cod = input("Código: ")
    est1, pos = listaEst.buscarElemento(cod)
    print(f"""Registro Actual""")
    print(est1)
    print("Nuevos Datos")
    nuevoNombre = input("Nombres: ")
    nuevoApellidos = input("Apellidos: ")
    nuevaCarrera = input("Carrera: ")
    resp = input("Posee beca? SI -NO: ")
    if(resp.upper() == "SI"): nuevaBeca = True
    else: nuevaBeca = False
    newEst = est(cod, nuevoNombre, nuevoApellidos, nuevaCarrera, nuevaBeca)
    listaEst.editarElemento(newEst, pos)

def eliminarRegistro():
    print("Eliminar Registro")
    cod = input("Código: ")
    est1, pos = listaEst.buscarElemento(cod)
    print(f"""Realmente desea eliminar el registro {est1}""")
    resp = input("SI - NO: ")
    if resp.upper()=="SI":
        listaEst.eliminarElemento(est1)
    else:
        print("Operación cancelada")

def buscarRegistro():
    print("Buscar Registro")
    cod = input("Código: ")
    try:
        est, pos = listaEst.buscarElemento(cod)
 
        if est.Codigo != None:
            print(est)
    except:
        print("Todo bien segui adelante")
        
def mostrarRegistros():
    for estudiante in listaEst.lista:
        print(estudiante)
        print("="*30)

def main():
    op = 0
    while(op!=10):
        op = menu()
        if op == 1: agregarRegistro()
        elif op == 2: modificarRegistro()
        elif op == 3: eliminarRegistro()
        elif op == 4: menuElemento2()
        elif op == 5: mostrarRegistros()
        elif op == 10: print("Ciao, ciao")
        else: print("Opcion no valida")
#Acá estamos creando un menú para que elijan la manera en la que quieren buscar
#Ya sea por codigo, nombre, apellido, carrera o beca
def menuBuscar():
        print("1. Buscar por codigo")
        print("2. Buscar por nombres")
        print("3. Buscar por apellidos")
        print("4. Buscar por carrera")
        print("5. Buscar por beca")
        print("6. Salir")
        o = int(input("Escriba su opción: "))
        return o

def menuElemento2():
        o = 0
        while(o!=10):
            o = menuBuscar()
            if o == 1: buscarRegistro()
            if o == 2: buscarnombre()
"""         if o == 3: buscarapellidos()
            if o == 4: buscarcarrera()
            if o == 5: buscarbeca()
"""
def buscarnombre():
    print("Buscar Registro")
    cod = input("Nombre: ")
    try:
        est, pos = listaEst.buscarnombre(cod)
 
        if est.Nombre != None:
            print(est)
    except:
        print("Todo bien segui adelante")
main()