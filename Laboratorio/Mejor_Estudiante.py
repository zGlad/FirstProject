def calcular_promedio(estudiante: dict) -> float:
    """
    Calcula el promedio aritmético de las cinco materias de un estudiante.

    Args:
        estudiante (dict): Diccionario con las notas del estudiante.

    Returns:
        float: El promedio de las notas.
    """
    materias = ["matematicas", "español", "ciencias", "literatura", "arte"]
    # Sumamos los valores asociados a cada materia y dividimos por el total
    total_notas = sum(estudiante[materia] for materia in materias)
    return total_notas / len(materias)




def mejor_del_salon(estudiante1: dict, estudiante2: dict, estudiante3: dict, 
                    estudiante4: dict, estudiante5: dict) -> str:
    """
    Identifica al estudiante con el promedio más alto en un grupo de cinco.
    
    En caso de empate en el promedio, se selecciona al estudiante cuyo nombre 
    sea alfabéticamente menor (A-Z), sin distinguir entre mayúsculas y minúsculas.

    Args:
        estudiante1 (dict): Datos del primer estudiante (nombre y 5 notas).
        estudiante2 (dict): Datos del segundo estudiante (nombre y 5 notas).
        estudiante3 (dict): Datos del tercer estudiante (nombre y 5 notas).
        estudiante4 (dict): Datos del cuarto estudiante (nombre y 5 notas).
        estudiante5 (dict): Datos del quinto estudiante (nombre y 5 notas).

    Returns:
        str: El nombre del estudiante con el mejor desempeño.
    """
    # Agrupamos los diccionarios en una lista para procesarlos cíclicamente
    lista_estudiantes = [estudiante1, estudiante2, estudiante3, estudiante4, estudiante5]
    
    # Inicializamos variables de control
    mejor_nombre = ""
    mejor_promedio = -1.0  # Iniciamos en -1 para que cualquier nota (0-5) sea mayor

    for estudiante in lista_estudiantes:
        nombre_actual = estudiante["nombre"]
        promedio_actual = calcular_promedio(estudiante)
        
        # CASO 1: Encontramos un promedio estrictamente mayor
        if promedio_actual > mejor_promedio:
            mejor_promedio = promedio_actual
            mejor_nombre = nombre_actual
            
        # CASO 2: Hay un empate en el promedio
        elif promedio_actual == mejor_promedio:
            # Comparamos nombres en minúsculas para cumplir la regla alfabética
            if nombre_actual.lower() < mejor_nombre.lower():
                mejor_nombre = nombre_actual
                
    return mejor_nombre



# --- CASO DE PRUEBA ---

# Estudiante A: Promedio 4.0
est1 = {"nombre": "Carlos", "matematicas": 4.0, "español": 4.0, "ciencias": 4.0, "literatura": 4.0, "arte": 4.0}

# Estudiante B: Promedio 4.4
est2 = {"nombre": "Ana", "matematicas": 4.5, "español": 4.2, "ciencias": 4.8, "literatura": 4.1, "arte": 4.5}

# Estudiante C: Promedio 4.4 (EMPATE con Ana)
est3 = {"nombre": "alberto", "matematicas": 4.0, "español": 5.0, "ciencias": 4.0, "literatura": 5.0, "arte": 4.0}

# Estudiante D: Promedio 3.0
est4 = {"nombre": "Zulema", "matematicas": 3.0, "español": 3.0, "ciencias": 3.0, "literatura": 3.0, "arte": 3.0}

# Estudiante E: Promedio 4.0
est5 = {"nombre": "Bernardo", "matematicas": 4.0, "español": 4.0, "ciencias": 4.0, "literatura": 4.0, "arte": 4.0}

# Ejecución de la función
ganador = mejor_del_salon(est1, est2, est3, est4, est5)

print(f"El mejor estudiante del salón es: {ganador}")

