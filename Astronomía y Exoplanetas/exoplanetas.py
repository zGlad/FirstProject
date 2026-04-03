import pandas as pd
import matplotlib.pyplot as plt
import math as m
import numpy as np

plt.rcParams.update({'font.size': 12})

def cargar_datos(nombre_archivo:str)->pd.DataFrame:
    """ Carga los datos de un archivo csv y retorna el DataFrame con la informacion.
    Parametros:
        nombre_archivo (str): El nombre del archivo CSV que se debe cargar
    Retorno:
        (DataFrame) : El DataFrame con todos los datos contenidos en el archivo
    """
    return pd.read_csv(nombre_archivo)


def histograma_descubrimiento(datos:pd.DataFrame)->None:
    """ Calcula y despliega un histograma con 30 grupos (bins) en el que debe
        aparecer la cantidad de planetas descubiertos por anho.
    Parametros:
        datos (DataFrame): el DataFrame con la informacion de los exoplanetas
    """
    plt.figure(figsize=(8, 6))
    plt.hist(datos['DESCUBRIMIENTO'].dropna(), bins=30)
    plt.title('Cantidad de planetas descubiertos')
    plt.xlabel('Años')
    plt.ylabel('Cantidad de planetas descubiertos')
    plt.show()

def estado_publicacion_por_descubrimiento(datos:pd.DataFrame)->None:
    """ Calcula y despliega un BoxPlot donde aparecen la cantidad de planetas
        descubiertos por anho, agrupados de acuerdo con el tipo de publicacion.
    Parametros:
        datos (DataFrame): el DataFrame con la informacion de los exoplanetas
    """
    datos.boxplot(column='DESCUBRIMIENTO', by='ESTADO_PUBLICACION', rot=90, figsize=(8,8))
    plt.title('Tipo de publicación vs año de descubrimiento')
    plt.xlabel('Tipo de publicación')
    plt.ylabel('Año de descubrimiento')
    plt.suptitle('') # Elimina el titulo automatico extra que genera pandas
    plt.show()

def deteccion_por_descubrimiento(datos:pd.DataFrame)->None:
    """ Calcula y despliega un BoxPlot donde aparecen la cantidad de planetas
        descubiertos por anho, agrupados de acuerdo con el tipo de deteccion
    Parametros:
        datos (DataFrame): el DataFrame con la informacion de los exoplanetas
    """
    datos.boxplot(column='DESCUBRIMIENTO', by='TIPO_DETECCION', rot=90, figsize=(8,8))
    plt.title('Tipo de detección vs año de descubrimiento')
    plt.xlabel('Tipo de detección')
    plt.ylabel('Año de descubrimiento')
    plt.suptitle('')
    plt.show()

def deteccion_y_descubrimiento(datos:pd.DataFrame,anho:int)->None:
    """ Calcula y despliega un diagrama de pie donde aparecen la cantidad de
        planetas descubiertos en un anho particular, clasificados de acuerdo
        con el tipo de detección.
        Si el anho es 0, se muestra la información para todos los planetas.
    Parametros:
        datos (DataFrame): el DataFrame con la informacion de los exoplanetas
        anho (int): el anho para el que se quieren analizar los planetas descubiertos
                    o 0 para indicar que deben ser todos los planetas.
    """
    if anho == 0:
        df_filtrado = datos
        titulo = 'Tipos de detección en todos los años'
    else:
        df_filtrado = datos[datos['DESCUBRIMIENTO'] == anho]
        titulo = f'Tipos de detección en el año {anho}'

    conteo = df_filtrado['TIPO_DETECCION'].value_counts()
    
    plt.figure(figsize=(8, 8))
    plt.pie(conteo, labels=conteo.index, autopct='%1.1f%%')
    plt.title(titulo)
    plt.show()

def cantidad_y_tipo_deteccion(datos:pd.DataFrame)->None:
    """ Calcula y despliega un diagrama de lineas donde aparece una linea por
        cada tipo de deteccion y se muestra la cantidad de planetas descubiertos
        en cada anho, para ese tipo de deteccion.
    Parametros:
        datos (DataFrame): el DataFrame con la informacion de los exoplanetas
    """
    # Se agrupan los datos por tipo de detección y luego por año
    conteo = datos.groupby(['TIPO_DETECCION', 'DESCUBRIMIENTO']).size()
    tipos = datos['TIPO_DETECCION'].dropna().unique()
    
    # Se construye el diccionario con las series
    diccionario = {}
    for tipo in tipos:
        if tipo in conteo:
            diccionario[tipo] = conteo[tipo]
            
    df_plot = pd.DataFrame(diccionario)
    df_plot.plot(kind='line', figsize=(10, 6))
    plt.title('Cantidad de planetas descubiertos según el tipo de detección')
    plt.xlabel('Año de descubrimiento')
    plt.ylabel('Cantidad de planetas')
    plt.legend(title='')
    plt.show()


