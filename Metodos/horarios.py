import random

# função para listar os possíveis horários a serem distribuidos para as cores

# cria as estruturas necessárias para as estratégias de elocações funcionarem


def estruturaAlocacoes(aulas):
    # cria lista de horários disponiveis, separadas por turnos e carga horária
    horas_disponiveis = {
        "MT": {
            2: [],
            3: []
        },
        "N": {
            2: [],
            3: []
        }
    }

    # loop que alimenta a lista de horários disponiveis
    dia = 2
    hora = 2
    while (dia < 7):
        if hora < 11:
            if hora in [2, 8]:
                horas_disponiveis["MT"][2].append(str(hora)+str(dia))
                horas_disponiveis["MT"][3].append(str(hora)+str(dia))
            else:
                horas_disponiveis["MT"][2].append(str(hora)+str(dia))
        else:
            if hora == 13:
                horas_disponiveis["N"][2].append(str(hora)+str(dia))
                horas_disponiveis["N"][3].append(str(hora)+str(dia))
            else:
                horas_disponiveis["N"][2].append(str(hora)+str(dia))

        if hora == 8:
            hora = hora + 3
        else:
            if hora+2 > 13:
                dia = dia + 1
                hora = 2
            else:
                hora = hora + 2
    # cria um dicionário para armazenar as cargas horárias das matérias presentes em cada cor
    # chave = cor, valores = cargas das matérias
    dict_ch = {
        "MT": {},
        "N": {}
    }
    for ch, turno, cor in aulas[:, [3, 5, 6]]:
        if cor not in dict_ch[turno]:
            dict_ch[turno][cor] = []
        dict_ch[turno][cor].append(ch)

    # cria um dicionario para armazenar a carga horária de cada professor no dia
    dict_profs = {}
    for profs in aulas[:, 2]:
        if profs not in dict_profs:
            dict_profs[profs] = {
                2: 0,
                3: 0,
                4: 0,
                5: 0,
                6: 0,
            }

    # cria dicionário vazio para armazenar horários das cores
    # chave = cor, valores = horário
    dict_horarios = {}
    for cor in aulas[:, 6]:
        if cor not in dict_horarios:
            dict_horarios[cor] = ''

    return horas_disponiveis, dict_ch, dict_profs, dict_horarios


def alocaSequencial(aulas):
    # cria estruturas necessárias para o alocamento dos horários
    horas_disponiveis, dict_ch, _, dict_horarios = estruturaAlocacoes(aulas)

    # itera na lista de horas disponiveis por turnos (MT (manhã-tarde) ou N(noite))
    for turno in horas_disponiveis.keys():
        # prioriza os blocos com 3 aulas
        for ch in [3, 2]:
            # itera na lista de cores
            for cor in dict_ch[turno].keys():
                # aloca e romove o primeiro horário disponivel na lista de horários
                if str(ch) in dict_ch[turno][cor] and dict_horarios[cor] == '':
                    if ch == 3:
                        if horas_disponiveis[turno][3] != []:
                            if (horas_disponiveis[turno][3][0] in horas_disponiveis[turno][2]):
                                horas_disponiveis[turno][2].remove(
                                    horas_disponiveis[turno][3][0])
                            dict_horarios[cor] = horas_disponiveis[turno][3].pop(
                                0)
                    else:
                        if horas_disponiveis[turno][2][0] in horas_disponiveis[turno][3]:
                            horas_disponiveis[turno][3].remove(
                                horas_disponiveis[turno][2][0])
                        dict_horarios[cor] = horas_disponiveis[turno][2].pop(0)

    return dict_horarios


