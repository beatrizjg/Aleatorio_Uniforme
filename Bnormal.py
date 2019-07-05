#Generacion de numeros aleatorios en python

import numpy as np
import matplotlib.pyplot as plt

mu, sigma = 0, 1 

s = np.random.normal(mu, sigma, 32000) #semilla=32000

count, bins, ignored = plt.hist(s, 50, density=True, alpha = 0.5)

plt.plot(bins, 1/(sigma * np.sqrt(2 * np.pi)) * np.exp( - (bins - mu)**2 / (2 * sigma**2) ),linewidth=2, color='y')

plt.xlabel("Escala X")
plt.ylabel("Escala Y")
plt.title("Distribucion normal")
plt.show()
