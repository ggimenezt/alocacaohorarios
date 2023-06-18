import networkx as nx

"""
Função para ler as informações do arquivo e armazane-las em uma matriz do tipo numpy
"""

def leArquivo(instancia):
    # a variável caminho serve para guardar o path do arquivo a ser lido
    caminho = 'Instancias/' + instancia + '.txt'
    # with open() realiza o tratamento do arquivo de forma mais limpa
    # 1. Abrir e ler o arquivo de texto
    with open(caminho, 'r') as arquivo:
        linhas = arquivo.readlines()

    # 2. Criar o objeto Graph
    grafo = nx.Graph()

    # 3. Adicionar vértices ao grafo
    # O número de vértices é determinado pela quantidade de linhas (desconsiderando a primeira linha de rótulos)
    num_vertices = len(linhas) - 1
    grafo.add_nodes_from(range(num_vertices))

    # 4. Adicionar as arestas ao grafo com base na matriz
    for i, linha in enumerate(linhas):
        valores = linha.split()  # Separar os valores da linha
        for j, valor in enumerate(valores):
            if int(valor) == 1:  # Se o valor na matriz for 1, adicionar uma aresta
                grafo.add_edge(i, j)

    return grafo
