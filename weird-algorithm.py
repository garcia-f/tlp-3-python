# weird-algorithm

def weird_algorithm(n):
    # Realiza las validaciones necesarias para que el número ingresado sea un entero positivo 
    # y que no sobrepase el limite de 10^6
    if not isinstance(n, int):
        return "Error, debes ingresar un número entero"
    if n <= 0:
        return "Error, debes ingresar un número positivo"
    if  n > 10**6:
        return "Error, sobrepasa el límite de 10^6"

    secuencia = [n] # Crea una lista vacía donde se almacenará la secuencia de números
    # Mientras el número ingresado sea diferente de 1, se realizará el siguiente proceso
    while (n != 1):
        # Si el número es par, se divide entre 2
        if ((n % 2) == 0):
            n = n // 2
        # Si el número es impar, se multiplica por 3 y se le suma 1
        else:
            n = n * 3 + 1
        # Se añade el número a la lista
        secuencia.append(n)
    # Se retorna la lista con la secuencia de números
    return secuencia

# caso de prueba 
assert weird_algorithm(3) == [3, 10, 5, 16, 8, 4, 2, 1], "Error en el caso de prueba"

print(weird_algorithm(3))