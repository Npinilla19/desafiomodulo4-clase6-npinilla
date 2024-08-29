class Producto:

    def __init__(self, nombre, precio, stock = 0):
        self.__nombre = nombre
        self.__precio = precio
        self.__stock = max(stock, 0) # Manejador stock negativo

    @property  # Getter
    def nombre(self):
        return self.__nombre

    @property   # Getter
    def precio(self):
        return self.__precio
    
    @property  # Getter
    def stock(self):
        return self.__stock
    
    @stock.setter
    def stock(self, nuevo_stock):
        self.__stock = max(nuevo_stock, 0)  # No permite stock negativo

    @nombre.setter
    def nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre
    
    @precio.setter
    def precio(self, nuevo_precio):
        self.__precio = nuevo_precio

    # Sobrecarga de operadores
    def __str__(self):
        return f"{self.__nombre} - ${self.__precio} - Stock: {self.__stock}"

    def __eq__(self, other):
        return self.__nombre == other.__nombre

    def __add__(self, cantidad):
        self.__stock += cantidad
        return self

    def __sub__(self, cantidad):
        self.__stock -= min(self.__stock, cantidad)
        return self
    