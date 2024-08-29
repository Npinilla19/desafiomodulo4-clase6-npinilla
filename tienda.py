from producto import Producto
from abc import ABC, abstractmethod

class Tienda(ABC):
    """
    Clase abstracta que representa una tienda.

    Attributes:
        nombre (str): El nombre de la tienda.
        costo_delivery (float): El costo de delivery de la tienda.
        productos (list): Lista de productos disponibles en la tienda.
    """
    def __init__(self, nombre, costo_delivery):
        """
        Inicializa una nueva instancia de la clase Tienda.

        Args:
            nombre (str): El nombre de la tienda.
            costo_delivery (float): El costo de delivery de la tienda.
        """
        self.__nombre = nombre
        self.__costo_delivery = costo_delivery
        self.productos = []

    def ingresar_producto(self, nombre, precio, stock):
        """
        Ingresa un nuevo producto a la tienda o actualiza el stock de un producto existente.

        Args:
            nombre (str): El nombre del producto.
            precio (float): El precio del producto.
            stock (int): La cantidad de stock del producto.
        """
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
        """
        Lista todos los productos disponibles en la tienda.

        Returns:
            str: Una cadena con la lista de productos.
        """
        pass
    
    @abstractmethod
    def realizar_venta(self, nombre_producto, cantidad):
        """
        Realiza la venta de un producto, actualizando el stock.

        Args:
            nombre_producto (str): El nombre del producto a vender.
            cantidad (int): La cantidad del producto a vender.
        """
        pass

    @property
    def nombre(self):
         """
        Obtiene el nombre de la tienda.

        Returns:
            str: El nombre de la tienda.
        """
        return self.__nombre

    @property
    def costo_delivery(self):
        """
        Obtiene el costo de delivery de la tienda.

        Returns:
            float: El costo de delivery de la tienda.
        """
        return self.__costo_delivery


class Restaurante(Tienda):
    """
    Clase que representa un restaurante, hereda de Tienda.
    """
    def ingresar_producto(self, nombre, precio, stock):
        """
        Ingresa un nuevo producto al restaurante con stock siempre igual a 0.

        Args:
            nombre (str): El nombre del producto.
            precio (float): El precio del producto.
            stock (int): La cantidad de stock del producto (no se usa).
        """
        super().ingresar_producto(nombre, precio, 0)  # Stock siempre es 0

    def listar_productos(self):
        """
        Lista todos los productos disponibles en el restaurante.

        Returns:
            str: Una cadena con la lista de productos y sus precios.
        """
        return "\n".join([f"{p.nombre} - ${p.precio}" for p in self.productos])

    def realizar_venta(self, nombre_producto, cantidad):
        """
        Realiza la venta de un producto en el restaurante (no modifica stock).

        Args:
            nombre_producto (str): El nombre del producto a vender.
            cantidad (int): La cantidad del producto a vender.
        """
        pass  # No se modifica stock en restaurante


class Supermercado(Tienda):
    """
    Clase que representa un supermercado, hereda de Tienda.
    """
    def listar_productos(self):
        """
        Lista todos los productos disponibles en el supermercado.

        Returns:
            str: Una cadena con la lista de productos, sus precios y stock.
        """
        listado = []
        for p in self.productos:
            if p.stock < 10:
                listado.append(f"{p.nombre} - ${p.precio} - Pocos productos disponibles - Stock Disponible: {p.stock}")
            else:
                listado.append(f"{p.nombre} - ${p.precio} - Stock: {p.stock}")
        return "\n".join(listado)

    def realizar_venta(self, nombre_producto, cantidad):
        for p in self.productos:
            """
        Realiza la venta de un producto en el supermercado, actualizando el stock.

        Args:
            nombre_producto (str): El nombre del producto a vender.
            cantidad (int): La cantidad del producto a vender.

        Returns:
            str: Mensaje indicando si el producto fue encontrado o no.
        """
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
               
            
           