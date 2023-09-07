import random
from matplotlib import pyplot as plt

# Genera una lista de números del 1 al 12 en el eje X
numbers_a = range(1, 13)

# Genera una lista de 12 números aleatorios en el eje Y
numbers_b = [random.randint(1, 1000) for i in range(12)]

# Crea el gráfico de líneas
plt.plot(numbers_a, numbers_b)

# Muestra el gráfico
plt.show()
Este código generará un gráfico de líneas con los números aleatorios en el eje Y y los números del 1 al 12 en el eje X, y luego lo mostrará en una ventana de visualización.





