#Acá pondremos todas las caracteristicas de nuestro producto

class Producto:
    def __init__(self, cod, prod, precio, des, exmin, ex):
        self.Codigo = cod
        self.Producto = prod
        self.Descripcion = des
        self.Precio = precio
        self.Existencia = ex
        self.ExistenciaMinima = exmin
        
    
    def __str__(self):
        return f"""Codigo: {self.Codigo}
Producto: {self.Producto}
Descripción: {self.Descripcion}
Precio: {self.Precio}
Existencia Minima: {self.ExistenciaMinima}
Existencia: {self.Existencia}
"""

class ListaProd:

    def __init__(self):
        self.listap=[]

    def agregarProducto(self, dato):
        try:
            self.listap.append(dato)
        except Exception as ex:
            print("Ocurrio un error al agregar: ", str(ex))
    def editarProd(self, prod, pos):
        try:
            self.listap[pos]=prod
        except Exception as ex:
            print("Hubo un error que no permite editar, intente de nuevo", str(ex))
    
    def eliminarProd(self, eprod):
        try:
            self.listap.remove(eprod)
        except Exception as ex:
            print("Hubo un error al eliminar, intente de nuevo", str(ex))
    
    def buscarCod(self, cod):
        try:
            pos = 0
            for prod in self.listap:
                
                if prod.Codigo == cod:
                    print("Producto encontrado...")
                    return prod, pos
                else:
                    print("No se encontro...")
            pos+=1
        except Exception as ex:
            print("Error al buscar elemento:", str(ex))

    def buscarNom(self, Producto):
        try:
            p = 0
            for prod in self.listap:
                
                if prod.Producto == Producto:
                    print("Producto encontrado")
                    return prod, p
                else:
                    print("No se encontro el producto")
            p+=1
        except Exception as ex:
            print("Error al encontrar el producto", str(ex))

    def buscarPrecio(self, precio):
        try:
            p = 0
            for prod in self.listap:
                if prod.Precio == precio:
                    print("Producto encontrado")
                    return prod, p
                else:
                    print("No se encontro el producto")
            p+=1
        except Exception as ex:
            print("Error al encontrar el producto", str(ex))
    
