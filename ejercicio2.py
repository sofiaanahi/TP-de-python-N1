# esta funcion busca el numero que falta

def buscar_numero(cant_elem,n):
    # se utiliza el metodo de Gauss para buscar el numero faltante 
    
    total_cant_elem = (cant_elem*(cant_elem+1))//2 
    suma_n = sum(n)
    
    # se hace la resta para saber cual es el numero faltante
    numero_faltante = total_cant_elem - suma_n   
   
    return numero_faltante
   
# caso de prueba
assert buscar_numero(5, [1, 2, 4, 5]) == 3, "Error en el caso de prueba"

print('todos los casos de pruba han pasado correctamente.')