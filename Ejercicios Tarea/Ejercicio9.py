"""Leer los datos de un estudiante como el nombre, los apellidos, la carrera y su promedio.
Evaluar si apto para beca, el estudiante podrá optar a beca si su promedio es mayor a 85
en todas las carreras excepto Ingeniería de Sistemas donde su promedio debe ser mayor a
95."""
fname = input("Ingrese su primer nombre: \n")

sname = input("Ingrese su apellido: \n")

prom = float(input("Ingrese su promedio: \n"))
resp = "NO"
resp = input("Desea optar por Ingeniería en sistemas? SI-NO:  ")
if (resp.upper() == "SI"):
    if prom >= 95: 
        print("Felicidades, su beca ha sido aprobada")
    else:
        print("Lo sentimos, su beca ha sido rechazada")
elif(prom >= 85):
    print("Felicidades, su beca ha sido aprobada")
else:
    print("Lo sentimos, su beca ha sido rechazada")
