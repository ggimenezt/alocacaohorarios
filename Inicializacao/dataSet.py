import pandas as pd
import numpy as np

# Função que le o arquivo de entrada
def leArquivo(instancia):
    # salva o caminho do arquivo de entrada na variável caminho
    caminho = 'Instancias/' + instancia + '.csv'

    # le o arquivo de entrada com a biblioteca pandas e armazena as informações na variável data
    data = pd.read_csv(caminho, delimiter=',')

    return data

# Função que gera o gráfico a partir das informações da plailha
def extraiGrafo(instancia):
    data = leArquivo(instancia)
    # armazena a quantidade de materias presentes na planilha
    tam = len(data)

    infos = []

    # loop para caso a carga horária ser maior que 3, separar a matéria em dois blocos ".1 e .2"
    for i in range(tam):
        if data["CH"][i] <= 3:
            infos.append([data["MATÉRIAS"][i], data["TURMAS"][i],
                         data["PROFESSORES"][i], data["CH"][i]])
        else:
            infos.append([data["MATÉRIAS"][i]+'.1', data["TURMAS"]
                         [i], data["PROFESSORES"][i], 2])
            infos.append([data["MATÉRIAS"][i]+'.2', data["TURMAS"]
                         [i], data["PROFESSORES"][i], data["CH"][i]-2])

    # atualiza o tamanho após as matérias setem separadas em blocos
    infos = np.array(infos)
    tam = len(infos)

    # cria o grafo e caso as matérias possuam turma ou professores iguais, une os vértices com uma aresta
    grafo = np.zeros((tam, tam))
    for i in range(tam):
        for j in range(tam-i-1):
            if infos[i][1] == infos[j+i+1][1] or infos[i][2] == infos[j+i+1][2]:
                grafo[i][j+i+1] = 1
                grafo[j+i+1][i] = 1

    return grafo, infos

# Função que gera os horários reais pós a locação
def geraHorarios(dados, dict_h):
    # cria um array para guardar cor e carga horária
    cor_ch = dados[:, 1:3]

    # loop que verifica em qual periodo o horário foi alocado e coloca no horário ideal dependendo se forem
    # 2 ou 3 aulas
    horario = []
    for i in range(len(dados)):
        hora = dict_h[int(cor_ch[i][0])][:-1]
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

# Função que aloca os horários sequencialmente, começando segunda de manhã, depois de tarde e assim segue
def alocacaoSequencial(dados):
    dict_ch = {}

    # cria um dicionário para armazenar as cargas horárias das matérias presentes em cada cor
    # chave = cor, valores = cargas das matérias
    for cor, hora in dados[:, 1:3]:
        if cor not in dict_ch:
            dict_ch[cor] = []
        dict_ch[cor].append(hora)

    # cria dicionário vazio para armazenar horários das cores
    # chave = cor, valores = horário
    dict_h = {}
    for i in range(len(dict_ch)):
        dict_h[i] = ''

    # loop que verifica qual horário está disponível, se o horário não estiver vai pro próximo horário ou dia
    # encontrando um horário disponível associa o horário a cor
    for _, cor in enumerate(dict_ch):
        dia = 2
        hora = 2
        if '3' in dict_ch[cor]:
            while (dict_h[int(cor)] == ''):
                if str(hora)+str(dia) not in dict_h.values():
                    dict_h[int(cor)] = (str(hora)+str(dia))
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
            while (dict_h[int(cor)] == ''):
                if str(hora)+str(dia) not in dict_h.values():
                    dict_h[int(cor)] = (str(hora)+str(dia))
                else:
                    if hora == 8:
                        hora = hora + 3
                    else:
                        if hora+2 > 13:
                            dia = dia + 1
                            hora = 2
                        else:
                            hora = hora + 2

    # chama função para gerar os horários reais baseado na alocação
    horario = geraHorarios(dados, dict_h)

    return horario

# Função que salva os resultados numa planilha para melhor visualização
def salvaResultados(mapColor, infos):
    # cria um array de materias e outro de carga horária
    materias = infos[:, 0].reshape(-1, 1)
    ch = infos[:, 3].reshape(-1, 1)

    # cria um array com as cores das matérias
    cores = []
    for i in range(len(mapColor)):
        cores.append(mapColor[i])
    cores = np.array(cores)

    # junta todos esses arrays em um só
    dados = np.column_stack([materias, cores.reshape(-1, 1), ch])

    # chama a função para retornar um array com os horários das cores
    horarios = np.array(alocacaoSequencial(dados))

    # junta o array de "matérias, cores, ch" com o de horários
    dados = np.column_stack([dados, horarios.reshape(-1, 1)])

    # cria os labels para indentificar as colunas no arquivo csv
    header = np.array(
        [['MATÉRIAS'], ['CORES'], ['CARGA HORÁRIA'], ['SUGESTÃO']])
    dados = np.row_stack([header.reshape(-1, 4), dados.reshape(-1, 4)])

    # gera um arquivo csv com os horários de cada matéria
    np.savetxt('Resultados/dados.csv', dados, delimiter=",", fmt='%s')

    return 0
