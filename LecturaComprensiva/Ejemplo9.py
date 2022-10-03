#Contar el número de letras “i” de una frase terminada en un punto. 
#Se supone que las letras pueden leerse independientemente.
#frase.count cuenta las letras contenidas en una frase
frase = str(input("Ingrese una frase: "))
print("Numero de letras I:", frase.count("i")+frase.count("I"))