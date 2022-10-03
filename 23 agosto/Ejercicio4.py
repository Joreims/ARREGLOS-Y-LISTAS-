#Almacenar los datos de un estudiantes tales como:
#nombres, apellidos, carrera y promedio.
from xml.dom import NoModificationAllowedErr


class Estudiante:

    def __init__(self, nom, ape, car, prom):
        self.Nombres = nom
        self.Apellidos = ape
        self.Carrera = car
        self.promedio = prom

    def mostrarDatos(self):

        return "Nombre: " + self.Nombres + "\nApellidos: " + self.Apellidos + "\nCarrera: " + self.Carrera + "\nPromedio: " + self.promedio


listado = []
bradly = Estudiante("Bradly", "Guitierrez", "ISI", 100)
jorge = Estudiante("Jorge", "Garcia", "ISI", 99)

listado.append(jorge)
listado.append(bradly)

