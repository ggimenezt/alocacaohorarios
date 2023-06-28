import networkx as nx
import numpy as np

def colore_grafo(grafo):
    grafo = nx.from_numpy_array(grafo)
    return nx.greedy_color(grafo)

def colore_grafo2(grafo):
    qtd = len(grafo)
    lista_vertices = []

    for l in range(0, qtd):
        lista_vertices.append(l)
    pos = -1

    grau = np.sum(grafo, axis=0)

    print(grau)

    grau_maior = 0
    for j in range(0, qtd - 1):
        pos = pos + 1  # 0 1
        if grau[j] > grau_maior:
            grau_maior = grau[j]
            pos_maior = pos

    lista_vertices.remove(pos_maior)
    dicionario = {pos_maior: 0}
    posDis = 0

    while len(lista_vertices) > 0:
        vertices_adjacentes = np.where(grafo[pos_maior] == 1)[0]
        grau_maior2 = 0

        if any(vertice in lista_vertices for vertice in vertices_adjacentes): # Pelo menos um vértice adjacente está presente em lista_vertices

            for k in vertices_adjacentes:  # ESTE FOR ACHA O MAIOR GRAU ADJACENTE
                if k in lista_vertices:
                    if grau[k] > grau_maior2:
                        grau_maior2 = grau[k]
                        pos_maior2 = k

            lista_vertices.remove(pos_maior2)
            dicionario[pos_maior2] = posDis + 1
            pos_maior = pos_maior2

        else:
            grau_maior2 = 0  # encontrar grau maior em lista vertice
            for u in lista_vertices:
                if grau[u] > grau_maior2:
                    grau_maior2 = grau[u]
                    pos_maior2 = u

            lista_vertices.remove(pos_maior2)
            dicionario[pos_maior2] = posDis + 1
            pos_maior = pos_maior2

        posDis += 1

    return dicionario

