
## Descripción
Este proyecto permite gestionar diferentes tipos de tiendas (Restaurante, Supermercado y Farmacia) mediante una interfaz de línea de comandos. A continuación, se describe brevemente la funcionalidad principal para cada uno de los siguientes archivos:

## 01- producto.py
Define la clase Producto que representa un producto con nombre, precio y stock. Incluye métodos para:
Inicializar una nueva instancia de Producto.
Obtener y establecer los valores de nombre, precio y stock.
Sobrecargar operadores para representar el producto, comparar productos y ajustar el stock.

 
## 02- tienda.py
Define una estructura para gestionar diferentes tipos de tiendas utilizando clases abstractas y herencia:
Clase Tienda: Clase abstracta que representa una tienda con atributos como nombre, costo_delivery y productos. Incluye métodos para ingresar productos, listar productos y realizar ventas.
Clase Restaurante: Hereda de Tienda y redefine métodos para ingresar productos con stock siempre igual a 0, listar productos y realizar ventas sin modificar el stock.
Clase Supermercado: Hereda de Tienda y redefine métodos para listar productos con stock y realizar ventas actualizando el stock.
Clase Farmacia: Hereda de Tienda y redefine métodos para listar productos indicando si tienen envío gratis y realizar ventas con restricciones en la cantidad.

## 03- programa.py
Maneja la interacción con el usuario para gestionar una tienda:
Función crear_tienda: Solicita al usuario el nombre de la tienda, el costo de delivery y el tipo de tienda, y crea una instancia de la tienda correspondiente.
Función main: Permite al usuario crear una tienda y realizar varias operaciones como ingresar productos, listar productos, realizar ventas y salir del programa. Muestra un menú de opciones y ejecuta la opción seleccionada por el usuario.

## Ejecución del Programa

Para ejecutar el programa, simplemente corre el archivo principal (programa.py). El programa solicitará la información necesaria para crear una tienda y luego permitirá gestionar los productos y ventas a través de un menú interactivo

## Prerrequisitos o Dependencias

Sistema Operativo Windows, Linux, MacOS
Lenguaje de programación Python 3.12

## Instalación del Proyecto

Clonar el repositorio:

```bash
# git@github.com:bpardo02/desafiomodulo4-clase6.git
```

Ingresar a la carpeta del proyecto:

```bash
# desafiomodulo4-clase6
```

Autor

- [Vanessa Morales](https://github.com/vanemn)
- [Benjamín Pardo](https://github.com/bpardo02)
- [Nicole Pinilla](https://github.com/Npinilla19)
