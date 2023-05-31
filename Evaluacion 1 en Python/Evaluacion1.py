tarifas = {
    "Niño": {"costo": 5500, "edad_min": 1, "edad_max": 13},
    "Joven": {"costo": 7000, "edad_min": 14, "edad_max": 21},
    "Adulto": {"costo": 9000, "edad_min": 22, "edad_max": None}
}

def calcular_precio_entrada(categoria, cantidad):
    if categoria not in tarifas:
        return None
    
    tarifa = tarifas[categoria]
    costo = tarifa["costo"]
    
    return costo * cantidad

def main():
    categoria = input("Ingrese la categoría de entrada (Niño, Joven o Adulto): ")
    cantidad = int(input("Ingrese la cantidad de entradas a comprar: "))

    precio_total = calcular_precio_entrada(categoria, cantidad)

    if precio_total is None:
        print("Categoría inválida.")
        return

    print("Total a pagar: $", precio_total)
    print("Gracias por su compra, disfrute la función.")

if __name__ == "__main__":
    main()
