# =============================================================================
# Funções
# =============================================================================

#Função de espalhamento por divisão
def EspalhamentoPorDivisao(key, m):
    return key % m 

#Função de espalhamento por multiplicação
def EspalhamentoPorMultiplicacao(key, m, a):
    return m * ((key * a) % 1)
