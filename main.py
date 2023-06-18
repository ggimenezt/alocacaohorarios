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
Classe principal - desenvolvido em Python 3.11.4
===================================================="""

import sys
from Inicializacao import (dataSet as ds)
from Metodos import (coloracao as cl)

def main(instancia):
    # chama a função para ler arquivo e retorna a matriz numpy
    grafo = ds.leArquivo(instancia)
    teste = cl.colore_grafo(grafo)
    print(teste)
"""Chamada a função main()
   Argumento Entrada: [1] dataset"""


if __name__ == '__main__':
    main(str(sys.argv[1]))