#Generacion de numeros aleatorios uniformes en python

from scipy.stats import uniform
import numpy as np
import matplotlib.pyplot as plt

s = np.random.uniform(1,0,32000)#semilla=32000

count, bins, ignored = plt.hist(s, 15, density=True, alpha = 0.5)
plt.plot(bins, np.ones_like(bins), linewidth=2, color='y')

plt.xlabel("Escala X")
plt.ylabel("Escala Y")
plt.title("Distribucion Uniforme")
plt.show()
