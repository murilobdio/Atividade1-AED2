import os, sys
sys.path.append(os.getcwd())
from exercicios import *

print(120*'_')
print('Exercicio 1.a)')
Exercicio1a()
print(120*'_')
print('Exercicio 1.b)')
Exercicio1b()
print(120*'_')
print('Exercicio 1.c)')
result = Exercicio1c()
for k in result.keys():
    print(k,':',result[k])
print(120*'_')
print('Exercicio 2.a)')
result = Exercicio2a()
for k in sorted(result.keys()):
    print(k,':',result[k])
print(120*'_')
print('Exercicio 2.b)')
result = Exercicio2b()
for k in sorted(result.keys()):
    print(k,':',result[k])
print(120*'_')