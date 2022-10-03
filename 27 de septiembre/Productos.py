class Producto:
    def _init_(self, cod, nom, pre):
        self.Codigo = cod
        self.Nombre = nom
        self.Precio = pre

    def _str_(self):
        return f"""Código: {self.Codigo}
Nombre: {self.Nombre}
Precio: {self.Precio}
"""
class ListaProducto:
    def _init_(self):
        self.lista = []

    def agregarProductos(self, producto):
        self.lista.append(producto)

    def imprimirProducto(self):
        for prod in self.lista:
            print(prod)

listita = ListaProducto()

producto = Producto(1,"Coca Cola", 34.50)
listita.agregarProductos(producto)
producto1 = Producto(2, "Pepsi", 50.78)
listita.agregarProductos(producto1)
producto2 = Producto(3, "Prix Cola", 20.56)
listita.agregarProductos(producto2)
listita.imprimirProducto()