"""=================================================
UNIVERSIDADE FEDERAL DE ITAJUBÁ
INSTITUTO DE MATEMÁTICA E COMPUTAÇÃO
CMAC03 - ALGORITMOS E GRAFOS
Prof. Rafael Frinhani

Gustavo Gimenez Teixeira - 2021006467
Caio Miranda Caetano Antunes - 2021024231
Matheus Gonçalves de Souza - 2021009128
Danubia Pereira Borges - 2019018489

Grafos - Programa com funções básicas para práticas de algoritmos em grafos.
Classe principal - desenvolvido em Python 3.10.11
===================================================="""

import sys
from Inicializacao import (dataSet as ds)
from Metodos import (coloracao as cl)

def main(instancia):

    # chama a função para ler arquivo e retorna a matriz numpy
    grafo, infos = ds.extraiGrafo(instancia)
    # chama a função para colorir o grafo e a armazena o mapColor
    mapColor = cl.colore_grafo(grafo)
    # chama a função para salvar os dados em uma planilha de saída
    ds.salvaResultados(mapColor=mapColor, infos=infos)

if __name__ == '__main__':
    main(str(sys.argv[1]))