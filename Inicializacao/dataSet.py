import pandas as pd
import numpy as np
from operator import itemgetter


def leArquivo(instancia):
    caminho = 'Instancias/' + instancia + '.xlsx'

    # Carregar o arquivo Excel usando pandas
    data = pd.read_excel(caminho, sheet_name='Planilha1')

    return data


def extraiGrafo(instancia):
    data = leArquivo(instancia)
    tam = len(data)

    infos = []

    for i in range(tam):
        if data["CH"][i] <= 3:
            infos.append([data["MATÉRIAS"][i], data["TURMAS"][i],
                         data["PROFESSORES"][i], data["CH"][i]])
        else:
            infos.append([data["MATÉRIAS"][i]+'.1', data["TURMAS"]
                         [i], data["PROFESSORES"][i], 2])
            infos.append([data["MATÉRIAS"][i]+'.2', data["TURMAS"]
                         [i], data["PROFESSORES"][i], data["CH"][i]-2])

    infos = np.array(infos)
    tam = len(infos)

    grafo = np.zeros((tam, tam))

    for i in range(tam):
        for j in range(tam-i-1):
            if infos[i][1] == infos[j+i+1][1] or infos[i][2] == infos[j+i+1][2]:
                grafo[i][j+i+1] = 1
                grafo[j+i+1][i] = 1

    return grafo, infos


def geraHorario(dados):
    dict_ch = {}
    cor_ch = dados[:, 1:3]

    for cor, hora in dados[:, 1:3]:
        if cor not in dict_ch:
            dict_ch[cor] = []
        dict_ch[cor].append(hora)

    dict_h = {}
    for i in range(len(dict_ch.keys())):
        dict_h[i] = ''

    for i, cor in enumerate(dict_ch):
        dia = 2
        hora = 2
        if '3' in dict_ch[cor]:
            while (dict_h[i] == ''):
                if str(hora)+str(dia) not in dict_h.values():
                    dict_h[i] = (str(hora)+str(dia))
                else:
                    if hora == 2:
                        hora = hora + 6
                    else:
                        if hora+5 > 13:
                            dia = dia + 1
                            hora = 2
                        else:
                            hora = hora + 5
        else:
            while (dict_h[i] == ''):
                if str(hora)+str(dia) not in dict_h.values():
                    dict_h[i] = (str(hora)+str(dia))
                else:
                    if hora == 8:
                        hora = hora + 3
                    else:
                        if hora+2 > 13:
                            dia = dia + 1
                            hora = 2
                        else:
                            hora = hora + 2

    for i in range(len(dict_h)):
        if int(dict_h[i]) < 100:
            dict_h[i] = '0'+dict_h[i]

    horario = []
    for i in range(len(dados)):
        hora = dict_h[int(cor_ch[i][0])][:-1]
        if hora[0] == '0':
            hora = hora[1:]
        dia = dict_h[int(cor_ch[i][0])][-1]
        if int(cor_ch[i][1]) == 3:

            if int(hora) < 6:
                horario.append(dia+'M'+str(int(hora)-1)+hora+str(int(hora)+1))
            elif int(hora) < 11:
                horario.append(dia+'T'+str(int(hora)-5) +
                               str(int(hora)-4)+str(int(hora)-3))
            else:
                horario.append(dia+'N'+str(int(hora)-10) +
                               str(int(hora)-9)+str(int(hora)-8))
        else:
            if int(hora) < 6:
                horario.append(dia+'M'+hora+str(int(hora)+1))
            elif int(hora) < 11:
                horario.append(dia+'T'+str(int(hora)-5)+str(int(hora)-4))
            else:
                horario.append(dia+'N'+str(int(hora)-10)+str(int(hora)-9))

    return horario


def salvaResultados(mapColor, infos):
    materias = infos[:, 0].reshape(-1, 1)
    ch = infos[:, 3].reshape(-1, 1)
    cores = np.array(list(mapColor.values()))
    dados = np.column_stack([materias, cores.reshape(-1, 1), ch])

    horarios = np.array(geraHorario(dados))

    dados = np.column_stack([dados, horarios.reshape(-1, 1)])

    dados_ordenados = np.array(sorted(dados, key=itemgetter(1)))

    header = np.array(
        [['MATÉRIAS'], ['CORES'], ['CARGA HORÁRIA'], ['SUGESTÃO']])

    dados_ordenados = np.row_stack(
        [header.reshape(-1, 4), dados_ordenados.reshape(-1, 4)])
    dados = np.row_stack([header.reshape(-1, 4), dados.reshape(-1, 4)])

    blank_column = []
    for _ in range(len(dados)):
        blank_column.append('                ')
    blank_column = np.array(blank_column)

    dados = np.column_stack(
        [dados_ordenados, blank_column.reshape(87, -1), dados])

    np.savetxt('Resultados/dados.csv', dados, delimiter=",", fmt='%s')

    return 0
