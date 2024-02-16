import matplotlib.pyplot as plt
import numpy as np


num_points = 1000
x_values = np.random.uniform(-1, 1, num_points)
y_values = np.random.uniform(-1, 1, num_points)

# Vemos qué puntos caen dentro del círculo
inside_circle = x_values**2 + y_values**2 < 1

# Calculamos la proporción de puntos dentro del círculo con la fórmula explicada
proportion_inside_circle = np.sum(inside_circle) / num_points

plt.figure(figsize=(8, 8))

# Graficar los puntos dentro y fuera del círculo
plt.scatter(x_values[inside_circle], y_values[inside_circle], color='blue', label='Dentro del círculo', s=10)
plt.scatter(x_values[~inside_circle], y_values[~inside_circle], color='red', label='Fuera del círculo', s=10)

# Dibujar la curva del círculo
theta = np.linspace(0, 2*np.pi, 100)
plt.plot(np.cos(theta), np.sin(theta), color='blue')

plt.xlim(-1, 1)
plt.ylim(-1, 1)

plt.xlabel('X')
plt.ylabel('Y')
plt.title('Puntos aleatorios dentro del círculo')

# Mostrar la trama
plt.grid(True)
plt.show()

# Imprimir la proporción de puntos dentro del círculo
print(f'Proporción de puntos dentro del círculo: {proportion_inside_circle:.4f}')