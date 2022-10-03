import Clases as c

lista = c.ListadoEst()

est = c.Estudiante("11", "HArry", "Bodan", "ISI", True)

lista.agregarElemento(est)
for est1 in lista.lista:
    print(est1)

est1 = c.Estudiante("11", "HArry", "BOdan Navarro", "Civil", False)
lista.editarElemento(est1, 0)

for est3 in lista.lista:
    print(est3)
    