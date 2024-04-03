# en esta funcion se realiza la validacion de la variable n 
def validar_n(n):
    # se controla que los datos sean validos
    while True:
            if 1 < n < 10**6:
                return n
            else:
                print('error')
                
# cuando la variable sea valida, recien pasa a la segunda funcion

# en esta funcion se demuestra si la varible es par o impar para realizar cada condicion 

def numero_par_impar(n):
    ans = []
    ans.append(n)
     
    # se realiza la condicion para saber si el numero es par o impar
    while n != 1:            
        if n % 2 == 0:
            n = n // 2
            ans.append(n)
        else:
            n = n * 3 + 1    
            ans.append(n)   
           
    return ans

# caso de prueba
assert numero_par_impar(3) == [3, 10, 5, 16, 8, 4, 2, 1], "Error en el caso de prueba"

print('todos los casos de pruba han pasado correctamente.')