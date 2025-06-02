def factorial_iterativo(n):
    resultado = 1
    for i in range(2, n + 1):
        resultado *= i
    return resultado

def factorial_recursivo(n):
    if n == 0:
        return 1
    return n * factorial_recursivo(n - 1)

#no hay mucho que decir...