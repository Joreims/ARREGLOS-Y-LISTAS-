from sqlite3 import DateFromTicks


class Nodo:
    def __init__(self, dato):
        self.dato = dato
        # Son none ya que al inicio el único valor que existe es el de la raíz
        self.izquierda = None
        self.derecha = None