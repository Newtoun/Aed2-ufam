import matplotlib.pyplot as plt
import numpy as np

# Suponha que você tenha um vetor de valores
valores = np.array([1, 2, 3, 2, 4, 5, 3, 2, 1])

# Crie um vetor de índices correspondentes aos valores
indices = np.arange(len(valores))

# Defina um valor de corte para pintar acima ou abaixo
valor_de_corte = 3

# Crie uma figura e um eixo
fig, ax = plt.subplots()

# Pinte a área acima do valor de corte com uma cor
ax.fill_between(indices, valores, where=(valores > valor_de_corte), color='green', alpha=0.5)

# Pinte a área abaixo do valor de corte com outra cor
ax.fill_between(indices, valores, where=(valores <= valor_de_corte), color='red', alpha=0.5)

# Plot os valores
ax.plot(indices, valores, marker='o', linestyle='-')

# Ajuste os limites do eixo Y, se necessário
ax.set_ylim(0, max(valores) + 1)

# Exiba o gráfico
plt.show()
