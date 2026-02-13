import calculadora_indices as calc

print("--- Calculadora de Calorías por Actividad Física ---")

peso = float(input("Ingrese el peso (kg): "))
altura = float(input("Ingrese la altura (cm): "))
edad = int(input("Ingrese la edad (años): "))
valor_genero = float(input("Ingrese valor género (5 hombre, -161 mujer): "))

print("Valores de actividad:")
print("1.2: poco/nada | 1.375: ligero | 1.55: moderado | 1.725: deportista | 1.9: atleta")
valor_actividad = float(input("Ingrese el valor de actividad física: "))

resultado = calc.calcular_calorias_en_actividad(peso, altura, edad, valor_genero, valor_actividad)

print(f"La cantidad de calorías que quema al realizar actividad es: {resultado} cal")