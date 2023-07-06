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
from Metodos import (horarios as hr)


def main(instancia):
    # extrai grafo, colote e une a lista de aulas com o mapa de cores
    grafo, aulas = ds.extraiGrafo(instancia)
    mapaDeCores = cl.colore_grafo(grafo)
    aulas = ds.atribuiCores(mapaDeCores, aulas)

    # chama a função de estrate
    horariosSequenciais = hr.alocaSequencial(aulas)
    ds.geraPlanilhas(aulas, horariosSequenciais, "Sequencial")

    horariosAleatorios = hr.alocaAleatorio(aulas)
    ds.geraPlanilhas(aulas, horariosAleatorios, "Aleatorio")

    horariosPorTurno = hr.alocaPorTurno(aulas)
    ds.geraPlanilhas(aulas, horariosPorTurno, "Dedicado")


if __name__ == '__main__':
    main(str(sys.argv[1]))
