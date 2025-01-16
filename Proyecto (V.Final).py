import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

N = 30  # Número de átomos


C = 1  # Constante elástica

M1 = 5 # Masa 1

M2 = 1 # Masa 2

a = 1  # Espaciado entre átomos del mismo tipo

t_max = 60  # Segundos máximos de simulación
dt = 0.05 # Paso de tiempo

t = np.arange(0, t_max, dt)

x_0 = np.zeros(N)

for i in range(N):
    x_0[i] = i*(a/2)

ka = 3*np.pi/N

omega_optica = (C/(M1*M2))*(M1+M2+np.sqrt(pow(2,M1)+pow(2,M2)+2*M1*M2*np.cos(ka)))

omega_acustica = abs((C/(M1*M2))*(M1+M2-np.sqrt(pow(2,M1)+pow(2,M2)+2*M1*M2*np.cos(ka))))

def generar_posiciones(t,y_0,rama):

    y = np.zeros((len(t),len(y_0)))
    u = np.zeros((len(t),len(y_0)))

    y[0] = y_0

    for i in range(len(t)):

        for j in range(N):

            if rama == 'acustica':

                if j % 2 == 0:  #Atomos pesados

                        u[i,j] = 0.1*np.cos(ka* j * a - np.sqrt(omega_acustica) * t[i])

                else:
                        u[i,j] = 0.1*C*((1 + np.cos(ka)) * np.cos(ka * j - np.sqrt(omega_acustica) * t[i]) -   #Atomos ligeros
                                  np.sin(ka) * np.sin(ka * j - np.sqrt(omega_acustica) * t[i]))/(2 * C - M2 * omega_acustica)

            if rama == 'optica':

                if j % 2 == 0:

                    u[i,j] = 0.05*C*((1 + np.cos(ka)) * np.cos(ka * j - np.sqrt(omega_optica) * t[i]) +
                    np.sin(ka) * np.sin(ka * j - np.sqrt(omega_optica) * t[i]))/(2 * C - M1 * omega_optica)  #Atomos pesados

                else:

                    u[i,j] = 0.05*np.cos(ka* j * a - np.sqrt(omega_optica) * t[i])   #Atomos ligeros

            y[i,j] = y_0[j] + u[i,j]
            
    return y

posiciones_acustica = generar_posiciones(t,x_0,'acustica')
posiciones_optica = generar_posiciones(t,x_0,'optica')

# Crear una lista de tamaños basados en la periodicidad
sizes = np.array([20*M1 if i % 2 == 0 else 20*M2 for i in range(N)])

# Crear la animación
fig, ax = plt.subplots(figsize=(8, 4))
ax.set_xlim(-1, 16 )  # Límites espaciales
ax.set_ylim(-0.5, 0.5)  # Límites verticales (solo para separar visualmente)
ax.set_title('Movimiento de los átomos en una cadena diatómica')
ax.set_xlabel('Posición (m)')
ax.set_yticks([])  # Ocultar eje y


# Crear puntos para los átomos con colores alternantes
colores = ['blue' if i % 2 == 0 else 'red' for i in range(N)]

# Crear el objeto scatter para cada rama con un desplazamiento en y para distinguirlas
offset_y_acustica = 0.2  # Desplazamiento en y para la rama acústica
offset_y_optica = -0.2   # Desplazamiento en y para la rama óptica

puntos_acustica = ax.scatter(x_0, np.full_like(x_0, offset_y_acustica), c='black', s=sizes, label='Rama Acústica')
puntos_optica = ax.scatter(x_0, np.full_like(x_0, offset_y_optica), c='b', s=sizes, label='Rama Óptica')

# Agregar la leyenda con el valor de ka
ax.legend(title=f"ka = {ka:.2f}", loc='upper right')

def actualizar(frame):
    """
    Función para actualizar las posiciones de las dos ramas en cada frame.
    """
    # Posiciones en el tiempo actual para cada rama
    x_acustica = posiciones_acustica[frame]
    x_optica = posiciones_optica[frame]
    
    # Actualizar las posiciones de los objetos scatter
    puntos_acustica.set_offsets(np.c_[x_acustica, np.full_like(x_acustica, offset_y_acustica)])
    puntos_optica.set_offsets(np.c_[x_optica, np.full_like(x_optica, offset_y_optica)])
    
    return puntos_acustica, puntos_optica

# Crear animación
anim = FuncAnimation(fig, actualizar, frames=len(t), interval=1, blit=True)

# Mostrar la animación
plt.show()

