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
import timeit
import time

def main(instancia):
    start = timeit.default_timer()
    # chama a função para ler arquivo e retorna a matriz numpy
    grafo, infos = ds.extraiGrafo(instancia)
    mapColor = cl.colore_grafo(grafo)
    ds.salvaResultados(mapColor=mapColor, infos=infos)
    end = timeit.default_timer()
    print(f"Tempo de execução: {end - start}s")
if __name__ == '__main__':
    main(str(sys.argv[1]))