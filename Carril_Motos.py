import numpy as np
import matplotlib.pyplot as plt

# Parámetros de la simulación
num_motos = 100
longitud_carril = 100
velocidad_maxima = 5
espacio_moto = 2

# Inicialización de la posición de las motos
posiciones = np.zeros(num_motos)

# Bucle de simulación
tiempo_recorrido = 1000
for tiempo in range(tiempo_recorrido):
    # Actualización de las posiciones de las motos
    for i in range(num_motos):
        posiciones[i] += velocidad_maxima

        # Control de la distancia entre motos
        if i > 0:
            distancia_previa = posiciones[i] - posiciones[i - 1]
            if distancia_previa < espacio_moto:
                posiciones[i] = posiciones[i - 1] + espacio_moto

    # Visualización de la simulación
    plt.clf()
    plt.xlim(0, longitud_carril)
    plt.ylim(0, 1)
    plt.plot(posiciones, np.zeros(num_motos), 'ro')
    plt.pause(0.1)