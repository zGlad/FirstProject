"""
Ejercicio nivel 2: Agenda de peliculas.
Módulo de cálculos.

Temas:
* Variables.
* Tipos de datos.
* Expresiones aritmeticas.
* Instrucciones basicas y consola.
* Dividir y conquistar: funciones y paso de parametros.
* Especificacion y documentacion.
* Instrucciones condicionales.
* Diccionarios.
@author: Cupi2

NOTA IMPORTANTE PARA TENER EN CUENTA EN TODAS LAS FUNCIONES DE ESTE MODULO:
        Los diccionarios de pelicula tienen las siguientes parejas de clave-valor:
            - nombre (str): Nombre de la pelicula agendada.
            - genero (str): Generos de la pelicula separados por comas.
            - duracion (int): Duracion en minutos de la pelicula
            - anio (int): Anio de estreno de la pelicula
            - clasificacion (str): Clasificacion de restriccion por edad
            - hora (int): Hora de inicio de la pelicula
            - dia (str): Indica que día de la semana se planea ver la película
"""

def crear_pelicula(nombre: str, genero: str, duracion: int, anio: int, 
                clasificacion: str, hora: int, dia: str) -> dict:
    """Crea un diccionario que representa una nueva película con toda su información 
    inicializada.
    Parámetros:
        nombre (str): Nombre de la pelicula agendada.
        genero (str): Generos de la pelicula separados por comas.
        duracion (int): Duracion en minutos de la pelicula
        anio (int): Anio de estreno de la pelicula
        clasificacion (str): Clasificacion de restriccion por edad
        hora (int): Hora a la cual se planea ver la pelicula, esta debe estar entre 
                    0 y 2359
        dia (str): Dia de la semana en el cual se planea ver la pelicula.
    Retorna:
        dict: Diccionario con los datos de la pelicula
    """     
    # Crear diccionario con los datos de la pelicula
    pelicula = { 
                "nombre" : nombre,
                "genero" : genero,
                "duracion" : duracion,
                "anio" : anio,
                "clasificacion" : clasificacion,
                "hora" : hora,
                "dia" : dia}
    return pelicula
    
    


def encontrar_pelicula(nombre_pelicula: str, p1: dict, p2: dict, p3: dict, p4: dict,  p5: dict) -> dict:
    """Encuentra en cual de los 5 diccionarios que se pasan por parametro esta la 
    pelicula cuyo nombre es dado por parametro.
    Si no se encuentra la pelicula se debe retornar None.
    Parametros:
        nombre_pelicula (str): El nombre de la pelicula que se desea encontrar.
        p1 (dict): Diccionario que contiene la informacion de la pelicula 1.
        p2 (dict): Diccionario que contiene la informacion de la pelicula 2.
        p3 (dict): Diccionario que contiene la informacion de la pelicula 3.
        p4 (dict): Diccionario que contiene la informacion de la pelicula 4.
        p5 (dict): Diccionario que contiene la informacion de la pelicula 5.
    Retorna:
        dict: Diccionario de la pelicula cuyo nombre fue dado por parametro. 
        None si no se encuentra una pelicula con ese nombre.
    """
    # Buscamos la pelicula en cada diccionario por medio de su nombre
    if nombre_pelicula == p1["nombre"]:
        return p1
    elif nombre_pelicula == p2["nombre"]:
        return p2
    elif nombre_pelicula == p3["nombre"]:
        return p3
    elif nombre_pelicula == p4["nombre"]:
        return p4
    elif nombre_pelicula == p5["nombre"]:
        return p5
    
    return None

