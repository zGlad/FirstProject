def contar_caracteres_repetidos(cadena:str)->int: 
    
    # Convertimos la cadena en minusculas para evitar errores
    minus = cadena.lower() 
    
    vistas = []
    repetidas = []
    
    for letra in minus: 
        if letra in vistas and letra not in repetidas:
            repetidas.append(letra)
        
        vistas.append(letra)
        
    print (vistas)
    print (repetidas)
            
    return len(repetidas)
print(contar_caracteres_repetidos("Albuquerque"))