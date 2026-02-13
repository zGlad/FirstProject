import calculadora_indices as calc

print("--- Calculadora de Porcentaje de Grasa Corporal ---")

# Pedimos los 4 parámetros requeridos [cite: 93, 95, 97, 99]
peso = float(input("Ingrese el peso de la persona (en Kilogramos): "))
altura = float(input("Ingrese la altura de la persona (en metros): "))
edad = int(input("Ingrese la edad de la persona (en años): "))
valor_genero = float(input("Ingrese el valor de género (10.8 para hombre, 0 para mujer): "))

# Llamamos a la función [cite: 112]
resultado = calc.calcular_porcentaje_grasa(peso, altura, edad, valor_genero)

print(f"El porcentaje de grasa corporal es: {round(resultado, 2)}%")