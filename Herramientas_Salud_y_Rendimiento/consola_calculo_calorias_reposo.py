import calculadora_indices as calc

print("--- Calculadora de Calorías en Reposo (TMB) ---")

# Nota: Según la fórmula, aquí la altura se pide en CENTÍMETROS [cite: 124]
peso = float(input("Ingrese el peso de la persona (en Kilogramos): "))
altura = float(input("Ingrese la altura de la persona (en centímetros): "))
edad = int(input("Ingrese la edad de la persona (en años): "))
valor_genero = int(input("Ingrese el valor (5 para hombre, -161 para mujer): "))

resultado = calc.calcular_calorias_en_reposo(peso, altura, edad, valor_genero)

print(f"La cantidad de calorías que la persona quema en reposo es: {resultado} cal")