def alocaAleatorio(aulas):
    # cria estruturas necessárias para o alocamento dos horários
    horas_disponiveis, dict_ch, _, dict_horarios = estruturaAlocacoes(aulas)

    # itera na lista de horas disponiveis por turnos (MT (manhã-tarde) ou N(noite))
    for turno in horas_disponiveis.keys():
        # prioriza os blocos com 3 aulas
        for ch in [3, 2]:
            # itera na lista de cores
            for cor in dict_ch[turno].keys():
                # sorteia um HORÁRIO PARA A COR e remove o mesmo da lista de horários disponiveis
                if str(ch) in dict_ch[turno][cor] and dict_horarios[cor] == '':
                    if ch == 3:
                        x = random.randint(
                            0, len(horas_disponiveis[turno][3])-1)
                        if horas_disponiveis[turno][3] != []:
                            if (horas_disponiveis[turno][3][x] in horas_disponiveis[turno][2]):
                                horas_disponiveis[turno][2].remove(
                                    horas_disponiveis[turno][3][x])
                            dict_horarios[cor] = horas_disponiveis[turno][3].pop(
                                x)
                    else:
                        x = random.randint(
                            0, len(horas_disponiveis[turno][2])-1)
                        if horas_disponiveis[turno][2][x] in horas_disponiveis[turno][3]:
                            horas_disponiveis[turno][3].remove(
                                horas_disponiveis[turno][2][x])
                        dict_horarios[cor] = horas_disponiveis[turno][2].pop(x)

    return dict_horarios


def alocaPorTurno(aulas):
    # cria estruturas necessárias para o alocamento dos horários
    horas_disponiveis, dict_ch, _, dict_horarios = estruturaAlocacoes(aulas)
    # ordena a lista de horários
    horas_disponiveis["MT"][2] = sorted(horas_disponiveis["MT"][2])
    horas_disponiveis["MT"][3] = sorted(horas_disponiveis["MT"][3])
    # itera na lista de horas disponiveis por turnos (MT (manhã-tarde) ou N(noite))
    for turno in horas_disponiveis.keys():
        # cria uma lista de cores para facilitar o sorteio
        lista_cores = list(dict_ch[turno].keys())
        # itera em cima da quantidade de cores
        for _ in dict_ch[turno].keys():
            # sorteia uma COR PARA O HORÁRIO e remove a cor da lista de cores e o horário da lisra de hoários
            x = random.randint(0, len(lista_cores)-1)
            cor = lista_cores.pop(x)
            # prioriza os blocos com 3 aulas
            for ch in [3, 2]:
                if str(ch) in dict_ch[turno][cor] and dict_horarios[cor] == '':
                    if ch == 3:
                        if horas_disponiveis[turno][3] != []:
                            if (horas_disponiveis[turno][3][0] in horas_disponiveis[turno][2]):
                                horas_disponiveis[turno][2].remove(
                                    horas_disponiveis[turno][3][0])
                            dict_horarios[cor] = horas_disponiveis[turno][3].pop(
                                0)
                    else:
                        if horas_disponiveis[turno][2][0] in horas_disponiveis[turno][3]:
                            horas_disponiveis[turno][3].remove(
                                horas_disponiveis[turno][2][0])
                        dict_horarios[cor] = horas_disponiveis[turno][2].pop(0)

    return dict_horarios


def geraHorarios(aulas, dict_h):
    # cria um array para guardar cor e carga horária
    cor_ch = aulas[:, [6, 3]]

    # loop que verifica em qual periodo o horário foi alocado e coloca no horário ideal dependendo se forem
    # 2 ou 3 aulas
    sugestoes = []
    for i in range(len(aulas)):
        hora = dict_h[cor_ch[i][0]][:-1]
        dia = dict_h[cor_ch[i][0]][-1]
        if int(cor_ch[i][1]) == 3:

            if int(hora) < 6:
                sugestoes.append(dia+'M'+str(int(hora)-1) +
                                 hora+str(int(hora)+1))
            elif int(hora) < 11:
                sugestoes.append(dia+'T'+str(int(hora)-5) +
                                 str(int(hora)-4)+str(int(hora)-3))
            else:
                sugestoes.append(dia+'N'+str(int(hora)-10) +
                                 str(int(hora)-9)+str(int(hora)-8))
        else:
            if int(hora) < 6:
                sugestoes.append(dia+'M'+hora+str(int(hora)+1))
            elif int(hora) < 11:
                sugestoes.append(dia+'T'+str(int(hora)-5)+str(int(hora)-4))
            else:
                sugestoes.append(dia+'N'+str(int(hora)-10)+str(int(hora)-9))

    return sugestoes
