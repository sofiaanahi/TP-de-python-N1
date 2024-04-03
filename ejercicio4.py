def ordenar_palindrome(n):
    
    set_letras = set(n) # elimina las repiticiones de letras
    set_letras = sorted(set_letras, reverse=True) # ordena las letras de forma descendente
    
    palidromo = [] # se crea una lista vacia para los valores del palindromo
    letra_impar = [] 
    # se crea un for que recorre las letras
    for letra in set_letras:
        count = n.count(letra)
       
    # se verifica si el recuento de las letras es par o impar
        if count % 2 == 0:
            
            for _ in range(count//2):
                # se inserta la letra  al principio y al final en la lista
                palidromo.insert(0,letra)
                palidromo.append(letra)
    
        else:
            # si es impar la letra se retorna esto
            if letra_impar:
                return 'NO SOLUTION' 
            
            palidromo.insert(len(palidromo) // 2,letra)
            letra_impar = True

    return ''.join(palidromo)

# caso de prueba
assert ordenar_palindrome("aabbc") == "abcba", "Error en el caso de prueba"

print('todos los casos de pruba han pasado correctamente.')  