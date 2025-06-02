import heapq  # Para usar una cola de prioridad (min-heap)

def dijkstra(grafo, inicio):
    distancias = {nodo: float('inf') for nodo in grafo} #como siempre, se inician estas instancias en ∞
    distancias[inicio] = 0  # La distancia al nodo de inicio es 0

    visitados = set()
    cola = [(0, inicio)]  #distancia, nodo

    while cola:
        actual_dist, actual_nodo = heapq.heappop(cola)  # Nodo más cercano

        if actual_nodo in visitados:
            continue

        visitados.add(actual_nodo)

        for vecino, peso in grafo[actual_nodo]:
            nueva_dist = actual_dist + peso  # Distancia acumulada hasta el vecino

            if nueva_dist < distancias[vecino]:
                distancias[vecino] = nueva_dist  # Mejor camino encontrado
                heapq.heappush(cola, (nueva_dist, vecino))

    return distancias  # Diccionario
