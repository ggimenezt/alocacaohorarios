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
import time

from Inicializacao import (dataSet as ds)
from Metodos import (coloracao as cl)

def main(instancia):
    # chama a função para ler arquivo e retorna a matriz numpy
    tempo_inicio = time.time()

    grafo = ds.extraiGrafo(instancia)
    #mapColor = cl.colore_grafo(grafo)
    grau = cl.colore_grafo2(grafo)

    tempo_fim = time.time()
    tempo_total = tempo_fim - tempo_inicio

    #print(grafo)
    print (grau)
    #print(mapColor)
    print("O algoritmo executou em", tempo_total, "segundos.")

if __name__ == '__main__':
    main(str(sys.argv[1]))