
# palindrome reorder

def palindrome_reorder(n):
    # Verificar si n es una cadena de texto del alfabeto inglés y no supera 10^6
    if not isinstance(n, str) or len(n) > 10 ** 6:
        return "n debe ser una cadena de texto del alfabeto inglés y no superar 10^6"
    
    conteo_letras = {} # Contar las ocurrencias de cada letra en la cadena
    # Recorrer la cadena n y cuenta las ocurrencias de cada letra
    for letra in n:
        conteo_letras[letra] = conteo_letras.get(letra, 0) + 1
    
    # Construye la cadena resultante
    letra_impar = ""
    palindromo = ""
    # Recorre el diccionario conteo_letras y verifica si hay más de una letra con frecuencia impar
    for letra, count in conteo_letras.items():
        if count % 2 != 0:
            if letra_impar:
                # Si hay más de una letra con frecuencia impar, no es posible formar un palíndromo
                return "NO SOLUTION"
            # Se guarda la letra con frecuencia impar y se construye la mitad del palíndromo
            letra_impar = letra
        palindromo += letra * (count // 2)
    # Se retorna el palíndromo completo
    return palindromo + letra_impar + palindromo[::-1]

# Caso de prueba
assert palindrome_reorder("aabbc") == "abcba", "Error en el caso de prueba"
print(palindrome_reorder("aabbc"))