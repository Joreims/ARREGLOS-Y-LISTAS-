class Libro:
    def __init__(self, tit, aut, edi):
        self.titulo = tit
        self.autor = aut
        self.edicion = edi
        
    def __str__(self):
        return f""""Titulo: {self.titulo}
Autor: {self.autor}
Edicion: {self.edicion}"""   


libros = []
from time import sleep
def menu():
    print("Pila:")
    print("1. Ingresar libro")
    print("2. Prestar")
    print("3. Lista de Libros")
    print("4. Salir")
    print("Digite la opcion")

def ingresarlibro():
    tit = input("Titulo: ")
    aut = input("Autor: ")
    edi = int(input("Edicion en #: "))
    libros.append(Libro(tit, aut, edi))
    print("Se apila el libro...")

def sacarlibro():
    libro = libros.pop
    print(libro)
    print("Se ha desapilado el libro")
    sleep(2)

def mostrarpila():
    print("Libros apilados")
    tope = len(libros)-1
    while (tope >= 0):
        print(libros[tope])
        tope -=1


def main():
    try:
        op = 0
        while(op!=4):
            menu()
            op = int(input())
            if (op==1): ingresarlibro()
            elif(op==2): sacarlibro()
            elif(op==3): mostrarpila()
            elif(op==4): print("Te vas")
            else: print("Opcion inexistente")

    except Exception as ex:
        print("Error:",str(ex))

main()