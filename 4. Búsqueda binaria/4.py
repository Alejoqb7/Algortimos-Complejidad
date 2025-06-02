def busqueda_binaria(lista, objetivo):
    izquierda, derecha = 0, len(lista) - 1

    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if lista[medio] == objetivo:
            return medio                    # Cuando encuentre algún elemento
        elif lista[medio] < objetivo:
            izquierda = medio + 1           # Buscar en la mitad derecha
        else:
            derecha = medio - 1             # Buscar en la mitad izquierda

    return -1
