"""Calcular la media aritmetica de 
n cantidad de edades.
"""
resp = "SI"
edades = []
while(resp.upper() =="SI"):
    try:
        edad = int(input("Dime una edad: "))
        edades.append(edad)
        resp = input("Desea ingresar otra edad SI - NO")
    except Exception as ex:
        print("Error: ", str(ex))

suma = 0
for edad in edades:
    suma += edad

media = suma/ len(edades)

print("La media es ", media)
