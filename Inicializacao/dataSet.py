import pandas as pd
import numpy as np
from Metodos import (horarios as hr)

# Função que le o arquivo de entrada


def leArquivo(instancia):
    # salva o caminho do arquivo de entrada na variável caminho
    caminho = 'Instancias/' + instancia + '.csv'
    # le o arquivo de entrada com a biblioteca pandas e armazena as informações na variável data
    materias = pd.read_csv(caminho, delimiter=',')

    return materias

# Função que gera o gráfico a partir das informações da plailha


def extraiGrafo(instancia):
    # Obtem as matérias e suas informações
    materias = leArquivo(instancia)
    # Separa os blocos de aula de cada matéria dependendo da carga horária
    aulas = []
    for i in range(len(materias)):
        if materias["CH"][i] <= 3:
            aulas.append([materias["MATÉRIA"][i], materias["TURMA"][i], materias["PROFESSOR"][i],
                          materias["CH"][i], materias["CURSO"][i], materias["TURNO"][i]])
        else:
            aulas.append([materias["MATÉRIA"][i]+'.1', materias["TURMA"][i], materias["PROFESSOR"][i],
                          2, materias["CURSO"][i], materias["TURNO"][i]])
            aulas.append([materias["MATÉRIA"][i]+'.2', materias["TURMA"][i], materias["PROFESSOR"][i],
                          materias["CH"][i]-2, materias["CURSO"][i], materias["TURNO"][i]])

    # tranforma a lista de aulas em arrays numpy
    aulas = np.array(aulas)
    # obtem o número de aulas para iteração
    tam = len(aulas)
    # cria os dois grafos colocando 0 em todas as posições
    grafo = np.zeros((tam, tam))
    # gera as arestas baseado na igualdade de turmas, professores e turnos
    for i in range(tam):
        for j in range(tam-i-1):
            if aulas[i][1]+aulas[i][4] == aulas[j+i+1][1]+aulas[j+i+1][4] or aulas[i][2] == aulas[j+i+1][2] or aulas[i][5] != aulas[j+i+1][5]:
                grafo[i][j+i+1] = 1
                grafo[j+i+1][i] = 1

    return grafo, aulas

# função que une o array de aulas com o array de cores formando um único array


def atribuiCores(mapaDeCores, aulas):
    cores = []
    for i in range(len(mapaDeCores)):
        cores.append(mapaDeCores[i])
    cores = np.array(cores)

    aulas = np.column_stack([aulas, cores.reshape(-1, 1)])

    return aulas

# função para gerar as planilhas de saídas


def geraPlanilhas(aulas, horarios, pasta):
    # cria lista de turmas
    turmas = []
    for turma in aulas[:, [1, 4]]:
        if turma[0]+turma[1] not in turmas:
            turmas.append(turma[0]+turma[1])

    # cria data frame de horários na semana
    escala_zero = pd.DataFrame({
        'Horários': ['07h00-07h55', '07h55-08h50', '08h50-09h45', '10h10-11h05', '11h05-12h00',
                     '13h30-14h25', '14h25-15h20', '15h45-16h40', '16h40-17h35', '17h35-18h30',
                     '19h00-19h50', '19h50-20h40', '21h00-21h50', '21h50-22h40', '22h40-23h30'],
        2: ['', '', '', '', '',
            '', '', '', '', '',
                    '', '', '', '', ''],
        3: ['', '', '', '', '',
            '', '', '', '', '',
                    '', '', '', '', ''],
        4: ['', '', '', '', '',
            '', '', '', '', '',
                    '', '', '', '', ''],
        5: ['', '', '', '', '',
            '', '', '', '', '',
                    '', '', '', '', ''],
        6: ['', '', '', '', '',
            '', '', '', '', '',
                    '', '', '', '', '']
    })

    # itera em cima da lista de turmas para alimentar o dataframe com o horário de cada turma
    for turma in turmas:
        escala = escala_zero.copy(deep=True)
        for aula in aulas:
            if aula[1]+aula[4] == turma:
                hora_dia = str(horarios[aula[6]])
                hora = int(hora_dia[:-1])-1
                dia = int(hora_dia[-1])

                for i in range(int(aula[3])):
                    if hora < 5 and aula[3] == 3:
                        escala[dia][hora-1+i] = aula[0]
                    else:
                        escala[dia][hora+i] = aula[0]

        escala_doc = escala.copy(deep=True)
        escala_doc = escala_doc.set_index('Horários')
        escala_doc = escala_doc.rename(
            columns={2: 'Segunda', 3: 'Terça', 4: 'Quarta', 5: 'Quinta', 6: 'Sexta'})
        # converte o dataframe da turma para arquivo csv
        escala_doc.to_csv('Resultados/'+pasta+'/Turma-'+turma+'.csv', sep=',')

    sugestoes = hr.geraHorarios(aulas, horarios)
    resultados = aulas[:, [0, 6]]
    resultados = np.column_stack(
        [resultados, np.array(sugestoes).reshape(-1, 1)])
    df_resultados = pd.DataFrame(
        resultados, columns=['MATÉRIAS', 'CORES', 'SUGESTÃO'])
    # gera um arquivo csv com os horários de cada matéria
    df_resultados.to_csv("Resultados/"+pasta+"/dados.csv",
                         sep=',', index=False)

    return 0
