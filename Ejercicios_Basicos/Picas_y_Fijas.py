def picas_y_fijas(numero_secreto, intento):
    """
    Calcula el número de Picas y Fijas en un juego de adivinanza numérica.
    
    Lógica:
    - Fija: El dígito existe en el número secreto y está en la posición correcta.
    - Pica: El dígito existe en el número secreto pero en una posición distinta.
    
    Args:
        numero_secreto (int): El número de 4 cifras a adivinar.
        intento (int): El número propuesto por el jugador.
        
    Returns:
        dict: Diccionario con el conteo de {'PICAS': int, 'FIJAS': int}.
    """
    
    # 1. Normalización: Convertimos a string y aseguramos 4 dígitos (ej: 0123)
    secreto_str = str(numero_secreto).zfill(4)
    intento_str = str(intento).zfill(4)
    
    fijas = 0
    picas = 0
    
    # Listas para almacenar dígitos que no fueron coincidencias exactas (fijas)
    # Esto evita contar un mismo dígito como fija y pica simultáneamente.
    secreto_restante = []
    intento_restante = []
    
    # --- PASO 1: Identificar FIJAS ---
    for i in range(4):
        if intento_str[i] == secreto_str[i]:
            fijas += 1
        else:
            # Si no coinciden, guardamos ambos para el análisis de picas
            secreto_restante.append(secreto_str[i])
            intento_restante.append(intento_str[i])
    
    # --- PASO 2: Identificar PICAS ---
    # Usamos set() sobre los sobrantes del intento para procesar valores únicos.
    # Esto previene errores si el usuario repite dígitos en su intento.
    for digito in set(intento_restante):
        if digito in secreto_restante:
            picas += 1
            
    return {
        "PICAS": picas, 
        "FIJAS": fijas
    }

# Ejemplo de uso y validación
print("Resultado del intento:" + picas_y_fijas(1234, 1341))