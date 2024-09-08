import sys
import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt  # Cambié 'pit' por 'plt', que es más común
import numpy as np

x = np.array(['Comedia', 'Accion', 'Terror'])
y = np.array([3, 1, 10])  # Cambié el set {} por un array/lista []

colores = ["blue", "red", "mediumaquamarine"]

plt.bar(x, y, color=colores)

# Guarda la imagen en un archivo
plt.savefig('grafico_barras.png')
