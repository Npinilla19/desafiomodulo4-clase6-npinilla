from tienda import Restaurante, Supermercado, Farmacia

def crear_tienda():
    """
    Crea una instancia de una tienda basada en el tipo especificado por el usuario.

    Solicita al usuario el nombre de la tienda, el costo de delivery y el tipo de tienda 
    (restaurante, supermercado, farmacia). Luego, crea y retorna una instancia de la tienda 
    correspondiente.

    Returns:
        Restaurante, Supermercado, Farmacia o None: Una instancia de la tienda correspondiente 
        o None si el tipo de tienda no es válido.
    """
    nombre = input("Ingrese el nombre de la tienda: ")
    costo_delivery = float(input("Ingrese el costo de delivery: "))
    tipo = input("Ingrese el tipo de tienda (restaurante, supermercado, farmacia): ").lower()

    if tipo == "restaurante":
        return Restaurante(nombre, costo_delivery)
    elif tipo == "supermercado":
        return Supermercado(nombre, costo_delivery)
    elif tipo == "farmacia":
        return Farmacia(nombre, costo_delivery)
    else:
        print("Tipo de tienda no válido.")
        return None

def main():
    """
    Función principal que maneja la interacción con el usuario para gestionar una tienda.

    Permite al usuario crear una tienda y luego realizar varias operaciones como ingresar 
    productos, listar productos, realizar ventas y salir del programa.
    """
    tienda = crear_tienda()
    if tienda:
        while True:
            print("\n1. Ingresar producto")
            print("2. Listar productos")
            print("3. Realizar venta")
            print("4. Salir")
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                nombre = input("Ingrese el nombre del producto: ")
                precio = float(input("Ingrese el precio del producto: "))
                stock = int(input("Ingrese el stock del producto: "))
                tienda.ingresar_producto(nombre, precio, stock)
            elif opcion == "2":
                print(tienda.listar_productos())
            elif opcion == "3":
                nombre = input("Ingrese el nombre del producto a vender: ")
                cantidad = int(input("Ingrese la cantidad a vender: "))
                tienda.realizar_venta(nombre, cantidad)
            elif opcion == "4":
                break
            else:
                print("Opción no válida.")

if __name__ == "__main__":
    main()
