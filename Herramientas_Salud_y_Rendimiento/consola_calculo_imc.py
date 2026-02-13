import calculadora_indices as calc

print("--- Calculadora de Índice de Masa Corporal (IMC) ---")

# Pedimos datos según el tipo definido (float) [cite: 83, 85]
peso = float(input("Ingrese el peso de la persona (en Kilogramos): "))
altura = float(input("Ingrese la altura de la persona (en metros): "))

# Llamamos a la función del módulo [cite: 79]
resultado = calc.calcular_IMC(peso, altura)

# Mostramos el resultado esperado [cite: 87]
print(f"El IMC de la persona es: {round(resultado, 2)}")