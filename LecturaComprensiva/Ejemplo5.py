#Se desea eliminar los blancos de una frase dada terminada en un punto. Se supone que es posible leer los caracteres 
#de la frase de uno en uno.
# != sirve para comparar 2 elementos
a = str(input("Digite una cadena con espacios: "))
for elemento in a:
    if elemento != " ":
        print(elemento, end="")
