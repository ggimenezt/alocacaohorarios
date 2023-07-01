import networkx as nx

def colore_grafo(grafo):
    # função da biblioteca networkX que colore o grafo a partir do vértice de maior grau
    grafo = nx.from_numpy_array(grafo, strategy='largest_first')
    return nx.greedy_color(grafo)