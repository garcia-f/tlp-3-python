
# Number Spiral

def number_spiral(row, column):
    # Si la fila es mayor que la columna
    if row > column:
        if row % 2 == 0: # Si la fila es par 
            # Calculamos el valor en la posición fila, columna
            return row ** 2 - (column - 1)  # Como el cuadrado de la fila menos el número de columnas menos 1.
        
        else: # Si la fila es impar
            return (row - 1) ** 2 + 1 + (column - 1) # Calculamos el valor como el cuadrado de la fila anterior más 1 más el número de columnas menos 1.
        
    else: # Si la columna es mayor que la fila
        if column % 2 == 0: # Si la columna es par
            # Calculamos el valor en la posición fila, columna

            return (column - 1) ** 2 + 1 + (row - 1) # Como el cuadrado de la columna anterior mas 1 mas el número de filas menos 1.
        else: # Si la columna es impar

            return column ** 2 - (row - 1) # Calculamos el valor como el cuadrado de la columna menos el número de filas menos 1.

assert number_spiral(2, 2) == 3, "Error en el caso de prueba"
print("Todos los casos de prueba han pasado correctamente")