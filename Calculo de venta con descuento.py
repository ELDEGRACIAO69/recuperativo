#Entrada
print("Calculo de venta con descuento")


def calcular_descuento(subtotal):
    # Proceso: determina si corresponde el descuento del 10%
    if subtotal >= 50000:
        descuento = subtotal * 0.10
    else:
        descuento = 0
    return descuento


def mostrar_resultado(nombre_producto, subtotal, descuento, total):
    # Proceso: mostrar la informacion en pantalla como nombre del producto, subtotal, descuento y total
    print("\n--- Resumen de la venta ---")
    print("Producto:", nombre_producto)
    print("Subtotal: $", subtotal)
    print("Descuento: $", descuento)
    print("Total a pagar: $", total)
    print("----------------------------\n")


# Programa principal
#al poner s continua el proceso en cambio otra letra termina el proceso
continuar = "s"

while continuar == "s":

    # Entrada: nombre del producto
    nombre_producto = input("Ingrese el nombre del producto: ")
    while nombre_producto.strip() == "":
        print("El nombre no puede estar vacío.")
        nombre_producto = input("Ingrese el nombre del producto: ")

    # Entrada y Proceso: precio unitario (validado con try/except en cazo de error para que el programa no muera)
    precio_valido = False
    while not precio_valido:
        try:
            precio_unitario = float(input("Ingrese el precio unitario: "))
            if precio_unitario > 0:
                precio_valido = True
            else:
                print("El precio debe ser mayor que cero.")
        except ValueError:
            print("Debe ingresar un numero valido para el precio.")

    # Entrada y Proceso: cantidad comprada (validada con try/except en cazo de error para que el programa no muera)
    cantidad_valida = False
    while not cantidad_valida:
        try:
            cantidad_comprada = int(input("Ingrese la cantidad comprada: "))
            if cantidad_comprada > 0:
                cantidad_valida = True
            else:
                print("La cantidad debe ser mayor que cero.")
        except ValueError:
            print("Debe ingresar un numero entero valido para la cantidad.")

    # Proceso: calculo del subtotal
    subtotal = precio_unitario * cantidad_comprada

    # Proceso: calculo del descuento llamando a la funcion
    descuento = calcular_descuento(subtotal)

    # Proceso: calculo del total a pagar
    total = subtotal - descuento

    # Salida: mostrar resultado llamando a la funcion
    mostrar_resultado(nombre_producto, subtotal, descuento, total)

    # Entrada: preguntar si desea continuar
    continuar = input("¿Desea realizar otra venta? (s/n): ").strip().lower()
    while continuar != "s" and continuar != "n":
        print("Respuesta invalida.")
        continuar = input("¿Desea realizar otra venta? (s/n): ").strip().lower()
#mensaje final
print("Programa finalizado.")
