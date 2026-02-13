import calculadora_indices as calc

print("--- Calculadora para Adelgazar ---")

peso = float(input("Ingrese el peso (kg): "))
altura = float(input("Ingrese la altura (cm): "))
edad = int(input("Ingrese la edad (años): "))
valor_genero = float(input("Ingrese valor género (5 hombre, -161 mujer): "))

# Esta función ya devuelve la frase completa armada [cite: 126]
resultado = calc.consumo_calorias_recomendado_para_adelgazar(peso, altura, edad, valor_genero)

print(resultado)