#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Ejercicio nivel 3: Billboard.
Interfaz basada en consola para la interacción con el usuario.
"""

import billboard as bb

def ejecutar_cargar_canciones() -> list:
    """Solicita al usuario que ingrese el nombre de un archivo CSV y carga los datos."""
    archivo = input("Por favor ingrese el nombre del archivo CSV con las canciones: ")
    canciones = bb.cargar_canciones(archivo)
    if len(canciones) == 0:
        print("El archivo seleccionado no es válido o está vacío.")
    else:
        print("Se cargaron", len(canciones), "canciones con éxito.")
    return canciones

def ejecutar_buscar_cancion(canciones: list) -> None:
    """Busca una canción por nombre y año."""
    nombre = input("Por favor ingrese el nombre de la canción que desea buscar: ")
    anio = int(input("Por favor ingrese el año de la canción que desea buscar: "))
    
    resultado = bb.buscar_cancion(canciones, nombre, anio)
    
    if resultado:
        print("\n--- Canción Encontrada ---")
        for llave, valor in resultado.items():
            print(f"{llave.capitalize()}: {valor}")
    else:
        print(f"\nNo se encontró la canción '{nombre}' en el año {anio}.")

def ejecutar_canciones_anio(canciones: list) -> None:
    """Consulta las canciones de un año específico."""
    anio = int(input("Por favor ingrese el año que desea consultar: "))
    lista = bb.consultar_canciones_anio(canciones, anio)
    
    if not lista:
        print(f"No hay registros para el año {anio}.")
    else:
        print(f"\n--- Ranking del año {anio} ---")
        for c in lista:
            print(f"#{c['posicion']} - {c['nombre_cancion']} ({c['nombre_artista']})")

def ejecutar_canciones_artista_periodo(canciones: list) -> None:
    """Consulta canciones de un artista en un rango de años."""
    artista = input("Por favor ingrese el nombre del artista que desea buscar: ")
    anio_inic = int(input("Por favor ingrese el año inicial: "))
    anio_fin = int(input("Por favor ingrese el año final: "))
    
    lista = bb.consultar_canciones_artista_periodo(canciones, artista, anio_inic, anio_fin)
    
    if not lista:
        print(f"No se encontraron canciones para {artista} en ese periodo.")
    else:
        print(f"\n--- Canciones de {artista} ({anio_inic}-{anio_fin}) ---")
        for c in lista:
            print(f"Año: {c['anio']} | {c['nombre_cancion']}")

def ejecutar_todas_canciones_artista(canciones: list) -> None:
    """Consulta toda la trayectoria de un artista en Billboard."""
    artista = input("Por favor ingrese el nombre del artista: ")
    lista = bb.consultar_canciones_artista(canciones, artista)
    
    if not lista:
        print(f"El artista {artista} no aparece en el listado.")
    else:
        print(f"\n--- Historial de {artista} ---")
        for c in lista:
            print(f"Año {c['anio']}: {c['nombre_cancion']}")

def ejecutar_todos_artistas_cancion(canciones: list) -> None:
    """Consulta quiénes han interpretado una canción específica."""
    nombre_c = input("Por favor ingrese el nombre de la canción: ")
    artistas = bb.consultar_artistas_cancion(canciones, nombre_c)
    
    if not artistas:
        print(f"Nadie ha interpretado la canción '{nombre_c}' según los registros.")
    else:
        print(f"\nArtistas que interpretaron '{nombre_c}':")
        print(", ".join(artistas))

def ejecutar_artistas_mas_populares(canciones: list) -> None:
    """Muestra artistas con un mínimo de éxitos."""
    minimo = int(input("Ingrese la cantidad mínima de canciones: "))
    populares = bb.artistas_mas_populares(canciones, minimo)
    
    if not populares:
        print(f"Ningún artista tiene más de {minimo} canciones.")
    else:
        print(f"\n--- Artistas con más de {minimo} éxitos ---")
        for art, cant in populares.items():
            print(f"{art}: {cant} canciones")

def ejecutar_artista_estrella(canciones: list) -> None:
    """Muestra al artista con más apariciones en la historia."""
    estrella = bb.artista_estrella(canciones)
    if not estrella:
        print("No hay datos cargados.")
    else:
        for nombre, cantidad in estrella.items():
            print(f"\nEl ARTISTA ESTRELLA es '{nombre}' con {cantidad} canciones.")

def ejecutar_artistas_y_sus_canciones(canciones: list) -> None:
    """Muestra el catálogo completo agrupado por artista."""
    dicc = bb.lista_artistas_canciones(canciones)
    print("\n--- Catálogo Completo por Artista ---")
    for artista, temas in dicc.items():
        print(f"{artista}: {', '.join(temas)}")

def ejecutar_promedio_canciones_por_artista(canciones: list) -> None:
    """Muestra el promedio estadístico de éxitos por artista."""
    promedio = bb.promedio_canciones_por_artista(canciones)
    print(f"\nEn promedio, cada artista tiene {promedio} canciones en el Billboard.")

# --- Funciones de control de flujo (se mantienen igual) ---

def mostrar_menu():
    print("\n" + "="*30)
    print("      MENU BILLBOARD")
    print("="*30)
    print("1. Cargar archivo CSV")
    print("2. Buscar una canción")
    print("3. Canciones de un año")
    print("4. Artista en un periodo")
    print("5. Todas las canciones de un artista")
    print("6. Artistas de una canción")
    print("7. Artistas más populares")
    print("8. Artista estrella")
    print("9. Lista completa artistas/canciones")
    print("10. Promedio de canciones por artista")
    print("11. Salir")

def iniciar_aplicacion():
    continuar = True
    canciones = []
    while continuar:
        mostrar_menu()
        try:
            opcion = int(input("\nSeleccione una opción: "))
            if opcion == 1: canciones = ejecutar_cargar_canciones()
            elif not canciones and opcion != 11:
                print("Primero debe cargar un archivo (Opción 1).")
            elif opcion == 2: ejecutar_buscar_cancion(canciones)
            elif opcion == 3: ejecutar_canciones_anio(canciones)
            elif opcion == 4: ejecutar_canciones_artista_periodo(canciones)
            elif opcion == 5: ejecutar_todas_canciones_artista(canciones)
            elif opcion == 6: ejecutar_todos_artistas_cancion(canciones)
            elif opcion == 7: ejecutar_artistas_mas_populares(canciones)
            elif opcion == 8: ejecutar_artista_estrella(canciones)
            elif opcion == 9: ejecutar_artistas_y_sus_canciones(canciones)
            elif opcion == 10: ejecutar_promedio_canciones_por_artista(canciones)
            elif opcion == 11: continuar = False
            else: print("Opción no válida.")
        except ValueError:
            print("Error: Ingrese un número válido.")

if __name__ == "__main__":
    iniciar_aplicacion()