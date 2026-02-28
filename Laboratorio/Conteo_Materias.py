def conteo_de_materias(nombre_materia_1: str, nombre_materia_2: str, nombre_materia_3: str) -> int:
    """
    Cuenta cuántas de las materias inscritas coinciden con las áreas de interés (favoritas).
    
    La función busca palabras clave como 'programacion' o 'matematica' dentro de nombres 
    más largos de materias, sin importar si están en mayúsculas o minúsculas.

    Args:
        nombre_materia_1 (str): Nombre de la primera materia.
        nombre_materia_2 (str): Nombre de la segunda materia.
        nombre_materia_3 (str): Nombre de la tercera materia.

    Returns:
        int: Cantidad total de coincidencias encontradas (máximo 3).
    """
    
    # Inicializamos el acumulador de coincidencias
    contador = 0 
    
    # Agrupamos los argumentos en una lista para facilitar la iteración
    materias = [nombre_materia_1, nombre_materia_2, nombre_materia_3]
    
    # Lista de palabras clave que definen si una materia nos gusta
    favoritas = ['programacion', 'matematica', 'filosofia', 'literatura']
    
    # Primer bucle: Recorremos cada una de las materias inscritas
    for materia in materias: 
        # Convertimos a minúsculas para asegurar que la comparación sea efectiva
        # (ej: 'Matemática' ahora será tratada como 'matematica')
        materia_min = materia.lower()    
            
        # Segundo bucle (Anidado): Comparamos cada palabra favorita contra el nombre de la materia
        for fav in favoritas: 
            # Verificamos si la palabra clave 'fav' existe dentro de la cadena 'materia_min'
            if fav in materia_min: 
                contador += 1
                # Si encontramos una coincidencia, pasamos a la siguiente materia 
                # para evitar contar dos veces la misma asignatura
                break
                
    return contador      
        
# Prueba 
print(conteo_de_materias(
    "introduccion a las ciencias naturales", # NO
    "matematica discreta",                   # SI
    "algoritmica y programacion orientada por objetos I" # SI
))