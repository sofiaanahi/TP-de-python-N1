# en esta funcion se realiza la validacion de la variable n 
def validar_n(n):
    while True:
        try:
            if 1 < n < 10**6:
                return n
            else:
                n = int(input('por favor, ingrese un numero que sea mayor a 1 y menor 10^6: '))  
        except ValueError:
            print('ingrese un numero valido.')

# cuando la variable sea valida, recien pasa a la segunda funcion
# en esta funcion se demuestra si la varible es par o impar para realizar cada condicion 

def numero_par_impar(n):
    ans = []
    ans.append(n)
    
    while n != 1:            
        if n % 2 == 0:
            n = n // 2
            ans.append(n)
        else:
            n = n * 3 + 1    
            ans.append(n)   
           
    return ans

n = int(input('escribe un valor numerico: '))    
n = validar_n(n)

# se muestra el resultado

resultado = numero_par_impar(n)                             
print('resultado generado: ',resultado)

assert numero_par_impar(3) == [3, 10, 5, 16, 8, 4, 2, 1], "Error en el caso de prueba"