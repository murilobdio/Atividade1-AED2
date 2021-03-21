import os, sys
sys.path.append(os.getcwd())
import matplotlib.pyplot as plt
from exercicios import *

a= Exercicio2b()

fig,axs = plt.subplots(figsize=(24,12))
axs.bar(list(a.keys()), a.values())
axs.margins(0.01)
axs.set_xlabel('H(k)')
axs.set_ylabel('Número de colisões')
plt.show()