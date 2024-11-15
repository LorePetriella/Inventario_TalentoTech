# Código principal del menú interactivo

from funciones import agregar_producto, mostrar_inventario

def mostrar_menu():
    """Muestra las opciones del menú."""
    print("\nMenú de Gestión de Productos")
    print("1. Agregar producto al inventario")
    print("2. Mostrar productos en el inventario")
    print("0. Salir")

def main():
    """Función principal para ejecutar el menú interactivo."""
    opcion = ""
    while opcion != "0":
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            agregar_producto()
        elif opcion == "2":
            mostrar_inventario()
        elif opcion == "0":
            print("Saliendo del programa. ¡Hasta la próxima!")            
        else:
            print("Opción no válida. Inténtalo de nuevo.")

# Llamada a la función principal
if __name__ == "__main__":
    main()
