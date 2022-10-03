#Leer un carácter y deducir si está situado antes o después de la letra “m” en orden alfabético.
"""Solo sirve si el caracter es en minúsculas"""
caracter = str(input("Digita un caracter: "))
if caracter < "m":
    print("El caracter va antes que la letra m")
elif caracter == "m":
    print("Su caracter es m")
else:
    print("Su caracter va después de m")