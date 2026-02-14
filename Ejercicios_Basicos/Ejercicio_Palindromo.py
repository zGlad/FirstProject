
def clasificar_regalo(id:int)-> str: 
    """
    Clasifica un regalo según su ID numérico.
    
    Args:
        id (int): Identificador único entre 100 y 999.
        
    Returns:
        str: Categoría del destinatario ('boy', 'girl', 'man', 'woman').
    """
    # Verificamos las dos condiciones base
    es_Palindromo = str(id) == str(id)[::-1]
    es_Par = id % 2 == 0
        
    # Aplicamos la matriz de decisión
    if es_Palindromo and es_Par:
        return "boy" 
    
    if es_Palindromo and not es_Par: 
        return "girl"
    
    if not es_Palindromo and es_Par: 
        return "man"
    
    if not es_Palindromo and not es_Par:
        return "woman"
    
    
# Test c
print (clasificar_regalo(121)) # girl 
print (clasificar_regalo(100)) # man
print (clasificar_regalo(709)) # woman
print (clasificar_regalo(666)) # boy
        
    
        
    

    
    
    