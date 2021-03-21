# =============================================================================
# Exercicios
# =============================================================================
import os, sys
sys.path.append(os.getcwd())
from funcoes_emparelhamento import EspalhamentoPorDivisao, EspalhamentoPorMultiplicacao

def Exercicio1a():
    hk = []
    
    for k in range(0,100):
        hki = EspalhamentoPorDivisao(k, 12)
        if(hki == 3):
            hk.append(k)
            print(k)
            
    return hk

def Exercicio1b():    
    hk = []
    
    for k in range(0,100):
        hki = EspalhamentoPorDivisao(k, 11)
        if(hki == 3):
            hk.append(k)
            print(k)
            
    return hk        

def Exercicio1c(): 
    hk = {}
    hkount = {}
    
    for k in range(0,10000):
        hki = EspalhamentoPorDivisao(k, 97)
        
        if(hki in hk):
            hk[hki].append(k)
            hkount[hki] += 1
            
        else:
            hk[hki] = [k]
            hkount[hki] = 0
    
    return hkount

def Exercicio2a(): 
    hk = {}
    hkount = {}
    
    for k in range(0,500000):
        hki = EspalhamentoPorMultiplicacao(k, 200, 0.62)
        
        if(hki in hk):
            hk[hki].append(k)
            hkount[hki] += 1
            
        else:
            hk[hki] = [k]
            hkount[hki] = 0
    
    return hkount

def Exercicio2b(): 
    hk = {}
    hkount = {}
    
    for k in range(0,500000):
        hki = EspalhamentoPorMultiplicacao(k, 200, 0.61803398875)
        
        if(hki in hk):
            hk[hki].append(k)
            hkount[hki] += 1
            
        else:
            hk[hki] = [k]
            hkount[hki] = 0
    
    return hkount
