def sucesion_fibonacci(cantidad_numeros: int) -> str: 
    """
    Genera una sucesión de Fibonacci de la cantidad de números indicados.
    
    Args:
        cantidad_numeros (int): Cantidad de números de la sucesión a generar.
        
    Returns:
        str: Cadena de texto con los números separados por comas.
    """
    # 1. Inicialización
    i = 0           # Contador para controlar el bucle While
    a, b = 0, 1     # Primeros dos números de la serie (semillas)
    serie = []      # Lista temporal para almacenar los números
    
    # 2. Lógica de generación (Bucle While)
    # Se ejecuta hasta que el contador alcanza el parámetro 'cantidad_numeros'
    while i < cantidad_numeros:
        serie.append(a)      # Guardamos el número actual
        a, b = b, a + b      # Actualización simultánea (a toma b, b toma la suma)
        i += 1               # Incrementamos el contador para evitar un bucle infinito
        
    # 3. Formateo "Inteligente" (Generador + Join)
    # Convertimos cada elemento (n) a string y los unimos con una coma
    resultado = ",".join(str(n) for n in serie)
    
    return resultado  # Devuelve el string para poder usarlo en otras partes del programa

# --- Probamos la función ---
print(sucesion_fibonacci(18))