# EJEMPLO DE USO DE GITHUB
print("INGRESO DE DATOS")
print("----------------")
vNom = input("Ingrese su nombre: ")
while True:
    try:
     vEdad =int(input("Ingrese su edad: "))
    except:
     print("Error de Ingreso")


print("--------------------------")
print(f"Su Nombre es: {vNom}")
print(f"Su Edad es: {vEdad}")
print("Programa Finalizado")

