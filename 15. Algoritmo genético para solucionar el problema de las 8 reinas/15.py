import random

def generar_individuo():
    return [random.randint(0, 7) for _ in range(8)]

def evaluar(individuo):
    ataques = 0
    for i in range(8):
        for j in range(i + 1, 8):
            if individuo[i] == individuo[j] or abs(individuo[i] - individuo[j]) == abs(i - j):
                ataques += 1  # Mismo fila o misma diagonal
    return ataques  # 0 ataques = solución válida

def cruzar(p1, p2):
    corte = random.randint(1, 6)
    return p1[:corte] + p2[corte:]  # Mezcla de padres

def mutar(individuo, prob=0.3):
    if random.random() < prob:
        i = random.randint(0, 7)
        individuo[i] = random.randint(0, 7)  # para cambiar fila aleatoria
    return individuo

def resolver_8_reinas():
    poblacion = [generar_individuo() for _ in range(80)]
    generacion = 0

    while True:
        generacion += 1
        poblacion.sort(key=evaluar)
        mejor = poblacion[0]

        if evaluar(mejor) == 0:
            print(f"Solución encontrada en la generación {generacion}")
            print("Tablero (columna: fila):")
            for col, fila in enumerate(mejor):
                print(f"{col}: {fila}")
            return mejor

        nueva_gen = poblacion[:10] #sobreviven diez individuos 
        while len(nueva_gen) < 80:
            p1, p2 = random.sample(nueva_gen, 2)
            hijo = cruzar(p1, p2)
            hijo = mutar(hijo)
            nueva_gen.append(hijo)

        poblacion = nueva_gen
