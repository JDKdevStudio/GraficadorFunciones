# Import libraries
import numpy as np
import matplotlib.pyplot as plt


# Initialize
def gasproduced(y):
    return (133.07 / 46.07) * y
def energiaproduced(z):
    return (-1 / 884.54) * z
x = np.linspace(-100, 100, 100)

plt.title("Gráfica de gas y energia producida")
plt.plot(x, energiaproduced(x), label='Energía producida')
plt.plot(x, gasproduced(x), label='Gas producido')


plt.show()

