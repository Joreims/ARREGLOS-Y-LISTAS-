"""realizando las siguientes operaciones; a) lectura del array, b) cálculo de la
suma de los valores del array, c) cálculo de la media de los valores."""
suma = 0
puntos=[]
i=0
Limite = 5-1
while i<=Limite: #contador<=40
    val= int(input("Ingrese un valor del arreglo: "))
    puntos.append(val)
    i= i+1
    suma = suma + val
    media = suma / len(puntos)
    print("La media es: ", media)
while i<=Limite:
    if puntos>media:
        print(puntos)