
def calcular_iva(precio_producto):
    iva = precio_producto * 0.19
    return iva

def descuento(precio_producto, descuento_aplicar):
    precio_final = precio_producto - descuento_aplicar
    print("Valor final del producto: ", precio_final)

def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    print("IMC: ", imc)
    if imc < 18.5:
        print("Estado: Bajo peso")
    elif imc >= 18.5 and imc <= 24.9:
        print("Estado: Adecuado")
    elif imc >= 25.0 and imc <= 29.9:
        print("Estado: Sobrepeso")
    elif imc >= 30.0 and imc <= 34.9:
        print("Estado: Obesidad grado 1")
    elif imc >= 35.0 and imc <= 39.9:
        print("Estado: Obesidad grado 2")
    else:
        print("Estado: Obesidad grado 3")

while True:
    print("Menú:")
    print("1. Calcular IVA")
    print("2. Aplicar descuento")
    print("3. Calcular IMC")
    print("4. Salir del programa")

    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        precio_producto = float(input("Ingrese el precio del producto: "))
        iva = calcular_iva(precio_producto)
        print("IVA: ", iva)
    elif opcion == "2":
        precio_producto = float(input("Ingrese el precio del producto: "))
        descuento_aplicar = float(input("Ingrese el descuento a aplicar: "))
        descuento(precio_producto, descuento_aplicar)
    elif opcion == "3":
        peso = float(input("Ingrese el peso en kg: "))
        altura = float(input("Ingrese la altura en metros: "))
        calcular_imc(peso, altura)
    elif opcion == "4":
        break
    else:
        print("Opción inválida. Por favor, selecciona una opción válida.")

print("Hasta luego")
