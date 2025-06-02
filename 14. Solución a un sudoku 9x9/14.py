def sudoku_valido(celda, fila, col, num):
    # Revisa si el número ya está en la fila o en la columna
    if num in celda[fila] or any(celda[i][col] == num for i in range(9)):
        return False

    # Revisa si el número ya está en el bloque 3x3 correspondiente
    f0, c0 = fila // 3 * 3, col // 3 * 3  # Coordenadas del inicio del bloque
    for i in range(f0, f0 + 3):
        for j in range(c0, c0 + 3):
            if celda[i][j] == num:
                return False

    return True

def completar_sudoku(celda):
    for f in range(9):
        for c in range(9):
            if celda[f][c] == 0:  # para encontrar una celda vacía
                for valor in range(1, 10):  # Prueba valores del 1 al 9
                    if sudoku_valido(celda, f, c, valor):
                        celda[f][c] = valor
                        if completar_sudoku(celda):  # Intenta resolver lo que sigue
                            return True
                        celda[f][c] = 0  # Vuelve atrás si no funciona
                return False
    return True
