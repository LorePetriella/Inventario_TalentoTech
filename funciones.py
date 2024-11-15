# Funciones para gestionar el inventario

# Lista para almacenar los productos del inventario.
inventario = []

def agregar_producto():
    """Agrega un producto al inventario."""
    nombre = input("Introduce el nombre del producto: ").strip()
    cantidad = input("Introduce la cantidad de stock del producto: ").strip()
    if cantidad.isdigit() and cantidad != "0":
        cantidad = int(cantidad)
        inventario.append({"nombre": nombre, "cantidad": int(cantidad)})
        print(f"Se agregaron {cantidad} unidades del producto '{nombre}'.")
    else:
        print("La cantidad debe ser un número válido.")

def mostrar_inventario():
    """Muestra todos los productos del inventario."""
    if inventario:
        print("\nProductos en el inventario:")
        for i, producto in enumerate(inventario, start=1):
            print(f"{i}. {producto['nombre']} - Cantidad: {producto['cantidad']}")
    else:
        print("El inventario está vacío.")
