#Leer los datos de un estudiante como el nombre, los apellidos, la carrera y su promedio.
#Evaluar si apto para beca, el estudiante podrá optar a beca si su promedio es mayor a 85
#en todas las carreras excepto Ingeniería de Sistemas donde su promedio debe ser mayor a
#95.
print("_"*50)
numDeCuenta = int(input("\t Ingrese su número de cuenta \n"))
print("_"*50)
saldoActual = 600
print("Su saldo actual es de: ", saldoActual)
retiro = float(input(" \t Escriba la cantidad a retirar \n"))
print("_"*50)

if saldoActual < retiro: 
    print("_"*50)
    print("Lo sentimos, no tiene los suficientes fondos")
elif saldoActual == retiro:
    print("_"*50) 
    print("Su cuenta quedará en cero")
else: 
    print("_"*50)
    print("Saldo despues del retiro: ", saldoActual- retiro)