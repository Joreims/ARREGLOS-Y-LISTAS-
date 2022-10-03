from email.mime import nonmultipart
from Clases import Estudiante as est, ListadoEst as lst
ListaEst = lst
def menu():
    print("1. Agregar Registro")
    print("2. Editar Registro")
    print("3. Eliminar Registro")
    print("4. Buscar por código")
    print("10. Salir")
    op = int(input("Escriba su opcion: "))
    return op

def agregarRegistro():
    print("Agregar Datos del Estudiante")
    codigo = input("Codigo: ")
    nombres = input("Nombres: ")
    apellidos = input("Apellidos: ")
    carrera =   input("Carrera: ")
    resp = input("Posee beca? SI-NO: ")
    if(resp.upper()== "SI"): beca = True
    else: beca = False
    estudiante = est(codigo, nombres, apellidos, carrera, beca)
    ListaEst.agregarElemento(estudiante)

def modificarRegistro():
    print("Editar Registro")
    cod = input("Codigo: ")
    est, pos = ListaEst.buscarElemento(cod)
    print(f"""Nombres Actual: {est.Nombres} 
Apellidos actual: {est.Apellidos}
Carrera: {est.Carrera}
Beca: {est.Beca}""")
    print("|Nuevos Datos|")
    nuevoNombre = input("Nombres: ")
    nuevoApellidos = input("Apellidos: ")
    nuevaCarrera = input("Carrera: ")
    