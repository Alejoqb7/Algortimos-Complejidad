def mochila(valores, pesos, capacidad):
    n = len(valores)

    tabla = [[0] * (capacidad + 1) for _ in range(n + 1)]

    # Llenamos la tabla comparando incluir o no cada objeto
    for i in range(1, n + 1):
        for w in range(capacidad + 1):
            sin_item = tabla[i - 1][w]  # Aún no se incluye el objeto
            con_item = 0
            if pesos[i - 1] <= w:
                con_item = valores[i - 1] + tabla[i - 1][w - pesos[i - 1]]  # Incluir el objeto
            tabla[i][w] = max(sin_item, con_item)  # mjor opción

    # Buscamos qué objetos fueron seleccionados
    seleccionados = []
    w = capacidad
    for i in range(n, 0, -1):
        if tabla[i][w] != tabla[i - 1][w]:  # Si el valor cambió, ese objeto fue usado
            seleccionados.append(i - 1)     # Guardamos el índice del objeto
            w -= pesos[i - 1]               # se reduce la capacidad restante

    seleccionados.reverse()  # aquí se invierte agregando de atrás pa delante
    return tabla[n][capacidad], seleccionados  # Valor total y lista de objetos usados
