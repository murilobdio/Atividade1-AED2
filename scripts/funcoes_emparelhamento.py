# =============================================================================
# Funções
# =============================================================================
import os, sys
sys.path.append(os.getcwd())
import numpy as np
from decimal import *

#Função de espalhamento por divisão
def EspalhamentoPorDivisao(key, m):
    if m == 0:
        print('Divisão por 0.')
        return 0
    return key % m 

#Função de espalhamento por multiplicação
def EspalhamentoPorMultiplicacao(key, m, a):
    if a<0 or a>1:
        print('Valor de A inválido.')
        return 0
    
    #Para garantir o arredondamento correto do número resultante da operação (key * a) % 1
    count = 0
    b = a
    while (b % 1 !=0):
        b = b*10
        count = count + 1
    return np.floor(m * round((key * a) % 1, count) +0.000000001)


