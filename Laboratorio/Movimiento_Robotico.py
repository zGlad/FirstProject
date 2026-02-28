def movimiento_robot(orientacion_actual: str, giro_1: str, giro_2: str, giro_3: str) -> str: 
    """
    Calcula la orientación final de un robot tras aplicar tres comandos de giro.

    Args:
        orientacion_actual (str): Representa el punto cardinal inicial ("N", "S", "E", "W").
        giro_1 (str): Primer comando del control remoto ("L", "R", "H", ".").
        giro_2 (str): Segundo comando del control remoto.
        giro_3 (str): Tercer comando del control remoto.

    Returns:
        str: 
            - "N" si la orientación final es Norte.
            - "S" si la orientación final es Sur.
            - "E" si la orientación final es Este.
            - "W" si la orientación final es Oeste.
    """
    # Esto permite que un giro a la derecha sea (+1) y a la izquierda (-1)
    direcciones = ['N', 'E', 'S', 'W']
    
    # Paso 2: Localizamos el índice numérico de la orientación inicial
    indice = direcciones.index(orientacion_actual) 
    
    # Paso 3: Agrupamos los comandos para procesarlos de forma secuencial
    comandos = (giro_1, giro_2, giro_3)
    
    # Paso 4: Iteramos sobre cada comando y actualizamos el índice de dirección
    for comando in comandos:       
        if comando == 'R':
            # Giro a la derecha (módulo 4 para ciclar)
            indice = (indice + 1) % 4
    
        elif comando == 'L':
            # Giro a la izquierda 
            indice = (indice - 1) % 4 
        
        elif comando == 'H':
            # Media vuelta:
            indice = (indice + 2) % 4    
    
        elif comando == '.': 
            # Mantener orientación:
            pass 
    
    # Paso 5: Retornamos la letra correspondiente al índice final alcanzado
    return direcciones[indice]

# Ejemplos de uso:
print(movimiento_robot('N', 'R', 'R', 'R'))  # "W"
