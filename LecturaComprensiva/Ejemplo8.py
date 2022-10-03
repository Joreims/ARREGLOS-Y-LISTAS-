#Leer una letra. Deduce si está o no comprendida entre las letras mayúsculas I-M inclusive

letra = str(input("Digite la letra a Evaluar: "))

if letra.upper() >= "I" and letra.upper() <= "M":
    print("La letra se encuentra entre I y M")
else:
    print("La letra no se encuentra entre I y M")