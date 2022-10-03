"""Escribir un programa que permita al usuario ingresar nuevos
pacientes, ver pacientes que esperan e imprimir el paciente que se va
atender."""

class Paciente:
    """Clase paciente"""
    def __init__(self, cod, nom, ape):
        self.nombres = nom
        self.apellidos = ape
        self.codigo = cod
    def __str__(self):
        return f"""Codigo: {self.codigo}
Nombres: {self.nombres}  
Apellidos: {self.apellidos}"""

class ColadePaciente:
    def __init__(self):
        self.cola = []

    def agregar(self, elem):
        self.cola.append(elem)

    def quitar(self):
        try:
            return self.cola.pop(0)    
        except Exception as ex:
            print("No hay pacientes esperando...", str(ex))
    
    def estaVacia(self):
        return self.cola == []