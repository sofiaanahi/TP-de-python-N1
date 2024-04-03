# esta funcion verifica el lugar de la fila y columna
# para descubrir el valor de donde este posicionado el numero

def espiral_num(fila, columna):
    
    if fila == columna:
        return fila**2 - fila + 1
    
    if fila > columna:
        if fila % 2 == 0:
            return fila**2 - columna + 1
        else:
            return (fila - 1)**2 + columna
    else:
        if columna % 2 == 0:
            return (columna - 1)**2 + fila
        else:
            return columna**2 + 1 - fila
        
# se muestra el resultado 

print(' el valor de la posicion es: ',espiral_num(2,2))
    
assert espiral_num(2, 2) == 3, "Error en el caso de prueba"
    
    
    
    
    
    
    
    
    