def masa_promedio_y_tipo_deteccion(datos:pd.DataFrame)->None:
    """ Calcula y despliega un diagrama de lineas donde aparece una linea por
        cada tipo de detección y se muestra la masa promedio de los planetas descubiertos
        en cada anho, para ese tipo de deteccion.
    Parametros:
        datos (DataFrame): el DataFrame con la informacion de los exoplanetas
    """
    promedio = datos.groupby(['TIPO_DETECCION', 'DESCUBRIMIENTO'])['MASA'].mean()
    tipos = datos['TIPO_DETECCION'].dropna().unique()
    
    diccionario = {}
    for tipo in tipos:
        if tipo in promedio:
            diccionario[tipo] = promedio[tipo]
            
    df_plot = pd.DataFrame(diccionario)
    df_plot.plot(kind='line', figsize=(10, 6))
    plt.title('Masa promedio de los planetas según el tipo de detección')
    plt.xlabel('Año de descubrimiento')
    plt.ylabel('Masa promedio')
    plt.legend(title='')
    plt.show()


def masa_planetas_vs_masa_estrellas(datos: pd.DataFrame)->None:
    """ Calcula y despliega un diagrama de dispersión donde en el eje x se
        encuentra la masa de los planetas y en el eje y se encuentra el logaritmo
        de la masa de las estrellas.
    Parametros:
        datos (DataFrame): el DataFrame con la informacion de los exoplanetas
    """
    plt.figure(figsize=(8, 6))
    plt.scatter(datos['MASA'], datos['MASA_ESTRELLA'], marker='.')
    plt.yscale('log')
    plt.title('Masa de los planetas vs. masa de la estrella más cercana')
    plt.xlabel('Masa del planeta')
    plt.ylabel('Masa de la estrella (log)')
    plt.show()


def graficar_cielo(datos:pd.DataFrame)->list:
    """ Calcula y despliega una imagen donde aparece un pixel por cada planeta,
        usando colores diferentes que dependen del tipo de detección.
    Parametros:
        datos (DataFrame): el DataFrame con la informacion de los exoplanetas
    Retorno:
        Una matriz de pixeles con la representacion del cielo
    """
    # Matriz inicial de pixeles color negro (100 filas x 200 columnas)
    imagen = [[[0.0, 0.0, 0.0] for _ in range(200)] for _ in range(100)]
    
    colores_rgb = {
        "Microlensing": [0.94, 0.10, 0.10],
        "Radial Velocity": [0.10, 0.50, 0.94],
        "Imaging": [0.34, 0.94, 0.10],
        "Primary Transit": [0.10, 0.94, 0.85],
        "Other": [0.94, 0.10, 0.85],
        "Astrometry": [0.94, 0.65, 0.10],
        "TTV": [1.0, 1.0, 1.0]
    }

    for index, row in datos.iterrows():
        ra = row['RA']
        dec = row['DEC']
        tipo = row['TIPO_DETECCION']

        # Omitimos datos incompletos
        if pd.isna(ra) or pd.isna(dec) or pd.isna(tipo):
            continue

        if tipo in colores_rgb:
            color = colores_rgb[tipo]
            
            # Ecuaciones para posicion del planeta
            fila_p = 99 - int(abs(m.sin(ra) * m.cos(dec) * 100))
            columna_p = int(m.cos(ra) * m.cos(dec) * 100) + 100
            
            # Evitar desbordes de índice
            fila_p = max(0, min(99, fila_p))
            columna_p = max(0, min(199, columna_p))
            
            imagen[fila_p][columna_p] = color

    plt.figure(figsize=(10, 5))
    plt.imshow(imagen)
    plt.show()
    return imagen


def filtrar_imagen_cielo(imagen:list)->None:
    """ Le aplica a la imagen un filtro de convolucion basado en la matriz predefinida.
    Parametros:
        imagen (list): una matriz con la imagen del cielo
    """
    filas = len(imagen)
    columnas = len(imagen[0])
    # Matriz vacía para evitar superponer valores filtrados
    nueva_imagen = [[[0.0, 0.0, 0.0] for _ in range(columnas)] for _ in range(filas)]
    
    mascara = [[-1, -1, -1],
               [-1,  9, -1],
               [-1, -1, -1]]

    # Aplicamos la convolución excluyendo los bordes para simplificar y evitar errores
    for i in range(1, filas - 1):
        for j in range(1, columnas - 1):
            for canal in range(3): # Recorrer R, G y B
                suma_convolucion = 0.0
                for mi in range(3):
                    for mj in range(3):
                        pixel_original = imagen[i - 1 + mi][j - 1 + mj][canal]
                        peso_mascara = mascara[mi][mj]
                        suma_convolucion += pixel_original * peso_mascara
                
                # Asegurar que el color resultante no sobrepase los límites RGB (0.0 a 1.0)
                nueva_imagen[i][j][canal] = max(0.0, min(1.0, suma_convolucion))

    plt.figure(figsize=(10, 5))
    plt.imshow(nueva_imagen)
    plt.show()