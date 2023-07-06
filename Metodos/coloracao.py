import networkx as nx
import numpy as np


def colore_grafo_networkx(grafo):
    # adapta o tipo de array para permitir a coloração dos grafos
    # função da biblioteca networkX que colore o grafo começando do vértice de maior grau

    return nx.greedy_color(nx.from_numpy_array(grafo), strategy="largest_first")


def colore_grafo(grafo):
    qtd = len(grafo)
    # Cria uma Lista com todos os vértices do grafo
    lista_vertices = list(range(qtd))
    cores = []  # Lista para armazenar as cores

    grau = np.sum(grafo, axis=0)  # Usado para encontrar o grau de um vértice
    # Usado para encontrar a posição do vértice de maior grau
    pos_maior = np.argmax(grau)

    # Quando encontrado o vértice de maior posição, ele é retirado da lista de vértices
    lista_vertices.remove(pos_maior)

    # É alocado a primeira cor (0) ao vértice de maior grau
    dicionario = {pos_maior: 0}
    cores.append(0)  # Adiciona a primeira cor na lista de cores

    # Enquanto ter números na lista vértice que não foram analisados, este while funcionará
    while len(lista_vertices) > 0:
        # Usado para encontrar em forma de lista todos os adjacentes do vértice de maior posição
        vertices_adjacentes = np.where(grafo[pos_maior] == 1)[0]
        grau_maior2 = 0
        cor_adj = []  # Lista de cores dos vértices adjacentes

        # Se pelo menos um vértice adjacente está presente em lista_vertices
        if any(vertice in lista_vertices for vertice in vertices_adjacentes):

            for k in vertices_adjacentes:  # Este FOR acha o maior vértice adjacente
                if k in lista_vertices:
                    if grau[k] > grau_maior2:
                        grau_maior2 = grau[k]
                        pos_maior2 = k

            # Aqui encontra-se uma nova lista de todos adjacentes da nova posição de maior grau
            vertices_adjacentes2 = np.where(grafo[pos_maior2] == 1)[0]

            for g in vertices_adjacentes2:  # Este FOR é usado para criar uma lista de cores adjacentes
                if g in dicionario:
                    cor_adj.append(dicionario[g])

            # Aqui é usado para que caso exista cores repetidas sejam agrupadas, evitando conflitos
            cor_adj_semrep = list(set(cor_adj))

            # Nesta linha copiamos todas cores armazenadas até o momento em outra lista
            cores_adj_dif = cores.copy()

            for b in cor_adj_semrep:
                if b in cores:  # É analisado se a cor adjacente existe em cores
                    # Caso já exista, ela é removida da lista de cores_adj_dif (Cópia de cores)
                    cores_adj_dif.remove(b)

            if len(cores_adj_dif) == 0:  # Se todas as cores adjacentes já existam, a lista será vazia
                # Logo é criado uma nova cor, baseado no ultimo número da lista + 1
                cor_nova = cores[-1] + 1
                dicionario[pos_maior2] = cor_nova
                cores.append(cor_nova)  # A nova cor é alocada na lista cores
            else:  # Caso exista cores adjacentes que não estão na lista de cores_adj_dif, ordenamos a lista e pegamos a menor cor que nenhum adjacente tenha
                cores_adj_dif.sort()
                dicionario[pos_maior2] = cores_adj_dif[0]

            # Removemos para que o while tenha um fim, atualizando a condição
            lista_vertices.remove(pos_maior2)
            pos_maior = pos_maior2  # O pos_maior é atualizado

        else:  # Caso não tenha adjacentes, o número é tratado aqui, encontrando novamente o maior grau que ainda não foi analisado na lista_vértice
            grau_maior2 = 0
            for u in lista_vertices:
                if grau[u] > grau_maior2:
                    grau_maior2 = grau[u]
                    pos_maior2 = u

            vertices_adjacentes2 = np.where(grafo[pos_maior2] == 1)[0]

            for g in vertices_adjacentes2:
                if g in dicionario:
                    cor_adj.append(dicionario[g])

            cor_adj_semrep = list(set(cor_adj))
            cores_adj_dif = cores.copy()

            for b in cor_adj_semrep:
                if b in cores:
                    cores_adj_dif.remove(b)

            if len(cores_adj_dif) == 0:
                cor_nova = cores[-1] + 1
                dicionario[pos_maior2] = cor_nova
                cores.append(cor_nova)
            else:
                cores_adj_dif.sort()  # 0 2
                dicionario[pos_maior2] = cores_adj_dif[0]

            lista_vertices.remove(pos_maior2)
            pos_maior = pos_maior2

    return dicionario