def encontrar_pelicula_mas_larga(p1: dict, p2: dict, p3: dict, p4: dict, p5: dict) -> dict:
    """Encuentra la pelicula de mayor duracion entre las peliculas recibidas por
    parametro.
    Parametros:
        p1 (dict): Diccionario que contiene la informacion de la pelicula 1.
        p2 (dict): Diccionario que contiene la informacion de la pelicula 2.
        p3 (dict): Diccionario que contiene la informacion de la pelicula 3.
        p4 (dict): Diccionario que contiene la informacion de la pelicula 4.
        p5 (dict): Diccionario que contiene la informacion de la pelicula 5.
    Retorna:
        dict: El diccionario de la pelicula de mayor duracion
    """
    MasLarga = p1

    # Comparamos duraciones para encontrar la mas larga
    if p2["duracion"] > MasLarga["duracion"]: 
        MasLarga = p2 # Si p2 es más larga, ella es el nuevo mas larga
        
    if p3["duracion"] > MasLarga["duracion"]: 
        MasLarga = p3
        
    # 4. Comparamos contra p4
    if p4["duracion"] > MasLarga["duracion"]: 
        MasLarga = p4
        
    # 5. Comparamos contra p5
    if p5["duracion"] > MasLarga["duracion"]: 
        MasLarga = p5
    return MasLarga


def duracion_promedio_peliculas(p1: dict, p2: dict, p3: dict, p4: dict, p5: dict) -> str:
    """Calcula la duracion promedio de las peliculas que entran por parametro. 
    Esto es, la duración total de todas las peliculas dividida sobre el numero de peliculas. 
    Retorna la duracion promedio en una cadena de formato 'HH:MM' ignorando los posibles decimales.
    Parametros:
        p1 (dict): Diccionario que contiene la informacion de la pelicula 1.
        p2 (dict): Diccionario que contiene la informacion de la pelicula 2.
        p3 (dict): Diccionario que contiene la informacion de la pelicula 3.
        p4 (dict): Diccionario que contiene la informacion de la pelicula 4.
        p5 (dict): Diccionario que contiene la informacion de la pelicula 5.
    Retorna:
        str: la duracion promedio de las peliculas en formato 'HH:MM'
    """
    # 1. Obtenemos la duracion promedio
    sumaTotal = p1["duracion"] + p2["duracion"] + p3["duracion"] + p4["duracion"] + p5["duracion"]
    promedio = int(sumaTotal/5)
    
    # 2. Convertimos la duracion promedio a horas y minutos
    horas = promedio // 60 
    minutos = promedio % 60
    
    # 3. Devolvemos la duracion promedio
    return f" {horas:02d}:{minutos:02d}"

def encontrar_estrenos(p1: dict, p2: dict, p3: dict, p4: dict, p5: dict, anio: int) -> str:
    """Busca entre las peliculas cuales tienen como anio de estreno una fecha estrictamente
    posterior a la recibida por parametro.
    Parametros:
        p1 (dict): Diccionario que contiene la informacion de la pelicula 1.
        p2 (dict): Diccionario que contiene la informacion de la pelicula 2.
        p3 (dict): Diccionario que contiene la informacion de la pelicula 3.
        p4 (dict): Diccionario que contiene la informacion de la pelicula 4.
        p5 (dict): Diccionario que contiene la informacion de la pelicula 5.
        anio (int): Anio limite para considerar la pelicula como estreno.
    Retorna:
        str: Una cadena con el nombre de la pelicula estrenada posteriormente a la fecha recibida. 
        Si hay mas de una pelicula, entonces se retornan los nombres de todas las peliculas 
        encontradas separadas por comas. Si ninguna pelicula coincide, retorna "Ninguna".
    """
    # Creamos una lista con todas las peliculas
    peliculas = [p1, p2, p3, p4, p5]
    # Creamos una lista con las peliculas encontradas
    peliculas_encontradas = []
    
    for pelicula in peliculas:
        # Si la pelicula tiene un anio posterior al recibido
        if pelicula["anio"] > anio:
            # Lo agregamos a la lista
            peliculas_encontradas.append(pelicula["nombre"])
            
    if len(peliculas_encontradas) > 0:
        # retornamos las peliculas encontradas separadas por comas
        return ", ".join(peliculas_encontradas  )
    
    return "Ninguna"

