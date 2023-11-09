class product:
    def __init__(self, precio, nombre, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def __str__(self):
        return "producto: {}, precio: ${:.2f}, cantidad: {}".format(self.nombre, self.precio, self.cantidad)

class almacen:
    def __init__(self):
        self.inv = []

    def agregarproducto(self, producto):
        for p in self.inv:
            if p.nombre == producto.nombre:
                print(f"'{producto.nombre}' ya se encuentra en el almacen")
                return
            
        self.inv.append(producto)
        print(f"'{producto.nombre}' ha sido agregado al almacen")

    def actualizar_cantidad(self, nombre, cantidad):
        for producto in self.inv:
            if producto.nombre == nombre:
                producto.cantidad += cantidad
                print(f"Cantidad del producto '{nombre}' actualizado. Existencias actuales: {producto.cantidad}")
                return
        print(f"No hay existencias de '{nombre}' en stock")

Almacen = almacen()

while True:
    print("\nMenú:")
    print("1. Añadir Producto")
    print("2. Mostrar el inventario")
    print("3. Actualizar cantidad en stock")
    print("4. Salida")
    opcion = input("Pulsa el número correspondiente para seleccionar una opción: ")

    if opcion == "1":
        nombre = input("Ingrese el nombre del producto: ")
        precio = float(input("Ingrese el precio del producto: "))  # Convertir a float
        cantidad = int(input("Agregue la cantidad en stock del producto: "))
        nuevo_producto = product(precio, nombre, cantidad)  # Poner el precio como el primer argumento
        Almacen.agregarproducto(nuevo_producto)

    elif opcion == "2":
        if len(Almacen.inv) == 0:
            print("No hay existencias en el almacén.")   
        else:
            print("Inventario almacén:")
            for producto in Almacen.inv:
                print(producto)

    elif opcion == "3":
        nombre = input("Nombre del producto: ")
        cantidad = int(input("Ingrese la cantidad que desea añadir, si desea quitar existencias ingrese el valor en formato negativo: "))
        Almacen.actualizar_cantidad(nombre, cantidad)

    elif opcion == "4":
        print("Hasta luego.")
        break

    else:
        print("Opción no válida. Por favor, selecciona una opción válida.")


