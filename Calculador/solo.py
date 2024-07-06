import heapq

Camino = 0
Edificio = 1
Agua = 2
Bache = 3

def generar_matriz(filas, columnas):
    matriz = []
    for i in range(filas):
        fila = []
        for j in range(columnas):
            fila.append(Camino)
        matriz.append(fila)
    return matriz


def introducir_obstaculos(mapa):
    while True:
        try:
            filao = input("Introduzca la fila del obstáculo (o 'exit' para salir): ")
            if filao.lower() == 'exit':
                break
            filao = int(filao)
            columnao = int(input("Introduzca la columna del obstáculo: "))
            if 0 <= filao < len(mapa) and 0 <= columnao < len(mapa[0]) and mapa[filao][columnao] == Camino:
                tipo_de_obstaculo = int(input("Introduzca el tipo de obstáculo (1 para edificio, 2 para agua, 3 para bache): "))
                if tipo_de_obstaculo in [Edificio, Agua, Bache]:
                    mapa[filao][columnao] = tipo_de_obstaculo
                else:
                    print("El tipo de obstáculo es inválido. Use 1, 2, o 3.")
            else:
                print("Coordenadas fuera de rango o celda no transitable.")
        except ValueError:
            print("Entrada inválida. Introduzca números enteros.")


def definir_puntos(mapa):
    while True:
        try:
            fila_inicio = int(input("Introduzca la fila del punto de inicio: "))
            columna_inicio = int(input("Introduzca la columna del punto de inicio: "))
            fila_destino = int(input("Introduzca la fila del punto de destino: "))
            columna_destino = int(input("Introduzca la columna del punto de destino: "))

            if 0 <= fila_inicio < len(mapa) and 0 <= columna_inicio < len(mapa[0]) and \
               0 <= fila_destino < len(mapa) and 0 <= columna_destino < len(mapa[0]) and \
               mapa[fila_inicio][columna_inicio] == Camino and mapa[fila_destino][columna_destino] == Camino:
                return (fila_inicio, columna_inicio), (fila_destino, columna_destino)
            else:
                print("Coordenadas fuera de rango o son obstáculos.")
        except ValueError:
            print("Entrada inválida. Introduzca números enteros.")


def imprimir_mapa(mapa, inicio, destino, ruta=None):
    simbolos = {Camino: '.', Bache: 'X', Agua: '~', Edificio: '#'}
    for i, fila in enumerate(mapa):
        for j, celda in enumerate(fila):
            if (i, j) == inicio:
                print('S', end=' ')
            elif (i, j) == destino:
                print('D', end=' ')
            elif ruta and (i, j) in ruta:
                print('*', end=' ')
            else:
                print(simbolos.get(celda, celda), end=' ')
        print()

def heuristica(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def algoritmoa(mapa, inicio, destino):
    filas = len(mapa)
    columnas = len(mapa[0])

    lista_abierta = []
    lista_cerrada = set()
    
    heapq.heappush(lista_abierta, (0, inicio))
    came_from = {}
    g_score = {inicio: 0}
    f_score = {inicio: heuristica(inicio, destino)}
    
    while lista_abierta:
        _, current = heapq.heappop(lista_abierta)

        if current == destino:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(inicio)
            return path[::-1]

        lista_cerrada.add(current)

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            vecino = (current[0] + dx, current[1] + dy)

            if 0 <= vecino[0] < filas and 0 <= vecino[1] < columnas:
                if mapa[vecino[0]][vecino[1]] == Edificio:
                    continue

                tentative_g_score = g_score[current] + 1

                if vecino in lista_cerrada and tentative_g_score >= g_score.get(vecino, float('inf')):
                    continue

                if tentative_g_score < g_score.get(vecino, float('inf')):
                    came_from[vecino] = current
                    g_score[vecino] = tentative_g_score
                    f_score[vecino] = tentative_g_score + heuristica(vecino, destino)
                    if vecino not in [i[1] for i in lista_abierta]:
                        heapq.heappush(lista_abierta, (f_score[vecino], vecino))

    return None


def main():
    filas = int(input("Ingrese el número de filas: "))
    columnas = int(input("Ingrese el número de columnas: "))

    mapa = generar_matriz(filas, columnas)
    introducir_obstaculos(mapa)
    inicio, destino = definir_puntos(mapa)

    ruta = algoritmoa(mapa, inicio, destino)

    if ruta:
        imprimir_mapa(mapa, inicio, destino, ruta)
    else:
        print("No se encontró un camino desde el punto de inicio al destino.")

if __name__ == "__main__":
    main()