def cuantas_peliculas_18_mas(p1: dict, p2: dict, p3: dict, p4: dict, p5: dict) -> int:
    """Indica cuantas peliculas de clasificación '18+' hay entre los diccionarios recibidos.
    Parametros:
        p1 (dict): Diccionario que contiene la informacion de la pelicula 1.
        p2 (dict): Diccionario que contiene la informacion de la pelicula 2.
        p3 (dict): Diccionario que contiene la informacion de la pelicula 3.
        p4 (dict): Diccionario que contiene la informacion de la pelicula 4.
        p5 (dict): Diccionario que contiene la informacion de la pelicula 5.
    Retorna:
        int: Numero de peliculas con clasificacion '18+'
    """
    # 1. Recorremos todas las peliculas
    contador = 0
    peliculas = [p1, p2, p3, p4, p5]
    
    for pelicula in peliculas:
        # 2. Verificamos si la pelicula es de 18+
        if pelicula["clasificacion"] == '18+':
            contador += 1
            
    # 3. Retornamos el contador
    return contador
    return 0 
        


def reagendar_pelicula(peli:dict, nueva_hora: int, nuevo_dia: str, 
                    control_horario: bool, p1: dict, p2: dict, p3: dict, p4: dict, p5: dict)->bool: 
        """Verifica si es posible reagendar la pelicula que entra por parametro. Para esto verifica
        si la nueva hora y el nuevo dia no entran en conflicto con ninguna otra pelicula, 
        y en caso de que el usuario haya pedido control horario verifica que se cumplan 
        las restricciones correspondientes.
        Parametros:
            peli (dict): Pelicula a reagendar
            nueva_hora (int): Nueva hora a la cual se quiere ver la pelicula
            nuevo_dia (str): Nuevo dia en el cual se quiere ver la pelicula
            control_horario (bool): Representa si el usuario quiere o no controlar
                                    el horario de las peliculas.
            p1 (dict): Diccionario que contiene la informacion de la pelicula 1.
            p2 (dict): Diccionario que contiene la informacion de la pelicula 2.
            p3 (dict): Diccionario que contiene la informacion de la pelicula 3.
            p4 (dict): Diccionario que contiene la informacion de la pelicula 4.
            p5 (dict): Diccionario que contiene la informacion de la pelicula 5.
        Retorna:
            bool: True en caso de que se haya podido reagendar la pelicula, False de lo contrario.
        """
        # Para verificar si es posible reagendar, se deben cumplir la siguiente condicion:
        # La nueva hora y el nuevo dia no coincidan con la hora y el dia de otra pelicula
        
        existentes = [p1, p2, p3, p4, p5]
    # 1. Reglas de Control Horario
        if control_horario:
        # Madrugada
            if 0 <= nueva_hora < 6: 
                return False
        # Siesta/Almuerzo
            if 12 <= nueva_hora < 14:
                return False
        # Lunes prohibido
            if nuevo_dia.lower() == "lunes":
                return False
            
    # 2. Verificar conflicto con las demás
        for existente in existentes:
        # Importante: No chocar con uno mismo usando el nombre como ID
            if peli["nombre"] != existente["nombre"]:
                if nueva_hora == existente["hora"] and nuevo_dia.lower() == existente["dia"].lower():
                    return False 
    
    # 3. Éxito: Actualizamos el diccionario original
        peli["hora"] = nueva_hora
        peli["dia"] = nuevo_dia
        return True
    
    
    
    
    
    
    
    
    
def decidir_invitar(peli: dict, edad_invitado: int, autorizacion_padres: bool)->bool:
    """Verifica si es posible invitar a la persona cuya edad entra por parametro a ver la 
    pelicula que entra igualmente por parametro. 
    Para esto verifica el cumplimiento de las restricciones correspondientes.
    Parametros:
        peli (dict): Pelicula que se desea ver con el invitado
        edad_invitado (int): Edad del invitado con quien se desea ver la pelicula
        autorizacion_padres (bool): Indica si el invitado cuenta con la autorizacion de sus padres 
        para ver la pelicula
    Retorna:
        bool: True en caso de que se pueda invitar a la persona, False de lo contrario.
    """
    # Verificamos si la edad del invitado es mayor o igual a 18 o si tiene autorizacion de sus padres
    if edad_invitado >= 18 or autorizacion_padres:
        return True
    
    # En cualquier otro caso (menor sin permiso), es False.
    return False









