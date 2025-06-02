def super_digit(n, k):
    suma = sum(int(d) for d in n) * k  # Suma de dígitos inicial multiplicada por k

    while suma >= 10:
        suma = sum(int(d) for d in str(suma))  # Repite suma de dígitos hasta un solo dígito

    return suma
