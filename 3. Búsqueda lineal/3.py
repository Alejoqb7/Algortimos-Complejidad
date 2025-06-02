def busqueda_lineal(lista, objetivo):
    for i in range(len(lista)):
        if lista[i] == objetivo:  # Compara cada elemento con el objetivo
            return i              # Retorna la posición si lo encuentra
    return -1                     # Retorna -1 si no está en la lista
