def es_palindromo(n):
    n_str = str(n)
    return n_str == n_str[::-1]  # Compara el número con su forma "invertida"
