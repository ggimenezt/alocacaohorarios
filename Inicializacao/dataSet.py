import pandas as pd
import numpy as np

def leArquivo(instancia):
    caminho = 'Instancias/' + instancia + '.xlsx'
    
    # Carregar o arquivo Excel usando pandas
    data = pd.read_excel(caminho, sheet_name='Planilha1')
    
    return data

def extraiGrafo(instancia):
    data = leArquivo(instancia)

    tam = len(data)

    grafo = np.zeros((tam, tam))
    np.set_printoptions(threshold=np.inf, linewidth=np.inf)
    
    for i in range(tam-1):
        for j in range(tam-i-1):
            if data["TURMAS"][i] == data["TURMAS"][j+i+1]:
                grafo[i][j+i+1] = 1
                grafo[j+i+1][i] = 1
            if data["PROFESSORES"][i] == data["PROFESSORES"][j+i+1]:
                grafo[i][j+i+1] = 1
                grafo[j+i+1][i] = 1
    return grafo