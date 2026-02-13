"""
Módulo: calculadora_indices.py
Contiene las funciones lógicas para el cálculo de índices corporales.
"""

def calcular_IMC(peso: float, altura: float) -> float:
    # Calcula el índice de masa corporal [cite: 79, 80]
    # Fórmula: peso / altura^2 [cite: 32]
    return peso / (altura ** 2)

def calcular_porcentaje_grasa(peso: float, altura: float, edad: int, valor_genero: float) -> float:
    # Calcula el porcentaje de grasa corporal [cite: 112, 113]
    # Primero se obtiene el IMC [cite: 37]
    imc = calcular_IMC(peso, altura)
    # Fórmula: 1.2 * IMC + 0.23 * edad - 5.4 - valor_genero [cite: 38]
    return 1.2 * imc + 0.23 * edad - 5.4 - valor_genero

def calcular_calorias_en_reposo(peso: float, altura: float, edad: int, valor_genero: int) -> float:
    # Calcula la Tasa Metabólica Basal (TMB) [cite: 120, 121]
    # Fórmula: (10 * peso) + (6.25 * altura) - (5 * edad) + valor_genero [cite: 47]
    return (10 * peso) + (6.25 * altura) - (5 * edad) + valor_genero

def calcular_calorias_en_actividad(peso: float, altura: float, edad: int, valor_genero: float, valor_actividad: float) -> float:
    # Calcula calorías según actividad física [cite: 126]
    tmb = calcular_calorias_en_reposo(peso, altura, edad, valor_genero)
    # Fórmula: TMB * valor_actividad [cite: 52]
    return tmb * valor_actividad

def consumo_calorias_recomendado_para_adelgazar(peso: float, altura: float, edad: int, valor_genero: float) -> str:
    # Calcula el rango para adelgazar (80% a 85% de la TMB) [cite: 61, 126]
    tmb = calcular_calorias_en_reposo(peso, altura, edad, valor_genero)
    rango_inferior = tmb * 0.80 
    rango_superior = tmb * 0.85 
    return f"Para adelgazar es recomendado que consumas entre: {rango_inferior} y {rango_superior} calorías al día."    