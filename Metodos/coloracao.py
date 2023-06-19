import networkx as nx

def colore_grafo(grafo):
    grafo = nx.from_numpy_array(grafo)
    return nx.greedy_color(grafo)