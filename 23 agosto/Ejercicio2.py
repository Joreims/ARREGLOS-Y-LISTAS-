#Leer x cantidades de edades y decir cuantas son mayor de edad y cuantos son menores de edad
edades = []

def getMayoresEDAD(lista):
    suma = 0
    for edad in lista:
        if edad >= 18:
            suma += 1
    return suma

def getMenoresEdad(lista):
    suma = 0
    for edad in lista:
        if edad < 18:
            suma += 1
    return suma

def principal():
        resp = "si"
        while (resp.upper() != "NO"):
            try:
                edad = int(input("Edad: "))
                edades.append(edad)
                resp = input("Desea agregar otra edad SI-NO: ")
            except Exception as ex:
                print("Error: ", str(ex), "Intente de nuevo.")
        cantmayorEDAD = getMayoresEDAD(edades)
        cantMenorEdad = getMenoresEdad(edades)
        print("Cantidad de Mayores de edad: ", cantmayorEDAD)
        print("Cantidad de Mayores de edad: ", cantMenorEdad)
        
principal()