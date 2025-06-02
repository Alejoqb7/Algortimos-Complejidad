def cambio_voraz(monedas, cantidad):
    monedas.sort(reverse=True) #Ordena de mayor a menor
    resultado = []

    for moneda in monedas:
        while cantidad >= moneda:
            cantidad -= moneda
            resultado.append(moneda)  # Usamos esta moneda

    return resultado  # Lista
