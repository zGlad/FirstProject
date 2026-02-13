
def es_divisible(n, d):
    """
    Determina el grado de divisibilidad de un número n respecto a d y su doble.

    Args:
        n (int): El número dividendo.
        d (int): El número divisor base.

    Returns:
        str: 
            - 2 si n es divisible por 2d.
            - 1 si n es divisible por d.
            - 0 si no es divisible por ninguno de los anteriores.
            - Mensaje de error si d es 0.
    """
    # Paso 1: Verificcamos que d no sea 0 para evitar divisiones inválidas 
    if d == 0: 
        return "No se puede dividir por 0"
    
    # Paso 2: 2d para la primera comprobación 
    dobleD = 2 * d 
    
    # Paso 3: Comprobamos las condiciones en orden de importancia 
    if n % dobleD == 0: 
        return 2
    if n % d == 0: 
        return 1
    else: 
        return 0
    
    # Ejemplos de uso:
print(es_divisible(20, 5))  # 20 es divisible por 10 (2d)
print(es_divisible(15, 5))  # 15 es divisible por 5 (d)
print(es_divisible(7, 3))   # 7 no es divisible ni por 3 ni por 6
print(es_divisible(0,0))    # 0 No se puede dividir