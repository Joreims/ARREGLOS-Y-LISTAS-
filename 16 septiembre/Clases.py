#Crear una lista de estudiantes
"""
Create
Read
Update
Delete
"""

from xmlrpc.server import _DispatchArity0


class Estudiante:
    def __init__(self, cod, nom, ape, car, bec):
        self.Codigo = cod
        self.Nombres = nom
        self.Apellido = ape
        self.Carrera = car
        self.Becado = bec   #Becado sera un valor Booleano

    def __str__(self):
        return f"""Codigo: {self.Codigo}
Nombres: {self.Nombres}
Apellidos: {self.Apellido}
Carrera: {self.Carrera}
Beca: {self.Becado}
"""

class ListadoEst:
    def __init__(self):
        self.lista = []
    
    def agregarElemento(self, dato):
        try:
            self.lista.append(dato)
        except Exception as ex:
            print("Ocurrio un error al agregar: ", str(ex))

    def editarElemento(self, dato, pos):
        try:
            self.lista[pos] = dato
        except Exception as ex:
            print("Ocurrio un error al editar: ", str(ex))    

    def eliminarElemento(self, pos):
        try:
            self.lista.remove(pos)
        except Exception as ex:
            print("Error al eliminar: ", str(ex))

    def buscarElemento(self,codigo):
        try:
            pos = 0
            for est in self.lista:
                if est.Codigo == codigo:
                    print("Estudiante encontrado...")
                    print(est)
            else:
                print("No se encontro...")
        except Exception as ex:
            print("Error al buscar elemento: ", str(ex))

