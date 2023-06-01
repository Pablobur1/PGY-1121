#Prueba 1 en Python 
tarifas = {
    "Niño": 5500,
    "Joven": 7000,
    "Adulto": 9000
}


total_pagar = 0
contador_entradas = 0
acumulador_entradas = 0


while True:
    
    print("Bienvenido al sistema de venta de entradas del cine Moro")
    print("1. Registrar venta de entradas")
    print("2. Mostrar total a pagar")
    print("3. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        categoria = input("Ingrese la categoría de entrada (Niño/Joven/Adulto): ")
        if categoria not in tarifas:
            print("Categoría no válida. Por favor, ingrese una categoría válida.")
            continue

        cantidad = int(input("Ingrese la cantidad de entradas: "))
        if cantidad <= 0:
            print("Cantidad no válida. Por favor, ingrese una cantidad mayor a cero.")
            continue

        costo = tarifas[categoria]
        total_entrada = costo * cantidad

        
        contador_entradas += cantidad
        acumulador_entradas += total_entrada

        print(f"Venta registrada: {cantidad} entradas de categoría {categoria} por un total de ${total_entrada}")
        print()

    elif opcion == "2":
        print(f"Total a pagar: ${acumulador_entradas}")
        print()

    elif opcion == "3":
        print("¡Gracias Por su Compra,Disfrute de su Función!")
        break

    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")
        print()
