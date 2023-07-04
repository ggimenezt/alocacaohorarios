import networkx as nx

def colore_grafo(grafo):
    #adapta o tipo de array para permitir a coloração dos grafos
    #função da biblioteca networkX que colore o grafo começando do vértice de maior grau
    return nx.greedy_color(nx.from_numpy_array(grafo))