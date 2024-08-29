from producto import Producto
from abc import ABC, abstractmethod

class Tienda(ABC):
    def __init__(self, nombre, costo_delivery):
        self.__nombre = nombre
        self.__costo_delivery = costo_delivery
        self.productos = []

    def ingresar_producto(self, nombre, precio, stock):
        nuevo_producto = Producto(nombre, precio, stock)
        for producto in self.productos:
            if producto.nombre == nuevo_producto.nombre:
                if isinstance(self, Restaurante):
                    return  # El stock de productos en Restaurante siempre es 0
                else:
                    producto.stock += stock  # Añadir
                    print(producto.stock)
                    return
        self.productos.append(nuevo_producto) # Ingresar
            

    @abstractmethod
    def listar_productos(self):
        pass
    
    @abstractmethod
    def realizar_venta(self, nombre_producto, cantidad):
        pass

    @property
    def nombre(self):
        return self.__nombre

    @property
    def costo_delivery(self):
        return self.__costo_delivery


class Restaurante(Tienda):
    def ingresar_producto(self, nombre, precio, stock):
        super().ingresar_producto(nombre, precio, 0)  # Stock siempre es 0

    def listar_productos(self):
        return "\n".join([f"{p.nombre} - ${p.precio}" for p in self.productos])

    def realizar_venta(self, nombre_producto, cantidad):
        pass  # No se modifica stock en restaurante


class Supermercado(Tienda):
    def listar_productos(self):
        listado = []
        for p in self.productos:
            if p.stock < 10:
                listado.append(f"{p.nombre} - ${p.precio} - Pocos productos disponibles - Stock Disponible: {p.stock}")
            else:
                listado.append(f"{p.nombre} - ${p.precio} - Stock: {p.stock}")
        return "\n".join(listado)

    def realizar_venta(self, nombre_producto, cantidad):
        for p in self.productos:
            if p.nombre == nombre_producto:
                p - cantidad  # Sobrecarga de operador para restar stock
                print(p.stock)
                break
                
            else :  
                return f"Producto no encontrado"


class Farmacia(Tienda):
    def listar_productos(self):
        listado = []
        for p in self.productos:
            if p.precio > 15000:
                listado.append(f"{p.nombre} - ${p.precio} - Envío gratis al solicitar este producto")
            else:
                listado.append(f"{p.nombre} - ${p.precio}")
        return "\n".join(listado)

    def realizar_venta(self, nombre_producto, cantidad):
        if cantidad > 3:
            print("No se pueden vender más de 3 productos a la vez")
            
        for p in self.productos:
            if p.nombre == nombre_producto:
                p - cantidad  # Sobrecarga de operador para restar stock
                break
            else :
                print("Producto no encontrado")
               
            
           