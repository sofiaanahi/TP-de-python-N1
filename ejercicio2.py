# esta funcion busca el numero que falta
# se utiliza el metodo de Gauss para buscar el numero faltante 

def buscar_numero(cant_elem,n):
    
    
    total_cant_elem = (cant_elem*(cant_elem+1))//2 
    suma_n = sum(n)
    
    numero_faltante = total_cant_elem - suma_n   
    return numero_faltante
   
# se muestra el resultado
   
buscar_numero(5,[1,2,4,5])
print('el numero que falta es: ',buscar_numero(5,[1,2,4,5]))
assert buscar_numero(5, [1, 2, 4, 5]) == 3, "Error en el caso de prueba"

