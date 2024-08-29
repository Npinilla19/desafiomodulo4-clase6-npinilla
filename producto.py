class Producto:
    """
    Representa un producto en inventario con nombre, precio y cantidad en stock.

    Atributos:
        nombre (str): Nombre del producto.
        precio (float): Precio del producto.
        stock (int): Cantidad de stock disponible del producto.

    Métodos:
        __str__(): Devuelve una representación en cadena del producto.
        __eq__(other): Compara si dos productos tienen el mismo nombre.
        __add__(cantidad): Aumenta el stock del producto en una cantidad especificada.
        __sub__(cantidad): Disminuye el stock del producto en una cantidad especificada, sin permitir que el stock sea negativo.
    """

    def __init__(self, nombre, precio, stock=0):
        """
        Inicializa una instancia de la clase Producto.

        Parámetros:
            nombre (str): Nombre del producto.
            precio (float): Precio del producto.
            stock (int, opcional): Cantidad inicial en stock. Por defecto es 0. No puede ser negativo.
        """
        self.__nombre = nombre
        self.__precio = precio
        self.__stock = max(stock, 0)  # Manejador stock negativo

    @property  # Getter
    def nombre(self):
        """
        Obtiene el nombre del producto.

        Returns:
            str: El nombre del producto.
        """
        return self.__nombre

    @property   # Getter
    def precio(self):
        """
        Obtiene el precio del producto.

        Returns:
            float: El precio del producto.
        """
        return self.__precio

    @property  # Getter
    def stock(self):
        """
        Obtiene la cantidad en stock del producto.

        Returns:
            int: La cantidad en stock del producto.
        """
        return self.__stock

    @stock.setter
    def stock(self, nuevo_stock):
        """
        Establece la cantidad en stock del producto.

        Args:
            nuevo_stock (int): La nueva cantidad en stock del producto. No permite valores negativos.
        """

        self.__stock = max(nuevo_stock, 0)  # No permite stock negativo

    @nombre.setter
    def nombre(self, nuevo_nombre):
        """
        Establece el nombre del producto.

        Args:
            nuevo_nombre (str): El nuevo nombre del producto.
        """
        self.__nombre = nuevo_nombre

    @precio.setter
    def precio(self, nuevo_precio):
        """
        Establece el precio del producto.

        Args:
            nuevo_precio (float): El nuevo precio del producto.
        """
        self.__precio = nuevo_precio

    # Sobrecarga de operadores
    def __str__(self):
        """
        Devuelve una representación en cadena del producto.

        Returns:
            str: Información del producto en formato de cadena.
        """
        return f"{self.__nombre} - ${self.__precio} - Stock: {self.__stock}"

    def __eq__(self, other):
        """
        Compara si el nombre de este producto es igual al nombre de otro producto.

        Args:
            other (Producto): Otro objeto de la clase Producto para comparar.

        Returns:
            bool: True si los nombres de los productos son iguales, False en caso contrario.
        """
        return self.__nombre == other.__nombre

    def __add__(self, cantidad):
        """
        Aumenta el stock del producto.

        Args:
            cantidad (int): Cantidad para agregar al stock.

        Returns:
            Producto: El producto con el stock actualizado.
        """
        self.__stock += cantidad
        return self

    def __sub__(self, cantidad):
        """
        Disminuye el stock del producto, sin permitir que sea negativo.

        Args:
            cantidad (int): Cantidad para restar del stock.

        Returns:
            Producto: El producto con el stock actualizado.
        """
        self.__stock -= min(self.__stock, cantidad)
        return self
