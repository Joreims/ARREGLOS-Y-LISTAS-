#Se desea contar el número de letras “a” y el número de letras “b” de una frase terminada en un punto. Se supone 
#que es posible leer los caracteres independientemente
frase = input("Ingresa una frase: ")
print("Numero de letras A:", frase.count("a")+frase.count("A"))
print("Numero de letras b:", frase.count("b")+frase.count("B"))