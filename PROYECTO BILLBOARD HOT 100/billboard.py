import csv

def cargar_canciones(nombre_archivo: str) -> list:
    canciones = []
    try:
        with open(nombre_archivo, mode='r', encoding='utf-8-sig') as archivo:
            # .strip() elimina espacios invisibles que suelen venir en archivos Excel
            lector = csv.DictReader(archivo)
            for fila in lector:
                # Usamos .get() para que si no encuentra 'Rank', no se bloquee el programa
                cancion = {
                    "posicion": int(fila.get("Rank", fila.get("rank", 0))),
                    "nombre_cancion": fila.get("Song", fila.get("song", "Sin nombre")),
                    "nombre_artista": fila.get("Artist", fila.get("artist", "Anónimo")),
                    "anio": int(fila.get("Year", fila.get("year", 0))),
                    "letra": fila.get("Lyrics", fila.get("lyrics", ""))
                }
                canciones.append(cancion)
    except Exception as e:
        print(f"Error al cargar: {e}")
    return canciones
def buscar_cancion(canciones: list, nombre_cancion: str, anio: int) -> dict:
    """ Busca una canción por nombre y año. """
    for cancion in canciones:
        if cancion["nombre_cancion"].lower() == nombre_cancion.lower() and cancion["anio"] == anio:
            return cancion
    return None

def consultar_canciones_anio(canciones: list, anio: int) -> list:
    """ Retorna canciones de un año (sin letra). """
    resultado = []
    for c in canciones:
        if c["anio"] == anio:
            info = c.copy()
            del info["letra"]
            resultado.append(info)
    return resultado

def consultar_canciones_artista_periodo(canciones: list, artista: str, anio_ini: int, anio_fin: int) -> list:
    """ Canciones de un artista en un rango de años. """
    resultado = []
    for c in canciones:
        if c["nombre_artista"].lower() == artista.lower() and anio_ini <= c["anio"] <= anio_fin:
            info = c.copy()
            del info["letra"]
            resultado.append(info)
    return resultado

def consultar_canciones_artista(canciones: list, artista: str) -> list:
    """ Todas las canciones de un artista. """
    resultado = []
    for c in canciones:
        if c["nombre_artista"].lower() == artista.lower():
            info = c.copy()
            del info["letra"]
            resultado.append(info)
    return resultado

def consultar_artistas_cancion(canciones: list, nombre_cancion: str) -> list:
    """ Artistas que han interpretado una canción específica. """
    artistas = []
    for c in canciones:
        if c["nombre_cancion"].lower() == nombre_cancion.lower():
            if c["nombre_artista"] not in artistas:
                artistas.append(c["nombre_artista"])
    return artistas

def artistas_mas_populares(canciones: list, minimo: int) -> dict:
    """ Artistas con más de 'minimo' apariciones. """
    conteos = {}
    for c in canciones:
        art = c["nombre_artista"]
        conteos[art] = conteos.get(art, 0) + 1
    return {art: cant for art, cant in conteos.items() if cant > minimo}

def artista_estrella(canciones: list) -> dict:
    """ El artista con más canciones en el ranking. """
    conteos = {}
    for c in canciones:
        art = c["nombre_artista"]
        conteos[art] = conteos.get(art, 0) + 1
    if not conteos: return {}
    nombre_max = max(conteos, key=conteos.get)
    return {nombre_max: conteos[nombre_max]}

def lista_artistas_canciones(canciones: list) -> dict:
    """ Diccionario de artistas y sus listas de canciones (únicas). """
    dicc = {}
    for c in canciones:
        art = c["nombre_artista"]
        nom = c["nombre_cancion"]
        if art not in dicc:
            dicc[art] = []
        if nom not in dicc[art]:
            dicc[art].append(nom)
    return dicc

def promedio_canciones_por_artista(canciones: list) -> float:
    """ Promedio de canciones únicas por cada artista único. """
    datos = lista_artistas_canciones(canciones)
    total_artistas = len(datos)
    if total_artistas == 0: return 0.0
    total_canciones_unicas = sum(len(lista) for lista in datos.values())
    return round(total_canciones_unicas / total_artistas, 2)