
# Missing Number

def missing_number(n, lista):

    suma_total = 0 # Inicializamos la suma total de la secuencia, de 1 hasta n

    # Calculamos la suma de la secuencia 
    for i in range(1, n + 1): # Recorremos la lista de 1 hasta n
        suma_total  += i # Sumamos el valor de la lista

    suma_lista = sum(lista)
    return suma_total - suma_lista # Retornamos la suma total de la secuencia menos la suma de la lista

# Caso de prueba
assert missing_number(5, [1, 2, 4, 5 ]) == 3, "Error en el caso de prueba"
print("Todos los casos de prueba han pasado correctamente")