tickets = int(input("cuántos pasajes desea vender "))
totalIngresos = 0
for i in range (tickets):
    while True:
        try:
            price = int(input(f"Ingrese el precio de pasaje número {i + 1} "))
            totalIngresos += price
            break
        except ValueError:
            print("Por favor, ingresa un valor numérico")
print(f"El precio total de los pasajes es {totalIngresos}")